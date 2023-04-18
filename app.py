import re
from urllib import response
from flask import Flask,request
from flask_restful import Resource, Api
from flask_cors import CORS
from fake_useragent import UserAgent
import os,requests,json,random,string,time

app=Flask(__name__)
api=Api(app)

CORS(app)


class RandomUa(Resource):
    def get(self):
        return ({
            "user-agent": "ua",
            "response code": 200,
            "creator": "Ammar-Excuted"
        })

api.add_resource(RandomUa, "/api", methods=["GET"])
if __name__ == "__main__":
    app.run(debug=True,port=5005)
