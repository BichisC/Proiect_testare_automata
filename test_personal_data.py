# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestPersonalData():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_personal_data(self):
    # Test name: personal_data2
    # Step # | name | target | value
    # 1 | open | /en/login?back=my-account | 
    self.driver.get("http://34.118.122.203/en/login?back=my-account")
    # 2 | setWindowSize | 1360x816 | 
    self.driver.set_window_size(1360, 816)
    # 3 | click | id=field-email | 
    self.driver.find_element(By.ID, "field-email").click()
    # 4 | type | id=field-email | claudiu_bikis@yahoo.com
    self.driver.find_element(By.ID, "field-email").send_keys("claudiu_bikis@yahoo.com")
    # 5 | click | id=field-password | 
    self.driver.find_element(By.ID, "field-password").click()
    # 6 | type | id=field-password | 1234567890
    self.driver.find_element(By.ID, "field-password").send_keys("1234567890")
    # 7 | click | id=submit-login | 
    self.driver.find_element(By.ID, "submit-login").click()
    # 8 | click | css=#addresses-link .material-icons | 
    self.driver.find_element(By.CSS_SELECTOR, " #addresses-link .material-icons").click()
    # 9 | click | css=.addresses-footer span | 
    self.driver.find_element(By.CSS_SELECTOR, ".addresses-footer span").click()
    # 10 | click | id=field-alias | 
    self.driver.find_element(By.ID, "field-alias").click()
    # 11 | type | id=field-alias | ClaudiuB
    self.driver.find_element(By.ID, "field-alias").send_keys("ClaudiuB")
    # 12 | click | id=field-address1 | 
    self.driver.find_element(By.ID, "field-address1").click()
    # 13 | type | id=field-address1 | Strada Mare
    self.driver.find_element(By.ID, "field-address1").send_keys("Strada Mare")
    # 14 | click | id=field-postcode | 
    self.driver.find_element(By.ID, "field-postcode").click()
    # 15 | type | id=field-postcode | 407280
    self.driver.find_element(By.ID, "field-postcode").send_keys("407280")
    # 16 | type | id=field-address2 | 43E
    self.driver.find_element(By.ID, "field-address2").send_keys("43E")
    # 17 | type | id=field-city | Florești - Cluj
    self.driver.find_element(By.ID, "field-city").send_keys("Florești - Cluj")
    # 18 | type | id=field-phone | +10755568730
    # self.driver.find_element(By.ID, "field-phone").send_keys("+10755568730")()
    # 19 | click | id=field-phone | 
    self.driver.find_element(By.ID, "field-phone").click()
    # 20 | type | id=field-phone | 1236589723
    self.driver.find_element(By.ID, "field-phone").send_keys("1236589723")
    # 21 | click | css=.form-control-submit | 
    self.driver.find_element(By.CSS_SELECTOR, ".form-control-submit").click()
    time.sleep(5)
    assert 'Address successfully added!' in self.driver.page_source
  