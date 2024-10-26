
from transformers import pipeline

# Initialize summarizer model
summarizer = pipeline("summarization")

def split_into_chunks(text, max_chunk_length=1024):
    """
    Split the input text into chunks that are of size max_chunk_length
    so they can be processed by the summarizer model.
    """
    words = text.split()
    chunks = []
    current_chunk = []
    current_length = 0
    
    for word in words:
        current_length += len(word) + 1  # account for space
        if current_length <= max_chunk_length:
            current_chunk.append(word)
        else:
            chunks.append(" ".join(current_chunk))
            current_chunk = [word]
            current_length = len(word) + 1

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks

def summarize_text(text):
    """
    Summarize the input text by splitting it into chunks and processing each chunk.
    """
    chunks = split_into_chunks(text)
    summarized_chunks = []

    for chunk in chunks:
        # Summarize each chunk
        summary = summarizer(chunk, max_length=150, min_length=30, do_sample=False)
        summarized_chunks.append(summary[0]['summary_text'])

    # Join summarized chunks back together
    return " ".join(summarized_chunks)
