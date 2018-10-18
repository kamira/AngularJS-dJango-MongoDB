from django.http import HttpResponse
from django.shortcuts import render
from pymongo import MongoClient
from bson.objectid import ObjectId
import json

# Create your views here.

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt



@csrf_exempt #忽略 csrf
def POST(request):
    item = json.loads(request.body)
    print(item)

    Mongo_Connection = MongoClient("mongodb://localhost:27017/")
    MG_Database = Mongo_Connection['test']

    DB_Collection = MG_Database['sample']
    try:
        x = item['DATA']
        print(x)
        DB_Collection.insert_one(x)
        return_dict = {'TEXT': "INSERT", "MSG": "SUCCEED"}
    except Exception as e:
        return_dict = {'TEXT': "INSERT", "MSG": "FAILED"}
    return_dict = {'TEXT': "INSERT", "MSG": "FAILED"}
    response = HttpResponse(json.dumps(return_dict))
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response
