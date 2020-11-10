
# there are 3 ways we can pass the driver control from to frame
# 1. string(ID/Name attribute)
# int /index
# web element (address)

driver.switch_to.frame('frame_name')
driver.switch_to.frame(1)
driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[0])


# in order to switch back from frame to main page
driver.switch_to.default_content() #it is used to switch to main page directly
driver.switch_to.parent_frame() #it is used to switch to its immediate patent page
# index of the frame page starts at 0

# whenever switch_to.frame method fails to locate perticular object on the frame it raises NoSuchFrameException
# when the frame page get refresh, control will automatically go back to the main page


