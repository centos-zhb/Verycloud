import os
import configparser

# 获取当前文件所在目录得据对路径
parentDirPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 获取存放token信息的文件绝对路径
tokenWeworkElement = parentDirPath + u"\\config\\WeworkElement.ini"

class ReadConfig:
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(tokenWeworkElement)

    def get_token(self,param):
        value = self.cf.get("TOKEN",param)
        return value

    def get_address_token(self,param):
        value = self.cf.get("Address",param)
        return value

    def get_host(self,param):
        value = self.cf.get("HOST",param)
        return value


# if __name__ == '__main__':
#     token1 = ReadConfig().get_host('tokenhost')
#     print(token1)