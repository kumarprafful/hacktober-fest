from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from selenium import webdriver
 
chrome_path="A:/Programs/Python/Python 2.7/selenium/chromedriver"
 
driver=webdriver.Chrome(chrome_path)
 
driver.maximize_window()
