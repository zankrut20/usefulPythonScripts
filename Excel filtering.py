import pandas as pd
import os
from openpyxl import load_workbook
from shutil import copyfile

# Related to file and path
file = input("File Path: ")
extn = os.path.splitext(file)[1]
file_name = os.path.splitext(file)[0]
path = os.path.dirname(file)
new_file = os.path.join(path, file_name + "_2" + extn)
df = pd.read_excel(file)
colpick = input("Select Colums: ")
cols = list(set(df[colpick].values))

# function for creating files
def sendtofile(cols):
    for i in cols:
        df[df[colpick] == i].to_excel("{}/{}.xlsx".format(path, i), sheet_name = i, index = False)
        print("\nCompleted")
        print("Thanks for using this program.")
        return

# function for creating different sheets
def sendtosheet(cols):
    copyfile(file, new_file)
    for j in cols:
        writer = pd.ExcelWriter(new_file, engine = "openpyxl")
        for myname in cols:
            mydf = df.loc[df[colpick] == myname]
            mydf.to_excel(writer, sheet_name = myname, index = False)
        writer.save()
    print("\nCompleted")
    print("Thanks for using the program.")

# user input regarding options
print('Your data will split based on these values {} and create {} files or sheets based on next selection. If you are ready to proceed please type "Y" and hit enter. Hit "N" to exit.')
while True:
    x = input("Ready to Proceed (Y/N): ").lower()
    if x == 'y':
        while True:
            s = input("Split into different Sheets (S) or Files(F) (S/F): ").lower()
            if s == 'f':
                sendtofile(cols)
                break
            elif s == 's':
                sendtosheet(cols)
                break
            else: continue
        break
    elif x == 'n':
        print("\nThnaks for using this Program.")
        break
    else:
        continue