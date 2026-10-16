from .client_connection import client_connector
from .model_transformers import load_model


def search(query, collection_name, model_name, limit=3):
    model = load_model(model_name)
    embedding = model.encode(query).tolist()

    return client_connector().search(
        collection_name=collection_name,
        data=[embedding],
        anns_field="embedding",
        limit=limit,
        output_fields=["text"],
        search_params={
            "metric_type": "COSINE",
            "params": {"nprobe": 2},
        },
    )