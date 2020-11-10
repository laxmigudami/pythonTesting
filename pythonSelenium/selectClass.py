# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# import time
# driver = webdriver.Chrome(executable_path=r"C:\Users\LENOVO\PycharmProjects\pythonTesting\drivers\chromedriver.exe")
# driver.maximize_window()
# driver.get('http://demowebshop.tricentis.com/books')
# time.sleep(2)
# lst_sort_by = driver.find_element_by_id("products-orderby")
# select = Select(lst_sort_by)
#
# # selecting item by visible text
# select.select_by_visible_text('Name: A to Z')
#
# time.sleep(2)
#
# # selecting item by index
# select.select_by_index(4)
#
#
# time.sleep(2)
# driver.quit()

# with the above code we will get the StaleElementReferenceException
# to handle that exception we ref below code

# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# from selenium.common.exceptions import StaleElementReferenceException
#
# import time
# driver = webdriver.Chrome(executable_path=r"C:\Users\LENOVO\PycharmProjects\pythonTesting\drivers\chromedriver.exe")
# driver.maximize_window()
# driver.get('http://demowebshop.tricentis.com/books')
# time.sleep(2)
# lst_sort_by = driver.find_element_by_id("products-orderby")
# select = Select(lst_sort_by)
#
# # selecting item by visible text
# select.select_by_visible_text('Name: A to Z')
#
# time.sleep(2)
# try:
#     # selecting item by index
#     select.select_by_index(4)
# except StaleElementReferenceException:
#     lst_sort_by = driver.find_element_by_id("products-orderby")
#     select = Select(lst_sort_by)
#     select.select_by_index(4)
#
#
#
# time.sleep(2)
# driver.quit()


# Selecting items in the listbox one-by-one using index.
from selenium import webdriver
from selenium.webdriver.support.select import Select


import time
driver = webdriver.Chrome(executable_path=r"C:\Users\LENOVO\PycharmProjects\pythonTesting\drivers\chromedriver.exe")
driver.maximize_window()
driver.get('http://demowebshop.tricentis.com/books')
time.sleep(2)
cars = driver.find_element_by_id("products-orderby")
select = Select(cars)
opts = select.options
for index, item in enumerate(opts):
    cars.select_by_index(1)
    time.sleep(1)




time.sleep(2)
driver.quit()