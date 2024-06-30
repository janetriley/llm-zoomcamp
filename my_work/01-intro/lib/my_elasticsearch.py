from elasticsearch import Elasticsearch
from tqdm.auto import tqdm

DEFAULT_INDEX = 'course_questions'
DEFAULT_ES_URL = 'http://localhost:9200'

es_client = Elasticsearch(DEFAULT_ES_URL)


# es_client.info()  # anybody home?


def get_client(url=None):
    global es_client
    if not es_client:
        es_client = Elasticsearch(url or 'http://localhost:9200')
    return es_client


def create_index(index_name=None):
    index_name = index_name or DEFAULT_INDEX
    # create the index
    index_settings = {
        "settings": {
            "number_of_shards": 1,
            "number_of_replicas": 0
        },
        "mappings": {
            "properties": {
                "text": {"type": "text"},
                "section": {"type": "text"},
                "question": {"type": "text"},
                "course": {"type": "keyword"}
            }
        }
    }
    # some logging here with the API response would be luxe
    return get_client().indices.create(index=index_name, body=index_settings)


def load_documents(all_docs, index_name):
    index_name = index_name or DEFAULT_INDEX
    for doc in tqdm(all_docs):
        es_client.index(index=index_name, document=doc)


def search(query, fields=None, course=None, match_type="best_fields", results=5, index_name=None):
    index_name = index_name or DEFAULT_INDEX
    fields = fields or ["question^3", "text", "section"]
    es_filter = {} if not course else {
        "term": {
            "course": course
        }
    }

    search_query = {
        "size": results,
        "query": {
            "bool": {
                "must": {
                    "multi_match": {
                        "query": query,
                        "fields": fields,
                        "type": match_type
                    }
                },
            }
        }
    }
    if course:
        search_query['query']['bool']['filter'] = {"term": {"course": course}}

    response = es_client.search(index=index_name, body=search_query)
    return response['hits']['hits']
