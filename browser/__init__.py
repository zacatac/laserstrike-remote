from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://192.168.10.103/lasertag/lt_game/game_main.php")

assert "LOGIN" in driver.title
elem = driver.find_element_by_name("password")
elem.send_keys("play")
elem.send_keys(Keys.RETURN)

ready_button = driver.find_element_by_id("readybutton")
start_button = driver.find_element_by_id("startbutton")
save_button = driver.find_element_by_id("savebutton")
print_button = driver.find_element_by_id("printbutton")
receive_button = driver.find_element_by_id("receivebutton")
