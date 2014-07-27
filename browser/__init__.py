from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# chromedriver_path = '/Users/zrfield/laserstrike/chromedriver'
driver = webdriver.PhantomJS() 
driver.get("http://192.168.10.103/lasertag/lt_game/game_main.php")

wait = WebDriverWait(driver, 10) 

assert "LOGIN" in driver.title
elem = driver.find_element_by_name("password")
elem.send_keys("play")
elem.send_keys(Keys.RETURN)

ready_button = driver.find_element_by_id("readybutton")
start_button = driver.find_element_by_id("startbutton")
save_button = driver.find_element_by_id("savebutton")
print_button = driver.find_element_by_id("printbutton")
receive_button = driver.find_element_by_id("receivebutton")
abort_button = driver.find_element_by_id("abortbutton")

