#verify the search functinality in home page is working

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


driver=webdriver.Chrome(executable_path=r"C:\Users\LENOVO\PycharmProjects\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.maximize_window()
driver.implicitly_wait(10)

list = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
list2 = []
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(5)
names = driver.find_elements_by_xpath('//h4[@class="product-name"]')
print(len(names))
for name in names:
    list2.append(name.text)
    print(name.text)
assert list == list2
print("test is passed")
driver.close()
