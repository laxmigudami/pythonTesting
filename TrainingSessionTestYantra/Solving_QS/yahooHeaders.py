from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path=r"C:\Users\LENOVO\PycharmProjects\pythonTesting\drivers\chromedriver.exe")
driver.get("http://www.yahoo.com")

links = driver.find_elements_by_xpath("//ul[@id='header-nav-bar']//a")
for link in links:
  text = link.text
  url = link.get_attribute("href")
  # print(f'{text:<20} {url:<40}')
  print(text,"    ", url)