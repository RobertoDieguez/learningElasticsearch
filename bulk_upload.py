from credentials import cloud_id, user, password
from elasticsearch import Elasticsearch

#Read json file and clean the data we need
f = open("accounts.json","r")
lines = f.readlines()
data = ""
for line in lines: data += line
f.close()

#Connecting to elasticsearch
es = Elasticsearch(
    cloud_id = cloud_id,
    http_auth = (user, password)
)

#Uploading all the data and printing the response
response = es.bulk(index = "accounts", body = data)
print(response["items"])
