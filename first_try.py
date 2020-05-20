from credentials import user, password, cloud_id
from elasticsearch import Elasticsearch

es = Elasticsearch(
    cloud_id = cloud_id,
    http_auth = (user, password)
)

my_first_document = {
    "name": "Roberto",
    "age": 22,
    "student": True
}

res = es.index(index = "testing", id = 1, body = my_first_document)
print(res["result"])

res = es.get(index = "testing", id = 1)
print(res["_source"])