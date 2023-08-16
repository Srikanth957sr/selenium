from selenium.webdriver import Chrome
from time import sleep

driver = Chrome(executable_path="../drivers/chromedriver.exe")
driver.get("https://www.youtube.com/")
driver.find_element("css selector","input[id='search']").send_keys("jailer")
driver.find_element("id","search-icon-legacy").click()
