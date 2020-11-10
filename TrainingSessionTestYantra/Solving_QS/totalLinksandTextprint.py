links = driver.find_elements_by_xpath("//a")
print("total number of links", len(links))
for link in links:
    print(link.text)
