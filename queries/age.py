#Man I don't know how to import things from a parent directo in Python :s
import sys
sys.path.append("..")
#--------------------------------------------------

import pandas as pd
from elastic.connection import elastic_instance
from elastic.credentials import cloud_id, user, password

def get_by_age(age):
    es = elastic_instance(cloud_id, user, password)

    query = {
        "size": 10000,
        "query": {
            "match" : {
                "age" : age
            }
        }
    }
    response = es.search(index = "accounts", body = query )
    dataframe = pd.DataFrame([account["_source"] for account in response["hits"]["hits"]])
    return dataframe

def get_by_age_range(start, end): #start is inclusive end is exclusive
    es = elastic_instance(cloud_id, user, password)
    query = {
    "size": 10000,
    "query": {
        "range" : {
            "age" : {
                "gte" : start,
                "lt" : end
                }
            }
        }
    }
    response = es.search(index = "accounts", body = query )
    dataframe = pd.DataFrame([account["_source"] for account in response["hits"]["hits"]])
    return dataframe


print(get_by_age_range(20,32))