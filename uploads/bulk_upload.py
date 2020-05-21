#Man I don't know how to import things from a parent directory in Python :s
import sys
sys.path.append("..")
#--------------------------------------------------

from elastic.credentials import cloud_id, user, password
from elastic.connection import elastic_instance

#Read json file and clean the data we need
f = open("../assets/accounts.json","r")
lines = f.readlines()
data = ""
for line in lines: data += line
f.close()

#Connecting to elasticsearch
es = elastic_instance(cloud_id, user, password)


#Uploading all the data and printing the response
response = es.bulk(index = "accounts", body = data)
print(response["items"])