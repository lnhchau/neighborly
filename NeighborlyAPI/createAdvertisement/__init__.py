import azure.functions as func
import pymongo
import os

def main(req: func.HttpRequest) -> func.HttpResponse:

    request = req.get_json()

    if request:
        try:
            url = os.environ.get("MONGO_DB_CONNECTION_STRING")  # TODO: Update with appropriate MongoDB connection information
            client = pymongo.MongoClient(url)
            db_name = os.environ.get("MONGO_DB_NAME")
            database = client[db_name]
            collection = database['advertisements']

            rec_id1 = collection.insert_one(eval(request))

            return func.HttpResponse(req.get_body())

        except ValueError:
            print("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)

    else:
        return func.HttpResponse(
            "Please pass name in the body",
            status_code=400
        )