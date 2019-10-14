import pandas as pd

df = pd.read_excel('/home/datalake/tejesh/current.xlsx')
#print df['5']
df1 = df[df['DATE']=='21/10/19']
print df1
print df1[['DATE','val8','val5','val7']]
