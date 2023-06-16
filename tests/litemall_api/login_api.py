from tests.litemall_api.base_api import BaseApi, BASE_URL


class LoginApi(BaseApi):
    def login(self):
        login_json = {
            "username": "hogwarts",
            "password": "test12345",
            "code": ""
        }
        login_url = f"{BASE_URL}/admin/auth/login"
        login_resp = self.myrequest("post", login_url, json=login_json)
        self.session.headers = {
            "x-litemall-admin-token": login_resp.json()['data']['token']
        }
