from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path=r"C:\Users\LENOVO\PycharmProjects\chromedriver.exe")
driver.get(r"https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element_by_xpath("//div[@class='form-group']//input[@name='name']").send_keys("laxmi")
driver.find_element_by_xpath('//input[@class="form-control ng-untouched ng-pristine ng-invalid"]').send_keys(
    'gudamilaxmi444@gmail.com')
driver.find_element_by_xpath('//input[@id="exampleCheck1"]').click()
obj = driver.find_element_by_xpath('//select[@id="exampleFormControlSelect1"]')
S = Select(obj)
S.select_by_visible_text('Female')
driver.find_element_by_xpath('//input[@id="inlineRadio1"]').click()
# driver.find_element_by_xpath('(//input[@class="form-control"])[2]').click()
driver.find_element_by_xpath('//input[@value="Submit"]').click()
driver.close()
