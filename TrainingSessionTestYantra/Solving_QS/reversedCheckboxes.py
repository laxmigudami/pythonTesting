import time

from selenium import webdriver
driver = webdriver.Chrome(executable_path=)

driver.get(url)
driver.maximize_window()
elements = driver.find_elements_by_css_selector(locator)

for element in reversed(elements):
    element.click()
    time.sleep(2)

time.sleep(2)
driver.close()
