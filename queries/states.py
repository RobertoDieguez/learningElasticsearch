#Man I don't know how to import things from a parent directo in Python :s
import sys
sys.path.append("..")
#--------------------------------------------------

import pandas as pd
from elastic.connection import elastic_instance
from elastic.credentials import cloud_id, user, password

def get_by_state(state):
    #Connecting to elasticsearch
    es = elastic_instance(cloud_id, user, password)

    query = {
        "size": 10000,
        "query": {
            "match" : {
                "state" : state
            }
        }
    }

    response = es.search(index = "accounts", body = query )
    dataframe = pd.DataFrame([account["_source"] for account in response["hits"]["hits"]])
    return dataframe

def get_by_states(states):
    return pd.concat([get_by_state(state) for state in states]).set_index("account_number").sort_values(by = ["account_number"])

print(get_by_states(["FL", "ID","CA"]))
