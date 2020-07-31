import json

import requests
from config.VarConfig import ReadConfig


class Common:
    def get_token(self):
        corpid=ReadConfig().get_token('corpid')
        corpsecret=ReadConfig().get_token('corpsecret')
        # 获取token
        r=requests.get(ReadConfig().get_host('token_host'),params={'corpid': corpid,'corpsecret': corpsecret})
        self.access_token=r.json()['access_token']
        return self.access_token

