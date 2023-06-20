import unittest
import requests
import ManagerUseCase
from BeautifulReport import BeautifulReport

suite = unittest.TestSuite()  # 类的实例化！！！要加括号才是实例化
changeRank = ManagerUseCase.changeRank
getClub = ManagerUseCase.getClub
getRank = ManagerUseCase.getRank
postManager = ManagerUseCase.postManager
deleteManager = ManagerUseCase.deleteManager
getManager = ManagerUseCase.getManager


class ManagerTest(unittest.TestCase):  # 调用unittest
    def tearDown(self) -> None:  # 后置条件
        print("执行结束")  # 打印标示用例执行结束

    def test_changeRank(self):
        # changeRank接口
        print("测试changeRank接口")
        for i in changeRank:
            payload = {
                "as_id": i["as_id"], "user_id": i["user_id"], "manager_id": i["manager_id"]}
            print(payload)
            res = requests.put(url='http://localhost:8081/changeRank',
                               params=payload)
            a = res.text
            print(a)

    def test_getClub(self):
        # getClub接口
        print("测试getClub接口")
        for i in getClub:
            payload = {"user_id": i["user_id"]}
            print(payload)
            res = requests.get('http://localhost:8081/getClub/' + i['user_id'],
                               params=payload)
            a = res.text
            print(a)

    def test_getRank(self):
        # getRank接口
        print("测试getRank接口")
        for i in getRank:
            payload = {"user_id": i["user_id"], "as_id": i["as_id"]}
            print(payload)
            res = requests.get('http://localhost:8081/getRank/' + i['user_id'] + '/' + i['as_id'],
                               params=payload)
            a = res.text
            print(a)

    def test_postManager(self):
        # post Manager接口
        print("测试post Manager接口")
        for i in postManager:
            payload = {"as_id": i["as_id"], "user_id": i["user_id"]}
            print(payload)
            res = requests.post('http://localhost:8081/manager',
                                params=payload)
            a = res.text
            print(a)

    def test_deleteManager(self):
        # delete Manager接口
        print("测试delete Manager接口")
        for i in deleteManager:
            payload = {
                "as_id": i["as_id"], "user_id": i["user_id"], "manager_id": i["manager_id"]}
            print(payload)
            res = requests.delete('http://localhost:8081/manager',
                                  params=payload)
            a = res.text
            print(a)

    def test_getManager(self):
        # get Manager接口
        print("测试get Manager接口")
        for i in getManager:
            payload = {"as_id": i["as_id"], "rank": i["rank"]}
            print(payload)
            res = requests.get('http://localhost:8081/manager/' + i['as_id'] + '/' + i['rank'],
                               params=payload)
            a = res.text
            print(a)

def DoM():
    suite.addTest(ManagerTest('test_changeRank'))
    suite.addTest(ManagerTest('test_getClub'))
    suite.addTest(ManagerTest('test_getRank'))
    suite.addTest(ManagerTest('test_postManager'))
    suite.addTest(ManagerTest('test_deleteManager'))
    suite.addTest(ManagerTest('test_getManager'))
    # 添加用例描述
    result = BeautifulReport(suite)
    result.report(filename='ManagerController测试报告', description='ManagerController',
                  log_path='../../public/static/report')


if __name__ == '__main__':
    suite.addTest(ManagerTest('test_changeRank'))
    suite.addTest(ManagerTest('test_getClub'))
    suite.addTest(ManagerTest('test_getRank'))
    suite.addTest(ManagerTest('test_postManager'))
    suite.addTest(ManagerTest('test_deleteManager'))
    suite.addTest(ManagerTest('test_getManager'))
    # 添加用例描述
    result = BeautifulReport(suite)
    result.report(filename='ManagerController测试报告', description='ManagerController',
                  log_path='./report')
    # unittest.main()
