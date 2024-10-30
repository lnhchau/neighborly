import logging
import os
import azure.functions as func
import pymongo
import json
from bson.json_util import dumps


def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python getPosts trigger function processed a request.')

    try:
        url = os.environ.get("MONGO_DB_CONNECTION_STRING")  # TODO: Update with appropriate MongoDB connection information
        client = pymongo.MongoClient(url)
        db_name = os.environ.get("MONGO_DB_NAME")
        database = client[db_name]
        collection = database['posts']

        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8', status_code=200)
    except:
        return func.HttpResponse("Bad request.", status_code=400)