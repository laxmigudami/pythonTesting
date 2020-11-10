from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path=r"C:\Users\LENOVO\PycharmProjects\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(10)
checkboxes = driver.find_elements_by_xpath('//input[@type="checkbox"]')
print(len(checkboxes))
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
radioButtons = driver.find_elements_by_name("radioButton")

radioButtons[2].click()
assert radioButtons[2].is_selected()
assert driver.find_element_by_css_selector("#displayed-text").is_displayed()  # assert True
driver.find_element_by_css_selector("#hide-textbox").click()
assert not driver.find_element_by_css_selector("#displayed-text").is_displayed()  # assert not False

driver.close()
