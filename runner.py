import argparse
from pathlib import Path

from src.chat import search
from src.create_collection import create_collection
from src.model_transformers import load_model
from src.pdf_encoding import insert_pdf
from src.text_encoding import insert_text

MODEL = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"


def run(path, query, collection_name="documents", model_name=MODEL):
    model = load_model(model_name)
    dimension = model.get_sentence_embedding_dimension()
    create_collection(collection_name, dimension)

    if Path(path).suffix.lower() == ".pdf":
        insert_pdf(path, collection_name, model_name)
    else:
        insert_text(path, collection_name, model_name)

    return search(query, collection_name, model_name)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    parser.add_argument("query")
    parser.add_argument("--collection", default="documents")
    args = parser.parse_args()
    print(run(args.path, args.query, args.collection))


if __name__ == "__main__":
    main()
