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

class TestNewAccountSameCredentials():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_new_account_same_credentials(self):
    # Test name: new_account
    # Step # | name | target | value
    # 1 | open | /en/login?back=my-account | 
    self.driver.get("http://34.118.122.203/en/login?back=my-account")
    # 2 | setWindowSize | 1360x816 | 
    self.driver.set_window_size(1360, 816)
    # 3 | click | linkText=No account? Create one here | 
    self.driver.find_element(By.LINK_TEXT, "No account? Create one here").click()
    # 4 | click | id=field-id_gender-1 | 
    self.driver.find_element(By.ID, "field-id_gender-1").click()
    # 5 | click | id=field-firstname | 
    self.driver.find_element(By.ID, "field-firstname").click()
    # 6 | type | id=field-firstname | Bichis
    self.driver.find_element(By.ID, "field-firstname").send_keys("Bichis")
    # 7 | type | id=field-lastname | Claudiu
    self.driver.find_element(By.ID, "field-lastname").send_keys("Claudiu")
    # 8 | type | id=field-email | claudiu_bikis@yahoo.com
    self.driver.find_element(By.ID, "field-email").send_keys("claudiu_bikis@yahoo.com")
    # 9 | click | id=field-password | 
    self.driver.find_element(By.ID, "field-password").click()
    # 10 | type | id=field-password | 123456789
    self.driver.find_element(By.ID, "field-password").send_keys("123456789")
    # 11 | click | css=.form-group:nth-child(6) > .col-md-6 > .form-control-comment | 
    self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(6) > .col-md-6 > .form-control-comment").click()
    # 12 | click | id=field-birthday | 
    self.driver.find_element(By.ID, "field-birthday").click()
    # 13 | type | id=field-birthday | 11/14/1988
    self.driver.find_element(By.ID, "field-birthday").send_keys("11/14/1988")
    # 14 | click | name=customer_privacy | 
    self.driver.find_element(By.NAME, "customer_privacy").click()
    # 15 | click | css=.form-control-submit | 
    self.driver.find_element(By.CSS_SELECTOR, ".form-control-submit").click()
    time.sleep(4)
  
