import requests

from utils.address_common import Address


class TestAddress:
    def setup_class(self):
        #所有用例执行之前只执行一次
        self.address=Address()
        self.access_token = self.address.get_token()

    def setup(self):
        pass

    def test_create_user(self):
        r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/user/create',
                          params={
                              'access_token':self.access_token,
                          },
                          json={
                              "userid": "zhangsan",
                              'name': "张三",
                              'department': [1],
                              "mobile": "+86 13800000000",
                              "email": "zhangsan@gzdev.com",
                          })
        assert r.status_code == 200
        print(r.json())

    def test_get_user(self):
        r = requests.get('https://qyapi.weixin.qq.com/cgi-bin/user/get',
                     params={
                         'access_token':self.access_token,
                         'userid': 'ZhangBin'
                     })
        assert r.status_code == 200
        print(r.text)