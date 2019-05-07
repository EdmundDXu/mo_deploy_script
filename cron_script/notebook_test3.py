# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class NotebookTest(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Firefox()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        #self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        #self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_notebook(self):
        driver = self.driver
        driver.get("http://www.momodel.cn:8899/user/login")
        print driver.title
        print "浏览器最大化"
        driver.maximize_window()  #将浏览器最大化显示
        driver.find_element_by_id("username").clear()
        print "enter username"
        driver.find_element_by_id("username").send_keys("edmund")
        driver.find_element_by_id("password").clear()
        print "enter password"
        driver.find_element_by_id("password").send_keys("redhat")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Password'])[1]/following::button[1]").click()
        print "login"
        time.sleep(2)
        print "gpu click"
        driver.find_element_by_css_selector("body > div:nth-child(14) > div > div.ant-modal-wrap.ant-modal-centered > div > div.ant-modal-content > button > span > i").click()
        time.sleep(2)
        print "new app"
        driver.find_element_by_id("Newapp").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='app'])[1]/following::div[3]").click()
        time.sleep(20)
        print "switch to tab 2"
        self.switch_tab(2)
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_1 | ]]
        print "wait filebrowser for 60s"
        for i in range(60):
            try:
                if self.is_element_present(By.ID, "filebrowser"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertTrue(self.is_element_present(By.ID, "filebrowser"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        print "switch to tab 1"
        self.switch_tab(1)
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_local | ]]
        print "refresh tab 1"
        driver.refresh()
        print "select project 1"
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Create Project'])[2]/following::div[7]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='···'])[12]/following::div[3]").click()
        time.sleep(5)
        print "scroll to top"
        driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME) 
        time.sleep(5)
        print "delete project 1"
        driver.find_element_by_xpath("//*[@id=\"LaunchPage_Contain\"]/div/div[1]/div/div/div[1]/div[1]/div[1]/div[2]/span[3]/i").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Are you sure you want to delete this Project?'])[1]/following::div[2]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[1]/following::button[1]").click()
        time.sleep(60)
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
    
    def switch_tab(self,num):
        driver = self.driver
        handles = driver.window_handles           # 获取当前窗口句柄集合（列表类型）
        driver.switch_to.window(handles[num-1])   # 跳转到第num个窗口

if __name__ == "__main__":
    unittest.main()

