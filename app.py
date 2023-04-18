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
        useragent=UserAgent()
        ua=useragent.random
        #return ua
        return ({
            "user-agent": f"{ua}",
            "response code": 200,
            "creator": "Ammar-Excuted"
        })

class Spam(Resource):
    def post(self):
        nomor=request.form.get("nomor")
        if not nomor:
            return ({
                "message": "nomor tidak valid",
                "response code": 403
            })
        tokoko=requests.post("https://api-v2.bukuwarung.com/api/v2/auth/otp/send",headers={'Host':'api-v2.bukuwarung.com','content-length':'198','sec-ch-ua':'"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile':'?0','user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36','content-type':'application/json','accept':'application/json, text/plain, */*','x-app-version-code':'5050','x-app-version-name':'android','buku-origin':'tokoko','sec-ch-ua-platform':'"Linux"','origin':'https://web.tokoko.id','sec-fetch-site':'cross-site','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://web.tokoko.id/','accept-encoding':'gzip, deflate, br','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',},data=json.dumps({"action":"LOGIN_OTP","countryCode":"+62","deviceId":"test-1","method":"WA","phone":nomor,"clientId":"2e3570c6-317e-4524-b284-980e5a4335b6","clientSecret":"S81VsdrwNUN23YARAL54MFjB2JSV2TLn"})).text
        if "OTP_SENT" in tokoko:
            return ({
                "message": f"Berhasil Spam ke nomor {nomor}",
                "Creator": "AmmarBN",
                "response code": 200
            })
        else:
            return ({
                "message": f"Gagal Spam ke nomor {nomor}",
                "Creator": "AmmarBN",
                "response code": 200
            })

api.add_resource(Spam, "/api/spam", methods=["POST"])
api.add_resource(RandomUa, "/api", methods=["GET"])
if __name__ == "__main__":
    app.run(debug=True,port=5000)
