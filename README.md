# RAG Chatbot Project

This project is aimed at developing a Retrieval-Augmented Generation (RAG) chatbot using AWS services.

## Project Structure

- `app/`: Contains the main application code.
  - `extract_text.py`: Code for extracting text from PDFs.
  - `index_data.py`: Code for indexing extracted text into OpenSearch.
  - `config.py`: Configuration details.
- `notebooks/`: Contains Jupyter notebooks for testing and development.
- `requirements.txt`: List of dependencies.
- `README.md`: Project documentation.
- `.gitignore`: Files and directories to be ignored by git.

## Setup Instructions

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
