import time

from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--disable-notifications")
driver = webdriver.Chrome(executable_path=r"C:\Users\LENOVO\PycharmProjects\pythonTesting\drivers\chromedriver.exe", options=chromeOptions)
driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.find_element_by_xpath('//input[@id="email"]').send_keys("gudamilaxmi444@gmail.com")
driver.find_element_by_xpath('//input[@id="pass"]').send_keys('laxpoojdal ')
driver.find_element_by_xpath('//button[text()="Log In"]').click()
# driver.implicitly_wait(20)
title = driver.title
print(title)
# wait = WebDriverWait(driver, 30)
# wait.until(expected_conditions.alert_is_present())
# alert = driver.switch_to.alert()
# alert.dismiss()
driver.find_element_by_xpath('//input[@placeholder="Search Facebook"]').send_keys('Vinayak Kinekar')
time.sleep(3)
driver.find_element_by_xpath(r'//li[1]//a[contains(@href,"/search/top/?q=")]').click()
# driver.find_element_by_xpath('//input[@placeholder="Search Facebook"]').send_keys('Vinayak Kinekar')
# driver.find_element_by_xpath(r'//li[1]//a[contains(@href,"&__epa__=SEARCH_BOX&__eps__=SERP_TOP_TAB")]').click()
# # driver.find_element_by_xpath(r"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/ul[1]/li[1]/div[1]/a[1]/div[1]/div[2]/span[1]/span[1]").click()
# # names = driver.find_elements_by_xpath(r'//span[@class="a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7 ltmttdrg g0qnabr5"]')
# # for name in names:
# #     time.sleep(2)
# #     if name.text == "vinayak kinekar":
# #         print("its your friend page")
# #         name.click()


# driver.find_element_by_xpath(r'//span[text()="Vinayak Kinekar"]').click()
friendpage_title = driver.title
print(friendpage_title)
driver.find_element_by_xpath('//span[text()="About"]').click()
driver.find_element_by_xpath('//span[text()="Work and education"]').click()
first_studied = driver.find_element_by_xpath('//div[@class="ii04i59q a3bd9o3v jq4qci2q oo9gr5id tvmbv18p"]').text
print(first_studied)

driver.close()
