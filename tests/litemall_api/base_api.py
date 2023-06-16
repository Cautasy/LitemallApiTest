import requests
import urllib3

BASE_URL = "https://litemall.hogwarts.ceshiren.com"
# 使用抓包工具
proxys = {
    "http": "127.0.0.1:8888",
    "https": "127.0.0.1:8888"
}
urllib3.disable_warnings()


class BaseApi:
    def __init__(self, session=None):
        # 当session为None的使用才进行初始化
        if session is None:
            self.session = requests.Session()
        else:
            self.session = session

    def myrequest(self, method, url, **kwargs):
        # 封装自定义的请求函数，传入代理配置
        return self.session.request(method=method, url=url, proxies=proxys, verify=False, **kwargs)
