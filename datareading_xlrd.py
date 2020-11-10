import xlrd

path = r"C:\Users\LENOVO\PycharmProjects\Python_Selenium_FW1\Data\TestData.xlsx"
excel_workbook = xlrd.open_workbook(path)
excel_worksheet = excel_workbook.sheet_by_name("Login")
print(excel_worksheet.cell_value(1, 3))  # (y,x)
# excel_worksheet = excel_workbook.sheet_by_index(0)
# excel_worksheet2 = excel_workbook.sheet_by_index(1)
# excel_worksheet3 = excel_workbook.sheet_by_index(2)

# read the data from the worksheet
print("your worksheet has " + str(excel_worksheet.nrows) + " rows")
print("your worksheet has " + str(excel_worksheet.ncols) + " columns")

for row in range(excel_worksheet.nrows):
    for col in range(excel_worksheet.ncols):
        print(excel_worksheet.cell_value(row, col), end="")
        print("\t", end="")
    print()


