from .client_connection import client_connector


def create_index(collection_name, nlist=128):
    client = client_connector()
    params = client.prepare_index_params()
    params.add_index(
        field_name="embedding",
        index_type="IVF_FLAT",
        metric_type="COSINE",
        params={"nlist": nlist},
    )
    client.create_index(collection_name, params)
    client.load_collection(collection_name)