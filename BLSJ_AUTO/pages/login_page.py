from selenium import webdriver
from common.base import Base
import time
login_url='http://192.168.0.181:9001/cas/login?service=http://192.168.0.181:9003/haems-web/cas'
# login_url='http://192.168.0.181:9001/cas/login?service=http://192.168.0.181:9000/base-web/cas'

class LoginPage(Base):#继承

    #定位登录
    loc1_user = ('xpath', '//*[@id="username"]')
    loc2_psw= ('xpath', '//*[@id="password"]')
    loc3_button = ('xpath', '//*[@id="fm1"]/div[4]/div/input')


    # loc4_keep=('xpath','//*[@id="keeplogin"]/label')
    # loc5_forget_psw=('xpath','//*[@id="login-form"]/form/table/tbody/tr[4]/td/a')
    '''判断user是否存在'''
    loc6_get_user=('xpath','//*[@id="userInfo"]/a')
    '''点击不良事件图标'''
    loc7_blsj=('xpath','//ul[@id="systemIconList"]/li[5]/a/p')
    '''获取登录用户'''
    loc8_admin=('xpath','//p[@role="button"]')
    '''事件上报管理元素'''
    loc9_addinfo=('xpath',"//span[contains(text(),'事件上报管理')]")
    '''事件上报元素'''
    loc10_addinfo1=('xpath','//*[@id="app"]/div/section/section/aside/div[1]/ul/div/li[2]/ul/div/li[1]')

    '''新增上报元素'''
    loc11_addinfo2=('xpath','.//main[@class="el-main"]//span[contains(text(),"新增上报")]')
    # loc11_addinfo2=('//*[@id="pane-list"]/form/div[6]/div/button/span')
    '''选择事件反反复复'''
    loc12_ffff=('xpath',"//div[@class='cell']//span[contains(text(),'反反复复')]")
    '''点击其它'''
    loc13_qt=('xpath',"//span[contains(text(),'其它')]")
    '''选择日期'''
    loc14_evtime=('xpath','//input[@name="evTime"]')
    '''点击此刻'''
    loc15_chike=('xpath',"//span[contains(text(),'此刻')]")
    '''事件伤害级别'''
    loc16_shcd=('xpath','//input[@name="aeLevel"]')
    '''选择事件伤害级别O级'''
    loc17_addshcd=('xpath',"//span[contains(text(),'〇级')]")
    '''选择单选1'''
    loc18_xyx1=('xpath',"//label[@id='option_radio']//span[contains(text(),'选项1')]")
    '''点击下一项'''
    loc19_xyx2=('xpath','//button[@type="button"]//span[contains(text(),"下一项 (表单未完成)")]')
    # loc20_xyx3=('xpath','')
    # loc21_xyx4 = ('xpath', '')
    # loc21_xyx5 = ('xpath', '')
    '''选择正常上报'''
    loc20_zcsb=('xpath',"//span[contains(text(),'正常上报')]")
    '''点击提交按钮'''
    loc21_tj=('xpath','//button[@class="el-button el-button--primary el-button--mini"]//span[contains(text(),"提交")]')
    '''选择审核人'''
    loc22_djsh=('xpath','//*[@id="pane-add"]/div[1]/div/div[7]/div/div[2]/form/div[3]/div/div/div/input')
    '''选择护士'''
    loc23_djshryxz=('xpath','//div[@class="el-cascader-panel"]//span[contains(text(),"护士")]')
    # loc23_djshryxz=('xpath','//*[@id="cascader-menu-8395-1-0"]/span')
    '''选择管理员'''
    loc24_gly=('xpath','//li[@role="menuitem"]//span[contains(text(),"管*员")]')
    '''点击确定'''
    # frame1=("xpath",'//iframe[@id="xh-bar"]')
    # loc25_qd=('xpath','//div[@class="el-picker-panel__footer"]//span[contains(text(),"确定")]')
    loc25_qd =('xpath','//*[@id="pane-add"]/div[1]/div/div[7]/div/div[3]/div/button[2]/span')
    '''清除状态'''
    loc26_qczt=('xpath','//*[@id="pane-list"]/form/div[3]/div/div/div[2]/span/span/i')
    '''点击查询'''
    loc27_djcx=('xpath','//div[@id="pane-list"]//span[contains(text(),"查询")]')

    # loc7_forget_psw_page=('xpath',"/html/body/div/div/div[2]/p/a")
    '''获取事件名称文本'''
    loc28=('xpath','//*[@id="pane-list"]/div[1]/div[3]/table/tbody/tr[1]/td[6]/div')
    def input_user(self,text=""):
        self.sendKeys(self.loc1_user,text)
    def input_pwd(self,text=""):
        self.sendKeys(self.loc2_psw,text)
    def click_login(self):
        self.click(self.loc3_button)

    # def keep_login(self):
    #     self.click(self.loc4_keep)
    # def click_forget_psw(self):
    #     self.click(self.loc5_forget_psw)
    # #def login(self,user='admin',psw='123456'):
    #     self.driver.get('http://192.168.0.159/zentao/user-login-L3plbnRhby8=.html')
    #     self.sendKeys(self.loc1,user)
    #     self.sendKeys(self.loc2,psw)
    #     self.click(self.loc3)
    # a=('xpth','//*[@id="mainmenu"]/ul/li[1]/a/span')
    # def is_add_bug_sucess(self,_text):
    #     return self.is_text_in_element(self.a, _text)
    def get_login_name(self):
        user=self.get_text(self.loc6_get_user)
        return  user
    def get_login_result(self,user):
        result=self.is_text_in_element(self.loc6_get_user,user)
        return result
    def is_add_bug_sucess(self,_text):
        return self.is_text_in_element(self.loc28,_text)


    # def is_alert_exist(self):
    #     '''判断alert是不是存在'''
    #     a = self.is_alert()
    #     if a:
    #         print(a.text)
    #         a.accept()

    # def is_refresh_exist(self):
    #     # '''判断忘记密码页没刷新按钮是否存在'''
    #     m= self.isElementExist(self.loc7_forget_psw_page)
    #     return m

    # def is_add_bug_sucess(self, _text):
    #     return self.is_text_in_element(self.loc6_get_user, _text)

    def login(self,user='thinkgem',psw='password'):#keep开关
        '''二次封装登录流程'''
        self.driver.get(login_url)
        self.input_user(user)
        self.input_pwd(psw)
        # if keep_login1:self.keep_login()
        self.click_login()
        # frame = self.findElement(("name","mainFrame"))
        # self.driver.switch_to.frame(frame)
        # self.click(self.loc7_blsj)
        # self.driver.switch_to.default_content()
    def add_aeinfo(self):
        self.click(self.loc9_addinfo)
        time.sleep(3)
        self.click(self.loc10_addinfo1)
        time.sleep(4)
        self.click(self.loc11_addinfo2)
        time.sleep(3)
        self.click(self.loc12_ffff)
        self.click(self.loc13_qt)
        self.click(self.loc14_evtime)
        time.sleep(3)
        self.click(self.loc15_chike)
        self.click(self.loc16_shcd)
        time.sleep(3)
        self.click(self.loc17_addshcd)
        time.sleep(3)
        self.click(self.loc18_xyx1)
        time.sleep(3)
        self.click(self.loc19_xyx2)
        self.click(self.loc20_zcsb)
        self.click(self.loc21_tj)
        self.click(self.loc22_djsh)
        time.sleep(3)
        self.click(self.loc23_djshryxz)
        self.click(self.loc24_gly)
        # # id_1=()
        # frame = self.findElement(("class name", "ke-edit-iframe"))
        # # self.driver.switch_to.frame(frame)
        # frame1 = ("xpath", '//iframe[@id="xh-bar"]')
        # self.driver.switch_to.frame("xh-bar")
        # self.driver.switch_to("xh-bar")
        self.click(self.loc25_qd)
        # self.driver.switch_to.default_content()
        time.sleep(5)
        self.click(self.loc26_qczt)
        self.click(self.loc27_djcx)




if __name__=='__main__':
    driver=webdriver.Chrome()
    login_page=LoginPage(driver)
    # driver.get(login_url)
    # login_page.input_user('admin')
    # login_page.input_pwd('123456')
    # login_page.keep_login()
    # login_page.click_login()
    # login_page.login(keep_login1=True)#keep开关，ture为保持登录，False为不点击保持登录
    login_page.login()
    #js处理不良事件时间
    #有readOnly用readonly=false，没有直接改
    # time.sleep(11)
    # js = "a=document.getElementsByName('')[0];" \
    #        "a.value='2020-05';"
    # driver.execute_script(js)
    #

