from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Users\LENOVO\PycharmProjects\chromedriver.exe")
driver.get('https://rahulshettyacademy.com/dropdownsPractise/')
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element_by_xpath('//input[@id="autosuggest"]').send_keys('ind')
countries = driver.find_elements_by_css_selector('li[class="ui-menu-item"] a')
print(len(countries))
for country in countries:
    if country.text == 'India':
        country.click()
        break

assert driver.find_element_by_xpath('//input[@id="autosuggest"]').get_attribute('value') == 'India'
