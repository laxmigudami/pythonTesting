from selenium import webdriver
driver = webdriver.Chrome(executable_path=r"C:\Users\LENOVO\PycharmProjects\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.maximize_window()
driver.implicitly_wait(10)
Cookies = driver.get_cookies()
print(len(Cookies))
print(Cookies)
