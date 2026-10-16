# Milvus Client

Minimal semantic search pipeline for PDF and text files using Milvus and Sentence Transformers.

## Requirements

- Python 3.10+
- Milvus running at `http://localhost:19530`

```bash
pip install -r requirements.txt
```

## Run

```bash
python runner.py path/to/file.txt "your search query"
```

PDF files are supported as well:

```bash
python runner.py path/to/file.pdf "your search query"
```
