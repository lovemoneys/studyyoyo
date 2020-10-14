#coding:utf-8
import requests,json

class BaseRequest():
    # def __init__(self,method,url,data):
    #     self.url = url
    #     self.data = data
    #     self.method = method

    def send_post(self,url,data):
        res = requests.post(url=url,data=data).text
        return res

    def send_get(self,url,data):
        res = requests.get(url=url,params=data).text
        return res

    def run_main(self,method,url,data):
        if method == "get":
            # res = self.send_get(url,data)
            res = BaseRequest.send_get(self,url,data)
        else:
            res = BaseRequest.send_post(self,url,data)
        try:
            res = json.loads(res)
        except:
            print("这个结果是一个text")
        return res

# request = BaseRequest




