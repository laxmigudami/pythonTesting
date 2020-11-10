from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path=r"C:/chromedriver.exe")
driver.get("https://www.makemytrip.com/")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element_by_id("fromCity").click()

driver.find_element_by_css_selector('input[placeholder="From"]').send_keys("del")
cities = driver.find_elements_by_css_selector('p[class*="blackText"]')
print(len(cities))
for city in cities:
    if city.text == "Dubai, United Arab Emirates":
        city.click()
        break
driver.find_element_by_xpath("//p[text()='Mumbai, India']").click()
