import json

import requests
from config.VarConfig import ReadConfig

class Tag:
    def get_token(self):
        corpid=ReadConfig().get_token('corpid')
        corpsecret=ReadConfig().get_token('corpsecret')
        # 获取token
        r=requests.get(ReadConfig().get_host('token_host'),params={'corpid': corpid,'corpsecret': corpsecret})
        self.access_token=r.json()['access_token']
        return self.access_token

    def tags_list(self):
        r=requests.post(ReadConfig().get_host('tags_list_host'),params={'access_token': self.access_token})
        self.format(r.json())
        return r

    def tags_add(self,group_name,tag_name):
        r=requests.post(ReadConfig().get_host('tags_add_host'),params={'access_token':self.access_token},
            json={'group_name':group_name,'tag': [{'name':tag_name}]})
        self.format(r.json())
        return r

    def tags_delete(self,tag_id):
        r=requests.post(ReadConfig().get_host('tags_del_host'),params={'access_token':self.access_token},
            json={'tag_id':[tag_id],'group_id':[]})
        self.format(r.json())
        return r

    def format(self,r):
        print(json.dumps(r, indent=2, ensure_ascii=False))