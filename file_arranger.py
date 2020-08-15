import os
import glob

# detect the file names in directory
files_lst = glob.glob("*")

# for storing the different file extensions
extn_set = set()
for file in files_lst:
    extn = file.split(sep=".") # later using to create a directory according to extension
    try:
        extn_set.add(extn[1])
    except IndexError:
        continue

# print(extension_set)

# create directory function for extensions which is stored in extension_set
def create_dir():
    for dir in extn_set:
        try:
            os.makedirs(dir+"_files")
        except FileExistsError:
            continue

# arranger function to move files into their respective directory
def arranger():
    for file in files_lst:
        fextension = file.split(sep=".")
        try:
            os.rename(file, fextension[1]+"_files/"+file)
        except (OSError, IndexError):
            continue

# calling order
create_dir()
arranger()