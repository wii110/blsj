#coding:utf-8
from selenium import webdriver
from common.base import Base
import time
# login_url='http://192.168.0.181:9001/cas/login?service=http://192.168.0.181:9003/haems-web/cas'
# login_url='http://192.168.0.181:9001/cas/login?service=http://192.168.0.181:9000/base-web/cas'

class Analysis(Base):#继承
    '''上报审核元素定位'''
    '''点击事件分析管理'''
    loc_1=('xpath','//div[@id="app"]//span[contains(text(),"事件分析管理")]')
    '''点击事件分析目录'''
    loc_2 = ('xpath', '//*[@id="app"]/div/section/section/aside/div[1]/ul/div/li[3]/ul/div/li[1]')
    '''点击事件分析列表'''
    loc_3=('xpath','//*[@id="pane-1"]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[17]/div/button/span')
    '''点击事件讨论 '''
    loc_4=('xpath','//div[contains(text(),"事件讨论") and @id="tab-1"]')
    # loc_4 = ('xpath', '/html/body/div/div/section/section/aside/div[1]/ul/div/li[3]/ul/div/li[1]')
    '''选择讨论时间'''
    # loc_5=('xpath','//*[@id="pane-1"]/div/div[1]/div/div/form/div[3]/div/div[1]/input')
    loc_5 = ('xpath', '//*[@id="pane-1"]//input[@placeholder="选择日期时间"]')
    '''选择此刻'''
    loc_6=('xpath','//span[contains(text(),"此刻")]')
    '''选择讨论地点'''
    loc_7=('xpath','//*[@id="pane-1"]/div/div[1]/div/div/form/div[4]/div/div[1]/div/input')
    '''选择护理部'''
    loc_8=('xpath','//div[@x-placement="bottom-start"]//span[contains(text(),"护理部")][1]')
    '''点击暂存'''
    loc_9=('xpath','//span[contains(text(),"暂存")]')
    '''选择病理技师不在岗'''
    loc_10=('xpath','//span[contains(text(),"病理技师不在岗") and @class="el-checkbox__label"]')
    '''点击暂存'''
    loc_11=('xpath','//div[@id="box"]//span[contains(text(),"暂存")]')
    '''选择病理技师不在岗'''
    loc_111=('xpath','//span[contains(text(),"病理技师不在岗") ]')




    '''点击暂存'''
    loc_12=('xpath','//span[contains(text(),"暂存") ]')
    '''点击新增临时对策'''
    '''录入对应的名称对策'''
    '''点击确定'''
    '''点击暂存'''
    '''点击审核安排'''
    loc_13=('xpath','//div[contains(text(),"审核安排") and @id="tab-7" ]')
    '''点击选择层级'''
    loc_14=('xpath','//*[@id="pane-7"]/div/form/div[3]/div[1]/div/div/div/div[1]/input')
    '''选择层级片区'''
    loc_15=('xpath','//span[contains(text(),"片区审核")]')
    # '''选择审核科室'''
    '''点击选择审核人'''
    loc_16=('xpath','//*[@id="pane-7"]/div/form/div[3]/div[3]/div/div/div/div[1]/div/div/input')
    '''选择人员性质'''
    loc_17=('xpath','//li[@role="menuitem"]//span[contains(text(),"护士")]')
    '''选择审核人'''
    loc_18=('xpath','//li[@role="menuitem"]//span[contains(text(),"管*员")]')
    '''点击提交'''
    loc_19=('xpath','//*[@id="pane-2"]//span[contains(text(),"提交分析")]')
    #loc_19=('xpayh','//*[@id="pane-2"]/div/div[3]/button[2]/span')
    '''点击确定'''
    locqd=('xpath','//div[@tabindex="-1"]//span[contains(text(),"确定")]')
    # loc_191=('xpath','//span[contains(text(),"确定")]')
    # loc_200=('xpath','/html/body/div[5]/div/div[3]/button/span')
    '''点击事件分析审核'''
    loc_20=('xpath','//*[@id="app"]/div/section/section/aside/div[1]/ul/div/li[3]/ul/div/li[2]')
    # loc_200=('xpath','//span[contains(text(),"确定")]')
    '''获取事件分析审核列表第一个事件名称'''
    loc_21=('xpath','//*[@id="pane-1"]/div[1]/div[3]/table/tbody/tr[1]/td[6]/div')
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
        self.click(self.loc_10)
        time.sleep(3)
        self.click(self.loc_11)
        time.sleep(3)
        self.click(self.loc_111)
        time.sleep(3)
        self.click(self.loc_12)
        time.sleep(3)
        self.click(self.loc_13)
        time.sleep(3)
        self.click(self.loc_14)
        time.sleep(3)
        self.click(self.loc_15)
        time.sleep(3)
        self.click(self.loc_16)
        time.sleep(3)
        self.click(self.loc_17)
        time.sleep(3)
        self.click(self.loc_18)
        time.sleep(3)
        self.click(self.loc_19)
        time.sleep(6)
        self.click(self.locqd)
        time.sleep(3)
        self.click(self.loc_20)
        time.sleep(3)

    def is_analysis_name(self, _text):
            return self.is_text_in_element(self.loc_21, _text)