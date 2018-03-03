#coding:utf-8
import requests
import json

class RunMethod:
    def post_main(self,url,data,header=None):
        if header != None:
            res = requests.post(url=url,data=data,header=header).json()
        else:
            res = requests.post(url=url,data=data)
            print res.status_code
        return res.json()

    def get_main(self,url,data,header):
        if header != None:
            res = requests.get(url=url,data=data,header=header).json()
        else:
            res = requests.get(url=url,data=data).json()
        return res.text
    def run_main(self,method,url,data=None,header=None):
        if method == 'post':
            res = self.post_main(url,data,header)
        else:
            res = self.get_main(url,data,header)
        return json.dump(res,ensure_ascii=False,sort_keys=True,indent=2)


