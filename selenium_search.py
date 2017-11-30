from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# driver = webdriver.Chrome(executable_path='C:\Users\User\Downloads\chromedriver_win32_2.0\chromedriver.exe')
url = 'https://www.olx.ua/obyavlenie/termousadka-dlya-akkumulyatorov-18650-IDtBbIG.html#9f4b3a5428'
# driver = webdriver.Chrome()
driver = webdriver.Firefox()
driver.get(url)
# assert "olx" in driver.title

action = webdriver.common.action_chains.ActionChains(driver)
time.sleep(10)
element = driver.find_element_by_class_name('spoiler')
# element = driver.find_element_by_id('contact_methods')
print(element.location)
print(element.size)
# loc_x = element.location['x'] + int(element.size['width']/2)
# loc_y = element.location['y'] + int(element.size['height']/1.3)
loc_x = element.location['x']
loc_y = element.location['y']
action.move_by_offset(loc_x, loc_y).perform()
time.sleep(5)
action.click().perform()
time.sleep(10)

driver.close()
