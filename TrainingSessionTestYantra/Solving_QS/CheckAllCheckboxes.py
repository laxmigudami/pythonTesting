import time

from selenium import webdriver
driver = webdriver.Chrome(executable_path= r"C:\Users\LENOVO\PycharmProjects\pythonTesting\drivers\chromedriver.exe")

driver.get("file:///HTML_Pages/Tables.html")
driver.maximize_window()
checkBoxes = driver.find_elements_by_css_selector()

for checkBox in checkBoxes:
    checkBox.click()
    time.sleep(2)

driver.quit()

