from selenium import webdriver
path = r'C:\Users\LENOVO\PycharmProjects\chromedriver.exe'
def headless():
    opt = webdriver.ChromeOptions()
    opt.headless = True
    driver = webdriver.Chrome(executable_path= path, options = opt)
    driver.get('https://rahulshettyacademy.com/seleniumPractise/')
    driver.find_element_by_css_selector('input[placeholder*="Search "]').send_keys("ber")
    print(driver.title)
    driver.close()
headless()