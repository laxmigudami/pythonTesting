from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r"C:\Users\LENOVO\PycharmProjects\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element_by_xpath('//a[text()="Shop"]').click()
products = driver.find_elements_by_xpath('//div[@class="card h-100"]')
# //div[@class="card h-100"]/div/h4/a
for product in products:
    productName = product.find_element_by_xpath("div/h4/a").text
    if productName == "Blackberry":
        product.find_element_by_xpath("div[2]/button").click()
        # add item to the cart #//div[@class="card h-100"]/div[2]/button
driver.find_element_by_css_selector('a[class="nav-link btn btn-primary"]').click()
driver.find_element_by_xpath('//button[@class="btn btn-success"]').click()
driver.find_element_by_css_selector("#country").send_keys("ind")
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element_by_link_text("India").click()
driver.find_element_by_xpath(r'//div[@class="checkbox checkbox-primary"]').click()
driver.find_element_by_css_selector('input[class*="success "]').click()
print(driver.find_element_by_xpath('//div[@class="alert alert-success alert-dismissible"]').text)
successMsg = driver.find_element_by_xpath('//div[@class="alert alert-success alert-dismissible"]').text
assert "Success! Thank you!" in successMsg
driver.get_screenshot_as_file("screen.png")

print("text is successful")
driver.close()
