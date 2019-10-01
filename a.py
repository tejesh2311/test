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

date = from_date 
while True:
    print (date)
    date = date + datetime.timedelta(days=1)
    
    if date > to_date:
        break
