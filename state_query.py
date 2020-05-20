from credentials import cloud_id, user, password
from elasticsearch import Elasticsearch

#Connecting to elasticsearch
es = Elasticsearch(
    cloud_id = cloud_id,
    http_auth = (user, password)
)

query = {
    "query" : {
        "match" : {
            "state" : "FL"
        }
    }
}

response = es.search(index = "accounts", body = query )
print(response["hits"]["hits"])