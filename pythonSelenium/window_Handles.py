from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Users\LENOVO\PycharmProjects\chromedriver.exe")
driver.get(r'https://the-internet.herokuapp.com/windows')
driver.implicitly_wait(5)
driver.find_element_by_xpath("//a[text()='Click Here']").click()
childWindow = driver.window_handles[1]
driver.switch_to.window(childWindow)
print(driver.find_element_by_xpath("//h3").text)
driver.close()
parentWindow = driver.window_handles[0]
driver.switch_to.window(parentWindow)
Text = driver.find_element_by_xpath("//h3").text
assert Text == "Opening a new window"
driver.close()

