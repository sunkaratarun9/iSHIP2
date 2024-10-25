#importing libraries
from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

# Load summarization model (BART, which works well for summarization)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Chunk the text into smaller parts
def chunk_text(text, chunk_size=1000):
    words = text.split()  # Split the text into words
    chunks = []
    for i in range(0, len(words), chunk_size):
        # Ensure the chunk doesn't exceed the word list length
        chunk = ' '.join(words[i:i + chunk_size])
        chunks.append(chunk)
    return chunks

# Function to summarize the large text
def summarize_large_text(text, chunk_size=512):
    chunks = chunk_text(text, chunk_size)
    summaries = []
    for i, chunk in enumerate(chunks):
        try:
            # Summarize each chunk individually
            summary = summarizer(chunk, max_length=30, min_length=10, do_sample=False)[0]['summary_text']
            # summary = summarizer(chunk, max_length=150, min_length=50, do_sample=False)[0]['summary_text']
            summaries.append(summary)
        except Exception as e:
            # Handle any exceptions that arise during summarization
            summaries.append(f"Error processing chunk {i+1}: {str(e)}")
    # Combine all summaries into one
    return ' '.join(summaries)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    input_text = request.form['text']
    if len(input_text) > 0:
        try:
            # Summarize the input text
            summary = summarize_large_text(input_text)
            return render_template('result.html', summary=summary)
        except Exception as e:
            return render_template('index.html', error=str(e))
    else:
        return render_template('index.html', error="Please enter some text to summarize.")

if __name__ == '__main__':
    app.run(debug=True)





