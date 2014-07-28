import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, ElementNotVisibleException, UnexpectedAlertPresentException

#executeable_path = 'C:\Program Files (x86)\phantomjs-1.9.7-windows\phantomjs'
chromedriver_path = 'C:\Users\LasertagDesk\chromedriver'
os.environ["webdriver.chrome.driver"] = chromedriver_path
driver = webdriver.Chrome(chromedriver_path) 
wait = WebDriverWait(driver, 10) 

driver.get("http://192.168.10.103/lasertag/login.php?ref=/lasertag/lt_game/game_main.php")


assert "LOGIN" in driver.title
elem = driver.find_element_by_name("password")
elem.send_keys("play")
elem.send_keys(Keys.RETURN)

driver.implicitly_wait(5)

ready_button = driver.find_element_by_id("readybutton")
start_button = driver.find_element_by_id("startbutton")
save_button = driver.find_element_by_id("savebutton")
print_button = driver.find_element_by_id("printbutton")
receive_button = driver.find_element_by_id("receivebutton")
abort_button = driver.find_element_by_id("abortbutton")
