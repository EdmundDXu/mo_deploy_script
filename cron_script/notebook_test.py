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
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_notebook(self):
        driver = self.driver
        driver.get("http://www.momodel.cn:8899/workspace?tab=app")
        driver.find_element_by_id("Newapp").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='应用'])[1]/following::div[3]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_1 | ]]
        for i in range(60):
            try:
                if self.is_element_present(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='SHUTDOWN'])[1]/following::div[2]"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertTrue(self.is_element_present(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Help'])[1]/following::div[2]"))
        except AssertionError as e: self.verificationErrors.append(str(e))
    
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

if __name__ == "__main__":
    unittest.main()
