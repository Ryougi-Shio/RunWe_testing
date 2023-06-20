import unittest
import requests
import FollowUseCase
from BeautifulReport import BeautifulReport

suite = unittest.TestSuite()  # 类的实例化！！！要加括号才是实例化
follow = FollowUseCase.follow
getFollow = FollowUseCase.getFollow
commonFollow = FollowUseCase.commonFollow
followOrNot = FollowUseCase.followOrNot


class FollowTest(unittest.TestCase):  # 调用unittest
    def tearDown(self) -> None:  # 后置条件
        print("执行结束")  # 打印标示用例执行结束

    def test_follow(self):
        # 关注接口
        print("测试关注接口")
        for i in follow:
            payload = {"userId": i["userId"], "followUserId": i["followUserId"]}
            print(payload)
            res = requests.post(url='http://localhost:8081/follow',
                                data={'userId': i['userId'],
                                      'followUserId': i['followUserId']})
            a = res.text
            print(a)

    def test_getFollow(self):
        # 返回关注列表接口
        print("测试返回关注列表接口")
        for i in getFollow:
            payload = {"id": i["id"]}
            print(payload)
            res = requests.get('http://localhost:8081/follow/' + i['id'],
                               params=payload)
            a = res.text
            print(a)

    def test_followOrNot(self):
        # 是否关注接口
        print("测试是否关注接口")
        for i in followOrNot:
            payload = {"userId": i["userId"], "followUserId": i["followUserId"]}
            print(payload)
            res = requests.get('http://localhost:8081/follow/or/not/' + i['followUserId'],
                               params=payload)
            a = res.text
            print(a)

    def test_commonFollow(self):
        # 共同关注接口
        print("测试共同关注接口")
        for i in commonFollow:
            payload = {"id": i["id"], "userId": i["UserId"]}
            print(payload)
            res = requests.get('http://localhost:8081/follow/common/' + i['id'],
                               params=payload)
            a = res.text
            print(a)


if __name__ == '__main__':
    suite.addTest(FollowTest('test_follow'))
    suite.addTest(FollowTest('test_getFollow'))
    suite.addTest(FollowTest('test_followOrNot'))
    suite.addTest(FollowTest('test_commonFollow'))
    # 添加用例描述
    result = BeautifulReport(suite)
    result.report(filename='FollowController测试报告', description='FollowController',
                  log_path='./report')
    # unittest.main()
