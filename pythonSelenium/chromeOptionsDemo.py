from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
# we can give the instructions to the chrome how it should behave or open like headless browser and maximized opening etc
# for free defined chrome options
# to ignore the certificate errors and go to my actual page
# use to customize and configure a ChromeDriver session
# more details -->https://www.programcreek.com/python/example/100025/selenium.webdriver.ChromeOptions
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(executable_path=r"C:\Users\LENOVO\PycharmProjects\chromedriver.exe", options=chrome_options)
driver.get(r'https://chercher.tech/practice/practice-pop-ups-selenium-webdriver')
print(driver.title)
