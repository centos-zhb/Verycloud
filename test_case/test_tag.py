import json
import requests

from utils.tag_common import  Tag

class TestTag:
    def setup_class(self):
        #所有用例执行之前只执行一次
        self.tag=Tag()
        self.access_token = self.tag.get_token()

    def setup(self):
        #所有用例执行之前都会执行一次
        pass

    # 获取标签组的信息
    def test_tags_list(self):
        r=self.tag.tags_list()
        self.tag.format(r.json())
        assert r.json()["errcode"] == 0
        assert len(r.json()["tag_group"]) > 0

    # 添加标签，测试用例可以包含中英文、特殊字符、纯数字、字母等
    def test_tags_add(self):
        #方法一：加上时间戳保证数据的唯一性
        #方法二：编写可维护的数据
        group_name='0730'
        tag_name='name0730'
        r = self.tag.tags_add(group_name,tag_name)
        assert r.json()['errcode'] == 0

    def test_tags_delete(self):
        #封装复用
        r = self.tag.tags_list()
        self.tag.tags_add('group_del_0730','tag_del_0730')
        r=self.tag.tags_list()

        tag_id=""
        for group in r.json()['tag_group']:
            for tag in group['tag']:
                if tag['name']=='tag_del_0730':
                    print(tag['id'])
                    tag_id=tag['id']
        assert tag_id != ""

        # 删除标签
        self.tag.tags_delete(tag_id)
        # 断言加入
        assert r.json()['errcode'] == 0

        r=self.tag.tags_list()
        tag_id=""
        for group in r.json()['tag_group']:
            for tag in group['tag']:
                if tag['name']=='tag_del_0730':
                    print(tag['id'])
                    tag_id=tag['id']
        assert tag_id == ""
