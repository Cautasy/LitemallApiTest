# import time
#
# import requests
# import urllib3
# from requests import session
#
# BASE_URL = "https://litemall.hogwarts.ceshiren.com"
# # 使用抓包工具
# proxys = {
#     "http": "127.0.0.1:8888",
#     "https": "127.0.0.1:8888"
# }
# urllib3.disable_warnings()
# requests = requests.session()
#
#
# class TestLiteamallApi():
#     def setup_class(self):
#         login_json = {
#             "username": "hogwarts",
#             "password": "test12345",
#             "code": ""
#         }
#         login_url = f"{BASE_URL}/admin/auth/login"
#         login_resp = requests.request("post", login_url, json=login_json, proxies=proxys, verify=False)
#         self.token = login_resp.json()['data']['token']
#         session.headers = {
#             "x-litemall-admin-token": self.token
#         }
#         self.pre = "20202277"
#
#     def setup(self):
#         self.nowtime = str(int(time.time()))
#
#     def test_add_goods(self):
#         goods_number = self.pre + self.nowtime
#         goods_name = self.pre + self.nowtime + "商品名称"
#         add_goods_json = {
#             "goods": {
#                 "picUrl": "",
#                 "gallery": [],
#                 "isHot": False,
#                 "isNew": True,
#                 "isOnSale": True,
#                 "goodsSn": goods_number,
#                 "name": goods_name
#             },
#             "specifications": [{
#                 "specification": "规格",
#                 "value": "标准",
#                 "picUrl": ""
#             }],
#             "products": [{
#                 "id": 0,
#                 "specifications": ["标准"],
#                 "price": 0,
#                 "number": 0,
#                 "url": ""
#             }],
#             "attributes": []
#         }
#         add_goods_url = f"{BASE_URL}/admin/goods/create"
#         add_goods_resp = requests.request("post", add_goods_url, json=add_goods_json,
#                                           proxies=proxys, verify=False)
#         add_goods_resp_json = add_goods_resp.json()
#         assert add_goods_resp.status_code == 200
#         assert add_goods_resp_json['errno'] == 0
#         assert add_goods_resp_json['errmsg'] == "成功"
#
#         search_goods_url = f"{BASE_URL}/admin/goods/list?page=1&limit=20&name={goods_name}&sort=add_time&order=desc"
#         search_goods_rsp = requests.request("get", search_goods_url, proxies=proxys, verify=False)
#         assert search_goods_rsp.json()['data']['list'][0]['goodsSn'] == goods_number
#
#     def test_edit_goods(self):
#         # 商品添加功能
#         goods_number = self.pre + self.nowtime
#         goods_name = self.pre + self.nowtime + "商品名称"
#         add_goods_json = {
#             "goods": {
#                 "picUrl": "",
#                 "gallery": [],
#                 "isHot": False,
#                 "isNew": True,
#                 "isOnSale": True,
#                 "goodsSn": goods_number,
#                 "name": goods_name
#             },
#             "specifications": [{
#                 "specification": "规格",
#                 "value": "标准",
#                 "picUrl": ""
#             }],
#             "products": [{
#                 "id": 0,
#                 "specifications": ["标准"],
#                 "price": 0,
#                 "number": 0,
#                 "url": ""
#             }],
#             "attributes": []
#         }
#         add_goods_url = f"{BASE_URL}/admin/goods/create"
#         add_goods_resp = session.request("post", add_goods_url, json=add_goods_json,
#                                          proxies=proxys, verify=False)
#
#         # 查询商品接口进行断言
#         search_goods_url = f"https://litemall.hogwarts.ceshiren.com/admin/goods/list?page=1&limit=20&name={goods_name}&sort=add_time&order=desc"
#         search_goods_resp = session.request("get", search_goods_url, proxies=proxys, verify=False)
#
#         # 获取商品id
#         goods_id = search_goods_resp.json()['data']['list'][0]['id']
#         # 获取商品详情
#         goods_detail_url = f"https://litemall.hogwarts.ceshiren.com/admin/goods/detail?id={goods_id}"
#         goods_detail_resp = session.request("get", goods_detail_url, proxies=proxys, verify=False)
#         # 提取编辑接口的json
#         edit_goods_json = goods_detail_resp.json()['data']
#         # 编辑商品
#         edit_goods_name = self.pre + self.nowtime + "修改商品名称"
#         edit_goods_json['goods']['name'] = edit_goods_name
#         edit_goods_url = "https://litemall.hogwarts.ceshiren.com/admin/goods/update"
#         edit_goods_resp = session.request("post", edit_goods_url, json=edit_goods_json, proxies=proxys, verify=False)
#         edit_goods_resp_json = edit_goods_resp.json()
#         assert edit_goods_resp.status_code == 200
#         assert edit_goods_resp_json['errno'] == 0
#         assert edit_goods_resp_json['errmsg'] == "成功"
#         # 获取商品详情
#         goods_detail_url = f"https://litemall.hogwarts.ceshiren.com/admin/goods/detail?id={goods_id}"
#         goods_detail_resp = session.request("get", goods_detail_url, proxies=proxys, verify=False)
#         goods_detail_resp_json = goods_detail_resp.json()
#         assert goods_detail_resp_json['data']['goods']['name']
