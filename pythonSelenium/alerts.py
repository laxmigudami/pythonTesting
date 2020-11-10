from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path=r"C:\Users\LENOVO\PycharmProjects\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(5)
validateText = "Option3"
driver.find_element_by_css_selector('#name').send_keys(validateText)
driver.find_element_by_id("alertbtn").click()
alert = driver.switch_to.alert
alertText = alert.text
assert validateText in alertText

alert.accept()  # to click on ok button it means for positive scenarios
# alert.dismiss() for negative scenarios i.e to cancel the alert
driver.close()
