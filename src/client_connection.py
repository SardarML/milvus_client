from pymilvus import MilvusClient


def client_connector():
    return MilvusClient(uri="http://localhost:19530")