from .client_connection import client_connector
from .model_transformers import load_model


def load_text(path):
    with open(path, encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]


def insert_text(path, collection_name, model_name):
    texts = load_text(path)
    model = load_model(model_name)
    embeddings = model.encode(texts)

    data = [
        {"embedding": embedding.tolist(), "text": text}
        for text, embedding in zip(texts, embeddings)
    ]
    return client_connector().insert(collection_name=collection_name, data=data)