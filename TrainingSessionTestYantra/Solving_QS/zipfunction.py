# Write a script enter firstname and lastname in custom webpage (sample.html) using for loop.
from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path=r"C:\Users\LENOVO\PycharmProjects\pythonTesting\drivers\chromedriver.exe")
driver.get("http://www.yahoo.com")

elements = driver.find_elements_by_name("spam")
texts = ['Hello', 'World']

for element, text in zip(elements, texts):
    element.send_keys(text)
    time.sleep(1)