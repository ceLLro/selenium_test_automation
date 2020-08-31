from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

CHROME_DRIVER_PATH = "C:\Program Files\chromedriver.exe"
WEB_PAGE = "https://rahulshettyacademy.com/AutomationPractice/"


class RadioButtons(unittest.TestCase):
    def test_RadioButton_1(self):
        try:
            driver = webdriver.Chrome(CHROME_DRIVER_PATH)
            driver.get(WEB_PAGE)
            element = driver.find_element_by_xpath("//input[@name='radioButton' and @value='radio1']")
            element.click()
            if element.is_selected():
                self.assertTrue(True)
            else:
                self.assertTrue(False)
        except:
            self.assertTrue(False)
        driver.quit()

    def test_RadioButton_2(self):
        try:
            driver = webdriver.Chrome(CHROME_DRIVER_PATH)
            driver.get(WEB_PAGE)
            element = driver.find_element_by_xpath("//input[@name='radioButton' and @value='radio2']")
            element.click()
            if element.is_selected():
                self.assertTrue(True)
            else:
                self.assertTrue(False)
        except:
            self.assertTrue(False)
        driver.quit()

    def test_RadioButton_3(self):
        try:
            driver = webdriver.Chrome(CHROME_DRIVER_PATH)
            driver.get(WEB_PAGE)
            element = driver.find_element_by_xpath("//input[@name='radioButton' and @value='radio3']")
            element.click()
            if element.is_selected():
                self.assertTrue(True)
            else:
                self.assertTrue(False)
        except:
            self.assertTrue(False)
        driver.quit()


class CheckBoxes(unittest.TestCase):
    def test_CheckBox_1(self):
        try:
            driver = webdriver.Chrome(CHROME_DRIVER_PATH)
            driver.get(WEB_PAGE)
            element = driver.find_element_by_xpath("//input[@id='checkBoxOption1' and @value='option1']")
            element.click()
            if element.is_selected():
                self.assertTrue(True)
            else:
                self.assertTrue(False)
        except:
            self.assertTrue(False)
        driver.quit()

    def test_CheckBox_2(self):
        try:
            driver = webdriver.Chrome(CHROME_DRIVER_PATH)
            driver.get(WEB_PAGE)
            element = driver.find_element_by_xpath("//input[@id='checkBoxOption2' and @value='option2']")
            element.click()
            if element.is_selected():
                self.assertTrue(True)
            else:
                self.assertTrue(False)
        except:
            self.assertTrue(False)
        driver.quit()

    def test_CheckBox_3(self):
        try:
            driver = webdriver.Chrome(CHROME_DRIVER_PATH)
            driver.get(WEB_PAGE)
            element = driver.find_element_by_xpath("//input[@id='checkBoxOption3' and @value='option3']")
            element.click()
            if element.is_selected():
                self.assertTrue(True)
            else:
                self.assertTrue(False)
        except:
            self.assertTrue(False)
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


class DropDown(unittest.TestCase):
    def test_Dropdown_select_option1(self):
        try:
            driver = webdriver.Chrome(CHROME_DRIVER_PATH)
            driver.get(WEB_PAGE)
            element = driver.find_element_by_xpath("//option[@value='option1']").click()
            self.assertTrue(True)
        except:
            self.assertTrue(False)
        driver.quit()

    def test_Dropdown_select_option2(self):
        try:
            driver = webdriver.Chrome(CHROME_DRIVER_PATH)
            driver.get(WEB_PAGE)
            element = driver.find_element_by_xpath("//option[@value='option2']").click()
            self.assertTrue(True)
        except:
            self.assertTrue(False)
        driver.quit()

    def test_Dropdown_select_option3(self):
        try:
            driver = webdriver.Chrome(CHROME_DRIVER_PATH)
            driver.get(WEB_PAGE)
            element = driver.find_element_by_xpath("//option[@value='option3']").click()
            self.assertTrue(True)
        except:
            self.assertTrue(False)
        driver.quit()


class Window(unittest.TestCase):
    def test_Switch_Window(self):
        try:
            driver = webdriver.Chrome(CHROME_DRIVER_PATH)
            driver.get(WEB_PAGE)
            window_before = driver.window_handles[0]
            element = driver.find_element_by_id(('openwindow')).click()
            window_after = driver.window_handles[1]
            driver.switch_to.window(window_after)
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_Switch_Tab(self):
        try:
            driver = webdriver.Chrome(CHROME_DRIVER_PATH)
            driver.get(WEB_PAGE)
            window_before = driver.window_handles[0]
            element = driver.find_element_by_id(('opentab')).click()
            window_after = driver.window_handles[1]
            driver.switch_to.window(window_after)
            self.assertTrue(True)
        except:
            self.assertTrue(False)


class ElementDisplay(unittest.TestCase):
    def test_Hide_Button(self):
        try:
            driver = webdriver.Chrome(CHROME_DRIVER_PATH)
            driver.get(WEB_PAGE)
            element = driver.find_element_by_id(('show-textbox')).click()
            valid = driver.find_element_by_id('displayed-text')
            if valid:
                element = driver.find_element_by_id(('hide-textbox')).click()
                self.assertTrue(True)
            else:
                self.assertTrue(False)
        except:
            self.assertTrue(False)

    def test_Show_Button(self):
        try:
            driver = webdriver.Chrome(CHROME_DRIVER_PATH)
            driver.get(WEB_PAGE)
            element = driver.find_element_by_id(('hide-textbox')).click()
            element = driver.find_element_by_id(('show-textbox')).click()
            valid = driver.find_element_by_id('displayed-text')
            if valid:
                self.assertTrue(True)
            else:
                self.assertTrue(False)
        except:
            self.assertTrue(False)


class MouseHover(unittest.TestCase):
    def test_Hover_Mouse(self):
        try:
            driver = webdriver.Chrome(CHROME_DRIVER_PATH)
            driver.get(WEB_PAGE)
            element = driver.find_element_by_id(('mousehover'))
            hover = ActionChains(driver).move_to_element(element)
            hover.perform()
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_iFrame(self):
        try:
            driver = webdriver.Chrome(CHROME_DRIVER_PATH)
            driver.get(WEB_PAGE)
            element = driver.find_element_by_id('courses-iframe')
            self.assertTrue(True)
        except:
            self.assertTrue(False)


class WebTable(unittest.TestCase):
    def test_Get_Table(self):
        try:
            driver = webdriver.Chrome(CHROME_DRIVER_PATH)
            driver.get(WEB_PAGE)
            element = driver.find_element_by_id('product')
            self.assertTrue(True)
        except:
            self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
