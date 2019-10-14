import datetime
import pandas as pd

#takes the time input.
start_date = raw_input("Enter the Start date in date/month/year (eg: 23/11/2019 or 23/11/19) :")
end_date = raw_input("Enter the end date in data/month/year (eg: 28/11/2019 or 28/11/19) :")

#path1 is the location of Excel sheet from where we need to copy.
path1 = "/home/datalake/tejesh/current.xlsx"

#path2 is the location of excel sheet to which we need to copy
path2 = "/home/datalake/tejesh/new.xlsx"

try:
    start_date = datetime.datetime.strptime(start_date, "%d/%m/%y").date()
    isValid = True
except:
    print "try again"


try:
    end_date = datetime.datetime.strptime(end_date, "%d/%m/%y").date()
    isValid = True
except:
    print "try again"

date = start_date

df_old = pd.read_excel(path1, sheet_name = 'Sheet1') #Sheet1 is the name of sheet from which we need to copy.
df_new = pd.read_excel(path2, sheet_name = 'Sheet1') #Sheet1 in this line defines the sheet name to which we to paste.

data = df_new

while True:
    df1 = df_old[df_old['DATE']== date]
    #print df1
    row = df1[['DATE','val8','val5','val7']]
#    data = df_new
    data = data.append(row)
#    print data
    date = date + datetime.timedelta(days=1)
    
    if date > end_date:
        break


data['DATE'] = pd.to_datetime(data['DATE']).dt.date

print data

##Copies the required information into the required Sheet.
data.to_excel(path2,sheet_name = 'Sheet1', index = False)


