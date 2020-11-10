from selenium import webdriver
driver=webdriver.Chrome(executable_path=r"C:\Users\LENOVO\PycharmProjects\chromedriver.exe")
driver.get(r"https://login.salesforce.com/")
driver.maximize_window()
driver.implicitly_wait(5)
print(driver.find_element_by_css_selector('form[name="login"] label:nth-child(4)').text)
# x path --->(//label[@class="label"])[1]
#