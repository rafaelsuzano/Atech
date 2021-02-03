# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import pytest
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
import unittest





driver =  webdriver.Chrome('//opt/DriverChrome//chromedriver.exe') 

driver.maximize_window()
driver.get("https://atech-airlines-ui-staging.herokuapp.com/") 
class FP(unittest.TestCase):
    #def setUp(self):

       
     
     


    def test_CT_01(self):
            
            print("Esse cenario contempla filtro Partida")
            element = WebDriverWait(driver, 1000).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div/div[2]/div[1]/div[5]/button")))
            time.sleep(2)
            
            #Consulta Somente Origem
            driver.find_element(By.NAME, "grupo").click()
            dropdown = driver.find_element(By.NAME, "grupo")
            dropdown.find_element(By.XPATH, "//option[. = 'São José dos Campos']").click()
            driver.find_element(By.CSS_SELECTOR, ".ng-dirty > option:nth-child(2)").click()
            driver.find_element(By.CSS_SELECTOR, ".btn").click()
            time.sleep(2)
            driver.save_screenshot('C://ProjetoAtech//Atech//automacao//evidencias//evidencia_origem_SJC.png')
              
    def test_CT_02(self):
         
          
            print("Esse cenario contempla filtro Partida/Chegada")
            element = WebDriverWait(driver, 1000).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div/div[2]/div[1]/div[5]/button")))
            time.sleep(2)
            
            #Consulta data Partida Chegada
            driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div[1]/div/div/md-datepicker/div[1]/input").send_keys("4/01/2018")
            time.sleep(2)
            driver.find_element(By.XPATH,"/html/body/div/div[2]/div[1]/div[2]/div/div/md-datepicker/div[1]/input").send_keys("4/02/2018")
            time.sleep(2)
            driver.find_element(By.CSS_SELECTOR, ".btn").click()
            time.sleep(2)
            driver.find_element(By.NAME, "grupo").click()
            dropdown = driver.find_element(By.NAME, "grupo")
            dropdown.find_element(By.XPATH, "//option[. = 'São José dos Campos']").click()
            driver.find_element(By.CSS_SELECTOR, ".ng-dirty > option:nth-child(2)").click()
            driver.find_element(By.CSS_SELECTOR, ".btn").click()
            driver.save_screenshot('C://ProjetoAtech//Atech//automacao//evidencias//evidencia_Partida_Chegada.png')
            time.sleep(2)
       
    #@unittest.skip("Em desenvolvimento")
    def test_CT_03(self):
        d1 = "4/05/2018"
        d2  = "04/04/2018"
        driver.refresh()
        
        element = WebDriverWait(driver, 1000).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div[2]/div[1]/div[5]/button")))
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div[1]/div/div/md-datepicker/div[1]/input").send_keys(d1)
        
        
        time.sleep(2)
        driver.find_element(By.XPATH,"/html/body/div/div[2]/div[1]/div[2]/div/div/md-datepicker/div[1]/input").send_keys(d2)
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, ".btn").click()
        self.assertEqual(d1<d2,"Data de chegada menor que data de Partida")

