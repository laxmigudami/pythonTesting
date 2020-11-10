#Print the link text of all the links in python.org iff the linktext contains word 'Python' in it. Also, print the attribute 'href' of the corresponding link.
from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path=r"C:\Users\LENOVO\PycharmProjects\pythonTesting\drivers\chromedriver.exe")
driver.get("https://www.python.org/")
time.sleep(3)
links = driver.find_elements_by_xpath("//a")

for link in links:
    if 'Python' in link.text:
        print(link.text, end=',')
        print(link.get_attribute("href"))
time.sleep(2)
driver.quit()

