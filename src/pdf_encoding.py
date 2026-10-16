import re

import PyPDF2

from .client_connection import client_connector
from .model_transformers import load_model


def load_pdf(path):
    reader = PyPDF2.PdfReader(path)
    text = "\n".join(page.extract_text() or "" for page in reader.pages)
    return [x.strip() for x in re.split(r"\n\d+(?:\.\d+)*\s+", text) if x.strip()]


def insert_pdf(path, collection_name, model_name):
    texts = load_pdf(path)
    model = load_model(model_name)
    embeddings = model.encode(texts)

    data = [
        {"embedding": embedding.tolist(), "text": text}
        for text, embedding in zip(texts, embeddings)
    ]
    return client_connector().insert(collection_name=collection_name, data=data)