#coding:utf-8
from selenium import webdriver
from common.base import Base
import time
# login_url='http://192.168.0.181:9001/cas/login?service=http://192.168.0.181:9003/haems-web/cas'
# login_url='http://192.168.0.181:9001/cas/login?service=http://192.168.0.181:9000/base-web/cas'

class Analysis_audit(Base):#继承
    '''上报审核元素定位'''
    '''点击事件分析管理'''
    loc_1=('xpath','//div[@id="app"]//span[contains(text(),"事件分析管理")]')
    '''点击事件分析审核目录'''
    loc_2=('xpath','//li[contains(text(),"事件分析审核")]')
    '''点击分析审核列表'''
    loc_3=('xpath','//*[@id="pane-1"]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[23]/div/button/span')
    '''点击分析审核标签'''
    loc_4=('xpath','//div[contains(text(),"分析审核") and @id="tab-7" ]')

    '''点击通过'''
    loc_5=('xpath','//span[contains(text(),"通过")]')
    '''提交审核'''
    loc_6=('xpath','//span[contains(text(),"提交审核")]')
    '''点击确认'''
    loc_7=('xpath','//span[contains(text(),"确定")]')
    '''点击目录事件整改管理'''
    loc_8=('xpath','//span[contains(text(),"事件整改管理")]')
    '''点击事件整改指派'''
    loc_9=('xpath','//li[contains(text(),"事件整改指派")  ]')
    '''获取整改列表的事件名称'''
    loc_10=('xpath','//*[@id="pane-first"]/div[1]/div[3]/table/tbody/tr[1]/td[8]/div')
    def ana_analysis(self):
        # self.click(self.loc_1)
        time.sleep(3)
        self.click(self.loc_2)
        time.sleep(3)
        self.click(self.loc_3)
        time.sleep(3)

        self.click(self.loc_4)
        time.sleep(3)

        self.click(self.loc_5)
        time.sleep(3)

        self.click(self.loc_6)
        time.sleep(3)

        self.click(self.loc_7)
        time.sleep(3)
        self.click(self.loc_8)
        time.sleep(3)
        self.click(self.loc_9)
        time.sleep(3)

    def is_analysis_audit_name(self, _text):
            return self.is_text_in_element(self.loc_10, _text)


