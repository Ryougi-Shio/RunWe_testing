import unittest
import requests
import UserUseCase
from BeautifulReport import BeautifulReport

suite = unittest.TestSuite()    # 类的实例化！！！要加括号才是实例化
adds = UserUseCase.adds
ids = UserUseCase.ids
searchs = UserUseCase.searchs
modifies = UserUseCase.modifies


class ArticleTest(unittest.TestCase):  # 调用unittest
    def setUp(self) -> None:  # 前置条件
        print()

    def tearDown(self) -> None:          # 后置条件
        print("执行结束")  # 打印标示用例执行结束

    def test_add(self):
        '''
        添加用户
        '''
        # 添加接口
        for i in adds:
            payload = {"phone": i["phone"], "name": i["name"],
                       "password": i["password"], "avatar": i["avatar"]}
            print(payload)
            res = requests.post('http://localhost:8081/user/',
                                params=payload)
            a = res.text
            print(a)

    def test_delete(self):
        '''
        删除用户
        '''
        # 删除接口
        for i in ids:
            res = requests.delete('http://localhost:8081/user/'+i)
            a = res.text
            print(a)

    def test_search(self):
        '''
        搜索用户
        '''
        # 搜索接口
        for i in searchs:
            res = requests.get('http://localhost:8081/SearchUser/'+i)
            a = res.text
            print(a)

    def test_put(self):
        '''
        修改用户信息
        '''
        # 搜索接口
        for i in modifies:
            payload = {"id": i["id"],
                       "gender": i["gender"], 'email': i["email"]}
            res = requests.put('http://localhost:8081/user/', params=payload)
            a = res.text
            print(a)

def DoU():
    suite.addTest(ArticleTest('test_add'))  # 添加测试用例
    suite.addTest(ArticleTest('test_delete'))  # 添加测试用例
    suite.addTest(ArticleTest('test_search'))  # 添加测试用例
    suite.addTest(ArticleTest('test_put'))  # 添加测试用例
    # 添加用例描述
    result = BeautifulReport(suite)
    result.report(filename='UserController测试报告', description='UserController',
                  log_path='../../public/static/report')


if __name__ == '__main__':
    suite.addTest(ArticleTest('test_add'))  # 添加测试用例
    suite.addTest(ArticleTest('test_delete'))  # 添加测试用例
    suite.addTest(ArticleTest('test_search'))  # 添加测试用例
    suite.addTest(ArticleTest('test_put'))  # 添加测试用例
    # 添加用例描述
    result = BeautifulReport(suite)
    result.report(filename='UserController测试报告', description='UserController',
                  log_path='./report')
    # unittest.main()
