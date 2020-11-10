from selenium import webdriver
driver = webdriver.Chrome(executable_path=r"C:\Users\LENOVO\PycharmProjects\pythonTesting\drivers\chromedriver.exe")


driver.get('http://demowebshop.tricentis.com/')
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element_by_class_name('search-box-text.ui-autocomplete-input').send_keys('Computer')
driver.find_element_by_class_name('button-1.search-box-button').click()