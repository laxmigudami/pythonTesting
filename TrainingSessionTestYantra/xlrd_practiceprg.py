# import xlrd
# wb =xlrd.open_workbook(path)
# ws = wb.sheet_by_name("stocks")
# rows = ws.get_rows()
# #it returns the generator object, if we feed it to the for loop we get all the details in the form of list. each row we get in each list.
# # each row is being reprsented by the list
# for row in rows:
#     print(row)
#     print(row[0], row[1], row[3]) #indexing is for the coloumn
#     print(type(row[0])) #type cell
#     print(row[0].value) #gives string we have to use .value method
# headers = next(rows) #we can skip to the next
# # portfolio = []
# # # for row in rows:
# # #     portfolio.append({row[0].value: (row[1].value, )})
#
# portfolio = {row[0].value : (row[1].value, row[2].value) for row in rows}
# # to read entire content from the excel file to inside python data structure
# # we can directly access it
# print(portfolio['TCS']) #It will give me details about tcs

import xlrd
wb = xlrd.open_workbook('TestData.xlsx')
ws = wb.sheet_by_name('Covid')
print(ws)
rows = ws.get_rows()
# print(rows)

# for row in rows:
#     print(row)


# to get actual value of the cell in the string format
#
# for row in rows:
#     print(row[0].value, row[1].value, row[2].value)

# since rows is a generator object you can feed that object to next() function
headers = next(rows)
print(headers[0].value, headers[1].value)



def read_locators(sheetname):
    workbook = xlrd.open_workbook("Objects.xlsx")
    worksheet = workbook.sheet_by_name(sheetname)
    rows = worksheet.get_rows()
    headers = next(rows)
    return {item[0].value: (item[1].value, item[2].value) for row in rows}

objects = read_locators('LoginPage')

print(objects)

{'txt_email': ('name', 'Email'), 'txt_password': ('name', 'Password'), 'btn_login': ('xpath', "//input[@value='Log in']")}










