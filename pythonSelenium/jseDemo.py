# before selenium being invented they used to invent all html related objects using DOM document.
# DOM stands for documentary object model
# https://www.w3schools.com/js/js_htmldom_document.asp
# js DOM can access any element on web page like selenium does.
# sel have a mtd to execute js inside your python code
# how to access it??

from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Users\LENOVO\PycharmProjects\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element_by_name("name").send_keys("hello")
print(driver.find_element_by_name(
    "name").text)  # it will not return anything bcz we cannt get the entered value with the help of text
print(driver.find_element_by_name("name").get_attribute(
    "value"))  # it return the hello if any value attribute not present in the web page
# we can achieve this purely using js without using selenium

print(driver.execute_script('return document.getElementsByName("name")[0].value'))
# whenever it is not able to get the text from the webpage using selenium we can use document. using js and grab the text

shopButton = driver.find_element_by_css_selector('a[href*="shop"]')
driver.execute_script("arguments[0].click();", shopButton)

# how to scroll in selenium using js


driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# driver.execute_script("arguments[0].scrollIntoView();", element)
# driver.execute_script("window.scrollBy(0,500)", " ")
# driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
# driver.execute_script("arguments[0].scrollIntoView(true);", target)