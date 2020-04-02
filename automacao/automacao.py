from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC


#driver.maximize_window()
driver =  webdriver.Chrome('C://ProjetoAtech//Atech/automacao//drivers//chromedriver_win32//chromedriver.exe')  

driver.get("https://atech-airlines-ui-staging.herokuapp.com/")  

try:

    #Consulta Somente Origem
    element = WebDriverWait(driver, 1000).until(
    EC.visibility_of_element_located((By.XPATH, "/html/body/div/div[2]/div[1]/div[5]/button")))
    time.sleep(2)
    
    driver.find_element(By.NAME, "grupo").click()
    dropdown = driver.find_element(By.NAME, "grupo")
    dropdown.find_element(By.XPATH, "//option[. = 'São José dos Campos']").click()
    driver.find_element(By.CSS_SELECTOR, ".ng-dirty > option:nth-child(2)").click()
    driver.find_element(By.CSS_SELECTOR, ".btn").click()
    time.sleep(2)
    driver.save_screenshot('C://ProjetoAtech//Atech//automacao//evidencias//evidencia_origem_SJC.png')

    driver.find_element(By.NAME, "grupo").click()
    dropdown = driver.find_element(By.NAME, "grupo")
    dropdown.find_element(By.XPATH, "//option[. = 'Guarulhos']").click()
    driver.find_element(By.CSS_SELECTOR, ".ng-dirty > option:nth-child(3)").click()
    driver.find_element(By.CSS_SELECTOR, ".btn").click()
    time.sleep(2)
    driver.save_screenshot('C://ProjetoAtech//Atech//automacao//evidencias//evidencia_origem_GR.png')


    driver.find_element(By.NAME, "grupo").click()
    dropdown = driver.find_element(By.NAME, "grupo")
    dropdown.find_element(By.XPATH, "//option[. = 'Nova Iorque']").click()
    driver.find_element(By.CSS_SELECTOR, ".ng-dirty > option:nth-child(4)").click()
    driver.find_element(By.CSS_SELECTOR, ".btn").click()
    time.sleep(2)
    driver.save_screenshot('C://ProjetoAtech//Atech//automacao//evidencias//evidencia_origem_NY.png')

    driver.find_element(By.NAME, "grupo").click()
    dropdown = driver.find_element(By.NAME, "grupo")
    dropdown.find_element(By.XPATH, "//option[. = 'Tóquio']").click()
    driver.find_element(By.CSS_SELECTOR, ".ng-dirty > option:nth-child(5)").click()
    driver.find_element(By.CSS_SELECTOR, ".btn").click()
    time.sleep(2)
    driver.save_screenshot('C://ProjetoAtech//Atech//automacao//evidencias//evidencia_origem_TOQUIO.png')


finally:
    driver.quit()


