# iSHIP2
AI-Powered Text Summarizer

# iSHIP2 - AI-Powered Text Summarizer

## Overview
iSHIP2 is a web application built using Flask and Hugging Face Transformers that provides AI-powered text summarization. Users can input large amounts of text, and the application will generate concise summaries, making it easier to digest lengthy documents.

## Features
- User-friendly interface for text input.
- Utilizes the BART model for effective text summarization.
- Handles large texts by splitting them into manageable chunks.
- Displays the summarized output on a separate results page.

## Project Structure
iSHIP2/
├── app.py               # Main Flask application 
├── summarizer.py        # Script containing text summarization logic
├── templates/           # Directory for HTML templates
│   ├── index.html       # Input form for text summarization
│   └── result.html      # Result page displaying the summarized text
├── static/              # Directory for static files (optional)
│   ├── css/             # Directory for CSS files (if needed)
├── requirements.txt     # List of Python dependencies
└── README.md            # Project documentation and setup instructions


## Requirements
Make sure you have Python 3.7 or higher installed. To install the required packages, you can create a virtual environment and use the following command:

```bash
pip install -r requirements.txt

Usage:
On the homepage, enter the text you want to summarize in the provided text area.
Click on the "Summarize" button to generate the summary.
The summary will be displayed on a new page.
