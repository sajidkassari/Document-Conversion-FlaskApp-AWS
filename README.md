# Document-Conversion-FlaskApp-AWS
This project is a web application that allows users to convert various document formats, such as PDFs, DOCX, TXT, PPTX, XLSX, and CSV files, into different formats like PDFs, DOCX, TXT, and PPTX. It provides a user-friendly interface for uploading files, selecting the desired output format, and downloading the converted files.

KEY FEATURES:

Supports conversion between multiple document formats.
Simple and intuitive user interface.
Utilizes Python Flask for the backend server.
Integrates AWS for deployment using Elastic Beanstalk (EB).
Implements Tailwind CSS for responsive and attractive styling.
Provides seamless conversion functionality powered by ConvertAPI.

USAGE:

Upload the document file you want to convert.
Select the desired output format from the dropdown menu.
Click the "Convert" button to initiate the conversion process.
Once the conversion is complete, download the converted file.

Changes Required to Use the Project:

Obtain a ConvertAPI API key by signing up for an account on the ConvertAPI website.
Once you have the API key, replace the placeholder key in the application.py with your actual API key.
Ensure that the ConvertAPI key is securely stored and not exposed in the project's source code or shared publicly.


GETTING STARTED:

Clone the repository to your local machine.
Install the required dependencies listed in the requirements.txt file.
Run the Flask application locally using the command python application.py
Access the web application in your browser at http://localhost:5000.

CONTRIBUTING:

Contributions are welcome! Feel free to open issues for bug fixes or feature requests, or submit pull requests to contribute improvements to the project.
