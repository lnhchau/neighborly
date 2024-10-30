import azure.functions as func
import pymongo
import json
from bson.json_util import dumps
from bson.objectid import ObjectId
import logging
import os

def main(req: func.HttpRequest) -> func.HttpResponse:

    # example call http://localhost:7071/api/getAdvertisement/?id=5eb6cb8884f10e06dc6a2084

    id = req.params.get('id')
    print("--------------->", id)
    
    if id:
        try:
            url = os.environ.get("MONGO_DB_CONNECTION_STRING")  # TODO: Update with appropriate MongoDB connection information
            print("The url is: ", url)
            client = pymongo.MongoClient(url)
            db_name = os.environ.get("MONGO_DB_NAME")
            database = client[db_name]
            print("The db_name is: ", db_name)
            collection = database['advertisements']
            print("The collection is: ", collection)
           
            query = {'_id': ObjectId(id)}
            result = collection.find_one(query)
            print("----------result--------")

            result = dumps(result)
            print(result)

            return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
        except:
            return func.HttpResponse("Database connection error.", status_code=500)

    else:
        return func.HttpResponse("Please pass an id parameter in the query string.", status_code=400)