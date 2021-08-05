#coding:utf-8
from selenium import webdriver
from common.base import Base
import time
# login_url='http://192.168.0.181:9001/cas/login?service=http://192.168.0.181:9003/haems-web/cas'
# login_url='http://192.168.0.181:9001/cas/login?service=http://192.168.0.181:9000/base-web/cas'

class Audit(Base):#继承
    '''上报审核元素定位'''
    '''点击事件上报管理'''
    loc_1=('xpath',"//span[contains(text(),'事件上报管理')]")
    '''点击事件上报审核'''
    loc_2 = ('xpath', "//*[@id='app']/div/section/section/aside/div[1]/ul/div/li[2]/ul/div/li[2]")
    '''点击事件列表上报审核 '''
    loc_3=('xpath','//*[@id="pane-1"]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[19]/div/button')
    '''点击上报审核'''
    loc_4=('xpath','//*[@id="pane-2"]//div[@class="el-tabs__item is-top"]')
    # '''选择事件点击上报审核'''
    # '''点击上报审核'''
    '''点击通过'''
    loc_5=('xpath','//div[@id="pane-1"]//span[contains(text(),"通过")]')
    '''点击提交审核'''
    loc_6=("xpath",'// div[ @ id = "pane-2"] // span[contains(text(), "提交审核")]')
    '''点击确认'''
    loc_66=("xpath",'//span[contains(text(),"确定")]')
    '''点击事件分析管理'''
    loc_7=('xpath','//span[contains(text(),"事件分析管理")]')
    # loc_7 = ('xpath', '//*[@id="app"]/div/section/section/aside/div[1]/ul/div/li[3]/div/span')
    '''点击事件分析'''
    loc_8=('xpath','//li[contains(text(),"事件分析")][1]')
    '''获取第一条数据的名称'''
    loc_9=('xpath','//*[@id="pane-1"]/div[1]/div[3]/table/tbody/tr[1]/td[6]/div')



    def add_dudit(self):
        # self.click(self.loc_1)
        # time.sleep(4)
        self.click(self.loc_2)
        time.sleep(4)
        self.click(self.loc_3)
        time.sleep(4)
        self.click(self.loc_4)
        time.sleep(4)
        self.click(self.loc_5)
        time.sleep(4)
        self.click(self.loc_6)
        # loc_11=("xpath",'//iframe[@id="xh-bar"]')
        # time.sleep(10)
        # self.driver.switch_to.frame(loc_11)

        time.sleep(4)
        self.click(self.loc_66)
        time.sleep(4)
        self.driver.switch_to.default_content()
        self.click(self.loc_7)
        time.sleep(4)
        self.click(self.loc_8)
        time.sleep(4)

    def is_audit_name(self, _text):
        return self.is_text_in_element(self.loc_9, _text)
