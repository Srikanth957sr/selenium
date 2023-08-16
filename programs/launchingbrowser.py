from selenium.webdriver import Chrome

# driver = Chrome("../drivers/chromedriver.exe")
driver = Chrome(executable_path=r"C:\Users\new soft\PycharmProjects\selenium\drivers\chromedriver.exe")
driver.maximize_window()
driver.minimize_window()
driver.get("https://www.youtube.com/")
print(driver.title)
print(driver.current_url)
snd = driver.find_element("id","container")
snd.send_keys("jailer")
# pwd = driver.find_element("id","search-icon-legacy")

# print(driver.page_source)
'''
 ctrl + shift + i
 f12  ===> to inspect
'''