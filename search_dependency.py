import argparse
import pprint

from elasticsearch import Elasticsearch

from get_subjects import parse_document

ES_HOST = "localhost:9200"
INDEX_NAME = "content"

def search(es_client, search_word):
    query = {
        "query": {
            "bool": {
                "must": [
                    {
                    "query_string": {
                        "default_field": "content",
                        "query": search_word,
                        "analyzer": "sudachi_analyzer"
                        }
                    },
                    {
                        "terms": {
                            "subjects": parse_document(search_word)
                        }
                    }
                ]
            }
        }
    }
    response = es_client.search(index=INDEX_NAME, body=query)
    return response["hits"]

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("search_word", help="検索文字")

    args = parser.parse_args() 

    es_client = Elasticsearch(ES_HOST)
    result = search(es_client, args.search_word)
    pprint.pprint(result)