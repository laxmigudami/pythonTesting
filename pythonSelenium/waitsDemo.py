from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(executable_path=r"C:\Users\LENOVO\PycharmProjects\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.maximize_window()
# driver.implicitly_wait(5)
driver.find_element_by_xpath('//input[@placeholder="Search for Vegetables and Fruits"]').send_keys('ber')
count = len(driver.find_elements_by_xpath('//div[@class="product"]'))
assert count == 3

driver.find_element_by_xpath('(//div[@class="products"]/div/div/button)[1]').click()
driver.find_element_by_xpath('(//div[@class="products"]/div/div/button)[2]').click()
driver.find_element_by_xpath('(//div[@class="products"]/div/div/button)[3]').click()

# time.sleep(2)
# for button in buttons:

#     button.click()
#     time.sleep(2)
driver.find_element_by_xpath('//img[@alt="Cart"]').click()
driver.find_element_by_xpath('//button[text()="PROCEED TO CHECKOUT"]').click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, '//input[@class="promoCode"]')))
driver.find_element_by_xpath('//input[@class="promoCode"]').send_keys('rahulshettyacademy')
driver.find_element_by_xpath('//button[text()="Apply"]').click()
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "span.promoInfo")))
print(driver.find_element_by_css_selector("span.promoInfo").text)
driver.close()
