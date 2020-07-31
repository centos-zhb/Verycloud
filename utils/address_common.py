import requests
import json
from config.VarConfig import ReadConfig
from utils.tag_common import Tag

class Address:
    def get_token(self):
        corpid=ReadConfig().get_address_token('corpid')
        corpsecret=ReadConfig().get_address_token('corpsecret')
        # 获取token
        r=requests.get(ReadConfig().get_host('token_host'),params={'corpid': corpid,'corpsecret': corpsecret})
        self.access_token=r.json()['access_token']
        return self.access_token

    def create_user(self):
        r=requests.post(ReadConfig.get_host('address_cre_host'),params={'access_token': self.access_token,})