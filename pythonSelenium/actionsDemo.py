from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path=r"C:\Users\LENOVO\PycharmProjects\chromedriver.exe")
driver.get(r'https://www.familysearch.org/en/')
driver.maximize_window()
driver.implicitly_wait(10)
action = ActionChains(driver)
# for multiple chain of actions we can use builds()
familyTree = driver.find_element_by_xpath('(//button[text()="Family Tree"])[1]')
person = driver.find_element_by_xpath('//li[@class="submenu-item "]/a[text()="Person"]')
action.move_to_element(familyTree).click().move_to_element(person).click().perform()

