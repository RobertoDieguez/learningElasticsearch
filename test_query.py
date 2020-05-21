from elastic.credentials import cloud_id, user, password
from elastic.connection import elastic_instance
import pandas as pd

def state_df():
    #Connecting to elasticsearch
    es = elastic_instance(cloud_id, user, password)

    query = {
        "query" : {
            "match" : {
                "state" : "FL"
            }
        }
    }

    response = es.search(index = "accounts", body = query )
    dataframe = pd.DataFrame([account["_source"] for account in response["hits"]["hits"]])
    return dataframe

print(state_df())