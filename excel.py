import openpyxl
import datetime

x = raw_input("in date/month/year")
y = raw_input("out data/month/year")
try:
    from_date = datetime.datetime.strptime(x, "%d/%m/%y").date()
    isValid = True
except:
    print "try again"
try:
    to_date = datetime.datetime.strptime(y, "%d/%m/%y").date()
    isValid = True
except:
    print "try again"

path1 = "/home/datalake/tejesh/current.xlsx"
path2 = "/home/datalake/Desktop/new.xlsx"

excel1 = openpyxl.load_workbook(path1)
old_sheet = excel1.get_sheet_by_name("Sheet1") #if we have multiple sheets specify the sheet name from where to be copied

excel2 = openpyxl.load_workbook(path2)
new_sheet = excel2.get_sheet_by_name("Sheet1")

for row in old_sheet:
    for cell in row:
        print cell.internal_value
        new_sheet[cell.coordinate].value = cell.value
excel2.save(path2)
