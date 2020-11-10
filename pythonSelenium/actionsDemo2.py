from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path=r"C:\Users\LENOVO\PycharmProjects\chromedriver.exe")
driver.get(r'https://chercher.tech/practice/practice-pop-ups-selenium-webdriver')
driver.maximize_window()
driver.implicitly_wait(10)
action = ActionChains(driver)
element = driver.find_element_by_xpath('//input[@id="double-click"]')
action.double_click(element).perform()
alert = driver.switch_to.alert

assert "You double clicked me!!!, You got to be kidding me" == alert.text
alert.accept()
driver.close()
# actionchains in python sel are highly unstable
# lly context_click() is used for right click. but usually it is not that much useful. used very rarely




