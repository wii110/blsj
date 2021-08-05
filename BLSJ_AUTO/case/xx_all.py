from selenium import  webdriver
import unittest
import time
from common.base import Base
from pages.login_page import LoginPage,login_url
from pages.page_audit import Audit
from pages.page_analysis import Analysis
from pages.analysis_audit import Analysis_audit



# 1输入admin，输入123456 点击登录
# 2输入admin，输入 点击登录
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

# chrome_options = Options()# 模拟器设置
# options.add_experimental_option('excludeSwitches', ['enable-automation'])
# driver = webdriver.Chrome(chrome_options=chrome_options) # 将配置文件加载进webdriver

class LoginCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.loginp = LoginPage(cls.driver)
        cls.audit = Audit(cls.driver)
        cls.analysis = Analysis(cls.driver)
        cls.ana1 = Analysis_audit(cls.driver)


    def setUp(self):
        # url = 'http://192.168.0.159/zentao/user-login-L3plbnRhby8=.html'
        # 打开浏览器
        self.driver.get(login_url)
        self.driver.maximize_window()
        # print('先打开浏览器')
        self.driver.delete_all_cookies()  # 清空cookies退出登录
        self.driver.refresh()
        self.loginp.is_alert()
        # print('关闭浏览器')


    def test_01(self):
        ''' 正常登录'''
        self.loginp.login()

        # self.loginp.input_user('thinkgem')
        # self.loginp.input_pwd('password')
        # self.loginp.click_login()
        # result=self.loginp.get_login_name()
        # user1=self.loginp.get_login_result('您好, 管*员 ')
        # print('测试结果 "%s' %  user1)
        # user2=self.loginp.is_add_bug_sucess('您好, 管*员 ')
        # print('测试结果 "%s' %  user2)
        # self.assertTrue(user2)
        time.sleep(11)
        self.loginp.add_aeinfo()
        time.sleep(3)
        user2 = self.loginp.is_add_bug_sucess('反反复复')
        print('测试结果 "%s' %  user2)
        self.assertTrue(user2)
        # result=self.loginp.is_add_bug_sucess('护理部 , 管*员')
        # print('测试结果 "%s' %  result)
        # self.assertTrue(result)
    def test_02(self):
        ''' 正常登录'''
        self.loginp.login()

        # self.loginp.input_user('thinkgem')
        # self.loginp.input_pwd('password')
        # self.loginp.click_login()
        # result=self.loginp.get_login_name()
        # user1=self.loginp.get_login_result('您好, 管*员 ')
        # print('测试结果 "%s' %  user1)
        # user2=self.loginp.is_add_bug_sucess('您好, 管*员 ')
        # print('测试结果 "%s' %  user2)
        # self.assertTrue(user2)
        time.sleep(11)
        self.loginp.add_aeinfo()
        self.audit.add_dudit()
        audit_name = self.audit.is_audit_name('反反复复')
        print('测试结果 "%s' % audit_name)
        self.assertTrue(audit_name)
    def test_03(self):
        ''' 正常登录'''
        self.loginp.login()
        time.sleep(11)
        # self.loginp.add_aeinfo()
        #
        # # self.loginp.input_user('thinkgem')
        # # self.loginp.input_pwd('password')
        # # self.loginp.click_login()
        # # result=self.loginp.get_login_name()
        # # user1=self.loginp.get_login_result('您好, 管*员 ')
        # # print('测试结果 "%s' %  user1)
        # # user2=self.loginp.is_add_bug_sucess('您好, 管*员 ')
        # # print('测试结果 "%s' %  user2)
        # # self.assertTrue(user2)
        # self.audit.add_dudit()
        self.loginp.add_aeinfo()
        self.audit.add_dudit()
        self.analysis.ana_analysis()
        analysis_name=self.analysis.is_analysis_name('反反复复')
        print('测试结果 "%s' % analysis_name)
        self.assertTrue(analysis_name)
    def test_04(self):
        ''' 正常登录'''
        self.loginp.login()
        time.sleep(11)
        self.loginp.add_aeinfo()
        self.audit.add_dudit()
        self.analysis.ana_analysis()
        self.ana1.ana_analysis()
        zg_name=self.ana1.is_analysis_audit_name('反反复复')
        print('测试结果 "%s' % zg_name)
        self.assertTrue(zg_name)
    # self.assertTrue( user1 == '您好, 管*员 ')
    # print('测试结果 "%s' % result)
    # self.assertTrue(result == '您好, 管*员 ')
    # r2=

        #断言
    #
    # def test_02(self):
    #     ''' 不输入账号登录'''
    #
    #     self.loginp.input_user('admin')
    #     self.loginp.click_login()
    #     result = self.loginp.get_login_name()
    #     self.assertTrue(result == '')
    #     #断言
    #
    #
    # def test_03(self):
    #     ''' 不输入用户名登录'''
    #     self.loginp.input_user('')
    #     self.loginp.input_pwd('123456')
    #     self.loginp.click_login()
    #     result = self.loginp.get_login_name()
    #     self.assertTrue(result == '')
    #     # 断言
    #
    # def test_04(self):
    #     ''' 先点击保持登录在进行登录'''
    #
    #     self.loginp.input_user('admin')
    #     self.loginp.input_pwd('123456')
    #     self.loginp.keep_login()
    #     self.loginp.click_login()
    #     result=self.loginp.get_login_name()
    #     self.assertTrue(result == 'admin')
    #     #断言
    #
    # def test_05(self):
    #     # ''' 点击忘记密码'''
    #     self.loginp.click_forget_psw()
    #     result = self.loginp.is_refresh_exist()
    #     print(result)
    #     self.assertTrue(result)
    #     # b='刷新'
    #     # a=self.loginp.is_add_bug_sucess(b)
    #     # print(a)
    #     # self.assertTrue(a)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()



if __name__ == '__main__':
    unittest.main()

