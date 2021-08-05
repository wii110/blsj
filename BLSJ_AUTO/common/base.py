from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
#from  selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select



class Base():
    def __init__(self,driver:webdriver.Chrome):
        self.driver=driver #打开浏览器的一个实例参数
        self.timeout=10  #超时的总时长
        self.t=1 # 循环去查询的间隙时间默认0.5秒
        #ignored_exceptions=None 默认为空，忽略找不到的异常默认NoSuchElementException
        

    def findElementNew(self,locator):
        #'''定位到元素，返回元素对象，没有定位到，Timeout异常'''
        ele = WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_element_located(locator))
        return  ele
    def findElement(self,locator):

    # # ele = WebDriverWait(driver, 5, 1).until(lambda x: x.find_element_by_xpath('.//*[@id="account"]'))
        ele = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_element(*locator))
        return ele
    #     if not isinstance(locator,tuple):
    #         print('locator参数类型错误，必须传元祖类型: loc = ("id", "valuel")')
    #     else:
    #         print("正在定位元素信息: 定位方式->%s"%(locator[0], locator[1]))
    #         ele =WebDriverWait(self.driver,self.timeout,self.t).until(lambda x: x.find_element(*locator))
    #         return  ele
    def findElements(self,locator):
        '''定位一组元素'''
        try:
        # eles = WebDriverWait(driver, 5, 1).until(lambda x: x.find_element_by_xpath('.//*[@id="account"]'))
            eles = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_elements(*locator))
            return eles
        except:
            return []
    # def finfElements(self,locator):
    #
    # # ele = WebDriverWait(driver, 5, 1).until(lambda x: x.find_element_by_xpath('.//*[@id="account"]'))
    #     eles = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_elements(*locator))
    #     return eles
    def sendKeys(self,locator,text):
        '''封装输入'''
        ele=self.findElement(locator)
        ele.send_keys(text)
    def click(self,locator):
        '''封装点击'''
        ele=self.findElement(locator)
        ele.click()
    def clear(self,locator):
        '''封装清空'''
        ele=self.findElement(locator)
        ele.clear()
    def isSelected(self,locator):
        '''判断元素是否被选中，返回bool值'''
        ele=self.findElement(locator)
        r=ele.is_selected()
        return r

    def isElementExist(self,locator): #判断元素存在
        try:
            self.findElement(locator)
            return True
        except:
            return False
    def isElementExist2(self,locator):#判断多个元素
        try:
            eles = self.findElement(locator)
            n=len(eles)
            if n==0:
                return False

            elif n==1:
                return True
            else:
                print('定位到元素的个数: %s'%n)
                return True
        except:
            return False

    def  is_title(self,_title):

        '''返回bool值'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_is(_title))
            return result
        except:
            return False
    def  is_title_contains(self,_title):

        '''返回bool值'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_contains(_title))
            return result
        except:
            return False

    def  is_text_in_element(self,locator,_text):
        '''返回bool值'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element(locator,_text))
            return  result
        except:
            return False
    def is_value_in_element(self,locator,_value):
        '''返回bool值,Value为空字符串返回False'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until( EC.text_to_be_present_in_element_value(locator,_value))
            return result
        except:
            return False
    def is_alert(self):
        '''判断alert'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until( EC.alert_is_present())
            return result
        except:
            return False
    def get_text(self,locator):
        try:
            t=self.findElement(locator).text
            return t
        except:
            print('获取失败')
            return ''
    def move_to_element(self, locator):
        '''鼠标悬停操作方法'''
        ele = self.findElement(locator)
        ActionChains(driver).move_to_element(ele).perform()

    def select_by_index(self, locator,index=0):
        '''通过索引，index是索引第几个，从0开始，默认选第一个'''
        element = self.findElement(locator) #定位select那一栏
        Select(element).select_by_index(index)
    def select_by_value(self, locator,value):
        '''通过value属性定位'''
        element = self.findElement(locator) #
        Select(element).select_by_value(value)

    def select_by_text(self, locator,text):
        '''通过文本属性定位'''
        element = self.findElement(locator) #
        Select(element).select_by_visible_text(text)

    def js_focus_element(self, locator):
        '''聚焦元素'''
        target = self.findElement(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();",target)
    def js_scroll_top(self, locator):
        '''滚动到顶部'''
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)
    def js_scroll_end(self, locator):
        '''滚动到底部'''
        js = "window.scrollTo(0, document.body.scrollHeight)"
        self.driver.execute_script(js)
    def js_scroll_end_1(self, x=0):
        '''横向滚动'''
        js = "window.scrollTo(%s, document.body.scrollHeight)"%x
        self.driver.execute_script(js)




if __name__=='__main__':
    driver = webdriver.Chrome()
    driver.get('http://192.168.101.5/zentao/user-login-L3plbnRhby8=.html')
    zentao=Base(driver)
    # loc1 = (By.XPATH, './/*[@id="account"]')
    # loc2 = (By.XPATH, './/*[@name="password"]')
    # loc3 = (By.XPATH, './/*[@type="submit" and @id="submit" ]')

    loc1 = ('xpath', './/*[@id="account"]')
    loc2 = ('xpath', './/*[@name="password"]')
    loc3 = ('xpath', './/*[@type="submit" and @id="submit" ]')
    # driver.switch_to ()
    zentao.sendKeys(loc1,'admin')
    zentao.sendKeys(loc2,'123456')
    zentao. click(loc3)


    # zentao.finfElement(loc1).send_keys('111')
    # zentao.finfElement(loc2).send_keys('111')
    # zentao.finfElement(loc3).click()


