import time

import allure

from tests.litemall_api.goods_api import GoodsApi
from tests.litemall_api.login_api import LoginApi


# litemall商城接口测试
class TestLiteamall:
    def setup_class(self):
        # 完成登录
        login_api = LoginApi()
        login_api.login()
        # 初始化商品api
        self.goods_api = GoodsApi(login_api.session)
        # 学号
        self.pre = "20202277"

    def setup(self):
        # 时间戳
        self.nowtime = str(int(time.time()))
        time.sleep(1)

    @allure.title("商品添加功能")
    def test_add_goods(self):
        # 商品添加功能
        # 用时间戳和学号初始化商品名称、编号
        with allure.step("添加商品"):
            goods_number = self.pre + self.nowtime
            goods_name = self.pre + self.nowtime + "商品名称"
            # 添加商品
            add_goods_resp = self.goods_api.add_goods(goods_number, goods_name)
        with allure.step("获取添加商品响应值"):
            # 获取添加商品响应值
            add_goods_resp_json = add_goods_resp.json()
            assert add_goods_resp.status_code == 200
            assert add_goods_resp_json['errno'] == 0
            assert add_goods_resp_json['errmsg'] == "成功"
        with allure.step("查询商品接口进行断言"):
            # 查询商品接口进行断言
            search_goods_resp = self.goods_api.search_goods(goods_name)
            assert search_goods_resp.status_code == 200
            assert search_goods_resp.json()['data']['list'][0]['goodsSn'] == goods_number

    @allure.title("商品查询功能")
    def test_search_goods(self):
        with allure.step("添加商品"):
            goods_number = self.pre + self.nowtime
            goods_name = self.pre + self.nowtime + "商品名称"
            add_goods_resp = self.goods_api.add_goods(goods_number, goods_name)
        with allure.step("获取添加商品响应值"):
            add_goods_resp_json = add_goods_resp.json()
            assert add_goods_resp.status_code == 200
            assert add_goods_resp_json['errno'] == 0
            assert add_goods_resp_json['errmsg'] == "成功"
        search_goods_resp = self.goods_api.search_goods(goods_name)
        goods_id = search_goods_resp.json()['data']['list'][0]['id']
        goods_detail_resp = self.goods_api.edit_goods(goods_id)
        assert goods_detail_resp.json()['data']['goods']['name'] == goods_name

    @allure.title("商品编辑功能")
    def test_edit_goods(self):
        with allure.step("添加商品"):
            goods_number = self.pre + self.nowtime
            goods_name = self.pre + self.nowtime + "商品名称"
            add_goods_resp = self.goods_api.add_goods(goods_number, goods_name)
        with allure.step("获取添加商品的json"):
            add_goods_resp_json = add_goods_resp.json()
            search_goods_resp = self.goods_api.search_goods(goods_name)
        with allure.step("获取商品id并进行编辑"):
            goods_id = search_goods_resp.json()['data']['list'][0]['id']
            goods_detail_resp = self.goods_api.edit_goods(goods_id)
            edit_goods_json = goods_detail_resp.json()['data']
            edit_goods_name = self.pre + self.nowtime + "修改商品名称"
            edit_goods_json['goods']['name'] = edit_goods_name
        with allure.step("更新商品名称并添加响应"):
            update_goods_resp = self.goods_api.update_goods(edit_goods_json)
            update_goods_resp_json = update_goods_resp.json()
            assert update_goods_resp.status_code == 200
            assert update_goods_resp_json['errno'] == 0
            assert update_goods_resp_json['errmsg'] == "成功"
        with allure.step("再次编辑获取商品名称并获取响应值"):
            goods_detail_resp = self.goods_api.edit_goods(goods_id)
            goods_detail_resp_json = goods_detail_resp.json()
            assert goods_detail_resp_json['data']['goods']['name']

    @allure.title("商品删除功能")
    def test_delete_goods(self):
        with allure.step("添加商品"):
            goods_number = self.pre + self.nowtime
            goods_name = self.pre + self.nowtime + "商品名称"
            add_goods_resp = self.goods_api.add_goods(goods_number, goods_name)
        with allure.step("获取商品id并进行删除"):
            search_goods_resp = self.goods_api.search_goods(goods_name)
            goods_id = search_goods_resp.json()['data']['list'][0]['id']
            delete_goods_resp = self.goods_api.delete_goods(goods_id)
            delete_goods_resp_json = delete_goods_resp.json()
            assert delete_goods_resp.status_code == 200
            assert delete_goods_resp_json['errno'] == 0
            assert delete_goods_resp_json['errmsg'] == "成功"
        with allure.step("再次查询看是否存在并获取响应"):
            search_goods_resp = self.goods_api.search_goods(goods_name)
            search_goods_resp_json = search_goods_resp.json()
            assert search_goods_resp.status_code == 200
            assert search_goods_resp_json['errno'] == 0
            assert search_goods_resp_json['data']['list'] == []
