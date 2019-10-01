import openpyxl
import datetime

path1 = "/home/datalake/tejesh/current.xlsx"

excel1 = openpyxl.load_workbook(path1)
old_sheet = excel1.get_sheet_by_name("Sheet1")

