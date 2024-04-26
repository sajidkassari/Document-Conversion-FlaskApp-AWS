from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
import convertapi

application = Flask(__name__)
application.config['SECRET_KEY'] = 'your-secret-key'  # Secret key for session management
convertapi.api_secret = 'your-secret-key'  # Set ConvertAPI secret key

# Define supported input and output file types
SUPPORTED_FILE_TYPES = {
    'pdf': 'PDF ',
    'docx': 'Microsoft Word Document ',
    'pptx': 'Microsoft PowerPoint Presentation ',
    'txt': 'Plain Text Document ',
    'html': 'HTML Document ',
    'xlsx': 'Microsoft Excel Spreadsheet ',
    'csv': 'Comma-Separated Values '
}

# Define supported conversions
SUPPORTED_CONVERSIONS = {
    'pdf': ['docx', 'pptx', 'txt', 'html', 'xlsx', 'csv'],
    'docx': ['pdf', 'txt'],
    'pptx': ['pdf', 'txt'],
    'txt': ['pdf', 'docx'],
    'html': ['pdf', 'docx'],
    'xlsx': ['pdf'],
    'csv': ['pdf']
}

# Configure upload and download folders
UPLOAD_FOLDER = 'uploads'
application.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

DOWNLOAD_FOLDER = 'downloads'
application.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER
if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

@application.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Handle file upload
        file = request.files['file']
        if file:
            filename = file.filename
            file_ext = filename.rsplit('.', 1)[1].lower()
            if file_ext in SUPPORTED_FILE_TYPES:
                # Save the uploaded file to the upload folder
                file_path = os.path.join(application.config['UPLOAD_FOLDER'], filename)
                file.save(file_path)
                return redirect(url_for('convert', filename=filename))
            else:
                return render_template('index.html', error='Unsupported file type.')
    return render_template('index.html', supported_types=SUPPORTED_FILE_TYPES)

@application.route('/convert/<filename>', methods=['GET'])
def convert(filename):
    # Render the conversion page with options
    file_ext = filename.rsplit('.', 1)[1].lower()
    if file_ext in SUPPORTED_CONVERSIONS:
        return render_template('convert.html', filename=filename, supported_conversions=SUPPORTED_CONVERSIONS[file_ext])
    else:
        return render_template('error.html', message='Unsupported conversion.')

@application.route('/process/<filename>', methods=['POST'])
def process(filename):
    # Process the conversion request
    output_format = request.form['output_format']
    try:
        # Convert the file using ConvertAPI
        result = convertapi.convert(output_format, { 'File': f'./{UPLOAD_FOLDER}/{filename}' })
        # Save the converted file
        converted_filename = f'{filename.rsplit(".", 1)[0]}.{output_format}'
        result.file.save(f'./{DOWNLOAD_FOLDER}/{converted_filename}')
        return redirect(url_for('download', filename=converted_filename))
    except Exception as e:
        return render_template('error.html', message=str(e))


@application.route('/download/<filename>', methods=['GET'])
def download(filename):
    # Serve the converted file for download
    return send_from_directory(directory=application.config['DOWNLOAD_FOLDER'], path=filename, as_attachment=True)

if __name__ == '__main__':
    application.run(debug=True)
