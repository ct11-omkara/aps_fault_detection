import pymongo
import pandas as pd
import json
import os
from sensor.config import mongo_client

# client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")
client = pymongo.MongoClient(os.getenv("MONGO_DB_URL"))


DATA_FILE_PATH = "/config/workspace/aps_failure_training_set1.csv"
DATABASE_NAME = 'aps'
COLLECTION_NAME = 'sensor'


if __name__ == "__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and columns {df.shape}")

    #Convert dataframe to json so that we can dump these records in MongoDB
    df.reset_index(drop=True, inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())
    # print(json_record[0])
    
    #insert converted json records to MongoDB

    #===================================================================
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
    
    #                             -OR-
    
    # mongo_client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
    #==============================================================


    print(f"Data inserted successfully...")
