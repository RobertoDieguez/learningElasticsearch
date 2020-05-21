from elasticsearch import Elasticsearch

def elastic_instance(cloud_id, user, password):
    return Elasticsearch(cloud_id = cloud_id, http_auth = (user, password))