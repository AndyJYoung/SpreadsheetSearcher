#import library
import gspread
import pandas as pd

#connect to the service account
gc = gspread.service_account(filename="creds.json")

#connect to your sheet (between "" = the name of your G Sheet, keep it short)
sh = gc.open("FLCL Python Version")
currws = sh.worksheet("All Time Car List")

rowstr = input("Enter the num of the row you would like to select: ")
while not rowstr.isdigit():
    rowstr = input("Please enter a valid number: ")

rownum = int(rowstr) + 1
rowstr = str(rownum)

pos = "A" + rowstr + ":" + "T" + rowstr

#get the values from cells a2 and b2
#col_names = "Yr, Manufacturer, Model, Country, Type, M1, M2, M3, M4, H1, M5, H2, M6, H3, M7, H4, H5, M8, DLC?, Notes"
#val_list = currws.get(pos)

df1 = pd.DataFrame(currws.get("A1:T1"))
df2 = pd.DataFrame(currws.get(pos))

#print(col_names)
#print(val_list)

df1 = pd.concat([df1, df2], ignore_index=True)
print(df1)