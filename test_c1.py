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

class TestC1():
  url ="https://atech-airlines-ui-staging.herokuapp.com/"
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  

#  def teardown_method(self, method):
#   self.driver.quit()
  
  def test_c1(url):
    self.driver.get(url)
    self.driver.set_window_size(1550, 838)
    self.driver.find_element(By.NAME, "grupo").click()
    dropdown = self.driver.find_element(By.NAME, "grupo")
    dropdown.find_element(By.XPATH, "//option[. = 'São José dos Campos']").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ng-dirty > option:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
  
  test_c1(url)

	  	

