import datetime
import pandas as pd

x = raw_input("in date/month/year")
y = raw_input("out data/month/year")

path1 = "/home/datalake/tejesh/current.xlsx"
path2 = "/home/datalake/tejesh/new.xlsx"

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

#print from_date
date = from_date 

df_old = pd.read_excel(path1, sheet_name = 'Sheet1')
df_new = pd.read_excel(path2, sheet_name = 'Sheet1')
data = df_new
while True:
#    print (date)
#    df = pd.read_excel(path1)
#    df_new = pd.read_excel(path2)
    #print df['5']
    df1 = df_old[df_old['DATE']== date]
    #print df1
    row = df1[['DATE','val8','val5','val7']]
#    data = df_new
    data = data.append(row)
#    print data
    date = date + datetime.timedelta(days=1)
    
    if date > to_date:
        break

#print data
#data['just_date'] = data ['dates'].dt.date 
#data = pd.Timestamp(data)

#print data

#data['DATE'] = pd.to_datetime(data['DATE'], dayfirst=True, errors='coerce')
data['DATE'] = pd.to_datetime(data['DATE']).dt.date
#print abcd
data.to_excel(path2,sheet_name = 'Sheet1', index = False)
#abcd.to_excel(path2,sheet_name = 'Sheet1', index = False)


