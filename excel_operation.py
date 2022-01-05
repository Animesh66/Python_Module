import openpyxl as xl

wb = xl.load_workbook("transactions.xlsx")
sheet = wb["Sheet1"]
cell = sheet.cell(row=1, column=1)
print(cell.value)