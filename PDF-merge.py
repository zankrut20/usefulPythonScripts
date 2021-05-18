import PyPDF2
import os

# user input for PDF file directory
userPDFlocation = input('Path of folder which has PDF files: ')
os.chdir(userPDFlocation)

# File name to save file after combine the files
userFilename = input('File name after merge: ')

# All PDF filenames
pdf2merge = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdf2merge.append(filename)

pdfWriter = PyPDF2.PdfFileWriter()

# Looping for all pdfs
for filename in pdf2merge:
    pdfFileOpen = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileOpen) # Reading
    for pageNum in range(pdfReader.numPages): # Adding pages
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
    pdfOutput = open(userFilename+'.pdf', 'wb') # Output
    pdfWriter.write(pdfOutput) # Writing as pdf
    pdfOutput.close()