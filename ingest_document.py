import argparse

from elasticsearch import Elasticsearch

from get_subjects import parse_document

ES_HOST = "localhost:9200"
INDEX_NAME = "content"

def ingest(es_client, document):
    body = {
        "content": document,
        "subjects": parse_document(document)
    }

    es_client.index(index=INDEX_NAME, doc_type="_doc", body=body)

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("document", help="投入する文章")

    args = parser.parse_args()

    es_client = Elasticsearch(ES_HOST)
    
    ingest(es_client, args.document)