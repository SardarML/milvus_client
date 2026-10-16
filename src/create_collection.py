from .client_connection import client_connector
from .collection_index import create_index
from .schema import schema


def create_collection(collection_name, dimension):
    client = client_connector()
    if client.has_collection(collection_name=collection_name):
        return
    client.create_collection(
        collection_name=collection_name,
        schema=schema(dimension),
    )
    create_index(collection_name)
