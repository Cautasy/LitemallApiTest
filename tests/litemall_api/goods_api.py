
from tests.litemall_api.base_api import BaseApi, BASE_URL


class GoodsApi(BaseApi):
    def add_goods(self, goods_number, goods_name):
        # 商品添加功能
        add_goods_json = {
            "goods": {
                "picUrl": "",
                "gallery": [],
                "isHot": False,
                "isNew": True,
                "isOnSale": True,
                "goodsSn": goods_number,
                "name": goods_name
            },
            "specifications": [{
                "specification": "规格",
                "value": "标准",
                "picUrl": ""
            }],
            "products": [{
                "id": 0,
                "specifications": ["标准"],
                "price": 0,
                "number": 0,
                "url": ""
            }],
            "attributes": []
        }
        add_goods_url = f"{BASE_URL}/admin/goods/create"
        add_goods_resp = self.myrequest("post", add_goods_url, json=add_goods_json)
        return add_goods_resp

    def search_goods(self, goods_name):
        # 查询商品功能
        search_goods_url = f"{BASE_URL}/admin/goods/list?page=1&limit=20&name={goods_name}&sort=add_time&order=desc"
        search_goods_resp = self.myrequest("get", search_goods_url)
        return search_goods_resp

    def edit_goods(self, goods_id):
        # 商品编辑功能
        edit_goods_url = f"{BASE_URL}/admin/goods/detail?id={goods_id}"
        edit_goods_resp = self.myrequest("get", edit_goods_url)
        return edit_goods_resp

    def update_goods(self, json):
        # 商品更新功能
        update_goods_url = f"{BASE_URL}/admin/goods/update"
        update_goods_resp = self.myrequest("post", update_goods_url, json=json)
        return update_goods_resp

    def delete_goods(self, goods_id):
        # 商品删除功能
        delete_goods_url = f"{BASE_URL}/admin/goods/delete"
        delete_json = {
            "id": goods_id
        }
        delete_goods_resp = self.myrequest("post", delete_goods_url, json=delete_json)
        return delete_goods_resp

    def get_goods_list(self):
        # 获取商品列表
        get_goods_url = f"{BASE_URL}/admin/goods/list?page=1&limit=20&sort=add_time&order=desc&goodsId="
        get_goods_resp = self.myrequest("get", get_goods_url)
        return get_goods_resp
