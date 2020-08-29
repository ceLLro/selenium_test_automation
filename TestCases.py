from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.keys import Keys

CHROME_DRIVER_PATH = "C:\\Program Files (x86)\\chromedriver.exe"
WEB_PAGE = "https://rahulshettyacademy.com/AutomationPractice/"


class RadioButtons(unittest.TestCase):
    def test_RadioButton_1(self):
        try:
            driver = webdriver.Chrome(CHROME_DRIVER_PATH)
            driver.get(WEB_PAGE)
            time.sleep(2)
            element = driver.find_element_by_xpath("//input[@name='radioButton' and @value='radio1']")
            element.click()
            if element.is_selected():
                self.assertTrue(True)
            else:
                self.assertTrue(False)
        except:
            self.assertTrue(False)
        time.sleep(1)
        driver.quit()

    def test_RadioButton_2(self):
        try:
            driver = webdriver.Chrome(CHROME_DRIVER_PATH)
            driver.get(WEB_PAGE)
            time.sleep(2)
            element = driver.find_element_by_xpath("//input[@name='radioButton' and @value='radio2']")
            element.click()
            if element.is_selected():
                self.assertTrue(True)
            else:
                self.assertTrue(False)
        except:
            self.assertTrue(False)
        time.sleep(1)
        driver.quit()

    def test_RadioButton_3(self):
        try:
            driver = webdriver.Chrome(CHROME_DRIVER_PATH)
            driver.get(WEB_PAGE)
            time.sleep(2)
            element = driver.find_element_by_xpath("//input[@name='radioButton' and @value='radio3']")
            element.click()
            if element.is_selected():
                self.assertTrue(True)
            else:
                self.assertTrue(False)
        except:
            self.assertTrue(False)
        time.sleep(1)
        driver.quit()


class CheckBoxes(unittest.TestCase):
    def test_CheckBox_1(self):
        try:
            driver = webdriver.Chrome(CHROME_DRIVER_PATH)
            driver.get(WEB_PAGE)
            time.sleep(2)
            element = driver.find_element_by_xpath("//input[@id='checkBoxOption1' and @value='option1']")
            element.click()
            if element.is_selected():
                self.assertTrue(True)
            else:
                self.assertTrue(False)
        except:
            self.assertTrue(False)
        time.sleep(1)
        driver.quit()

    def test_CheckBox_2(self):
        try:
            driver = webdriver.Chrome(CHROME_DRIVER_PATH)
            driver.get(WEB_PAGE)
            time.sleep(2)
            element = driver.find_element_by_xpath("//input[@id='checkBoxOption2' and @value='option2']")
            element.click()
            if element.is_selected():
                self.assertTrue(True)
            else:
                self.assertTrue(False)
        except:
            self.assertTrue(False)
        time.sleep(1)
        driver.quit()

    def test_CheckBox_3(self):
        try:
            driver = webdriver.Chrome(CHROME_DRIVER_PATH)
            driver.get(WEB_PAGE)
            time.sleep(2)
            element = driver.find_element_by_xpath("//input[@id='checkBoxOption3' and @value='option3']")
            element.click()
            if element.is_selected():
                self.assertTrue(True)
            else:
                self.assertTrue(False)
        except:
            self.assertTrue(False)
        time.sleep(1)
        driver.quit()


class NameAlert(unittest.TestCase):
    def test_AlertBox(self):
        try:
            driver = webdriver.Chrome(CHROME_DRIVER_PATH)
            driver.get(WEB_PAGE)
            element = driver.find_element_by_xpath("//input[@id='name' and @name='enter-name']")
            element.send_keys("Adrian")
            alertBtn = driver.find_element_by_xpath("//input[@id='alertbtn' and @value='Alert']")
            alertBtn.click()
            alert = driver.switch_to.alert
            alert.accept()
            self.assertTrue(True)
        except:
            self.assertTrue(False)
        driver.quit()

    def test_ConfirmBox_Ok(self):
        try:
            driver = webdriver.Chrome(CHROME_DRIVER_PATH)
            driver.get(WEB_PAGE)
            element = driver.find_element_by_xpath("//input[@id='name' and @name='enter-name']")
            element.send_keys("Adrian")
            alertBtn = driver.find_element_by_xpath("//input[@id='confirmbtn' and @value='Confirm']")
            alertBtn.click()
            alert = driver.switch_to.alert
            alert.accept()
            self.assertTrue(True)
        except:
            self.assertTrue(False)
        driver.quit()

    def test_ConfirmBox_Dismiss(self):
        try:
            driver = webdriver.Chrome(CHROME_DRIVER_PATH)
            driver.get(WEB_PAGE)
            element = driver.find_element_by_xpath("//input[@id='name' and @name='enter-name']")
            element.send_keys("Adrian")
            alertBtn = driver.find_element_by_xpath("//input[@id='confirmbtn' and @value='Confirm']")
            alertBtn.click()
            alert = driver.switch_to.alert
            alert.dismiss()
            self.assertTrue(True)
        except:
            self.assertTrue(False)
        driver.quit()

    def test_ConfirmBox_Text(self):
        string = "Hello Adrian, Are you sure you want to confirm?"
        try:
            driver = webdriver.Chrome(CHROME_DRIVER_PATH)
            driver.get(WEB_PAGE)
            element = driver.find_element_by_xpath("//input[@id='name' and @name='enter-name']")
            element.send_keys("Adrian")
            confirmBtn = driver.find_element_by_xpath("//input[@id='confirmbtn' and @value='Confirm']")
            confirmBtn.click()
            alert = driver.switch_to.alert
            if str(alert.text) == string:
                alert.dismiss()
                self.assertTrue(True)
            else:
                self.assertTrue(False)
        except:
            self.assertTrue(False)
        driver.quit()

if __name__ == '__main__':
    unittest.main()
