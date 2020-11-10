from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Users\LENOVO\PycharmProjects\chromedriver.exe")
driver.get(r'https://the-internet.herokuapp.com/iframe')
driver.implicitly_wait(5)
# if its a frame it will be having tag name as iframe, frameset, frame
# we can handle frames by either entering the frame id, frame name or index value
driver.switch_to.frame('mce_0_ifr')
driver.find_element_by_css_selector("#tinymce").clear()
driver.find_element_by_css_selector("#tinymce").send_keys("i can handle this frame")






























































































driver.switch_to.default_content()  # with the help of this we can switch back to the original frame
assert driver.find_element_by_xpath("//h3").text == "An iFrame containing the TinyMCE WYSIWYG Editor"
print("windows handled successfully")
driver.close()
dieeeeeeeeeeeeeeeeeeeeee



















eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee