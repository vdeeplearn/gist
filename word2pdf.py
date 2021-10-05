# https://medium.com/swlh/convert-doc-file-to-pdf-by-python-in-batch-c0ac405ff1d2
import docx
import glob
import os
import re
import comtypes.client
fileslist=glob.glob(r"C:\Users\Hp\Downloads\*.docx")
regex_filename=r".*\\"
regex_withoutext=r".docx"
for i in range(0, len(fileslist)):
    filename=re.sub(regex_filename, "", fileslist[i])
    filename=re.sub(regex_withoutext, "", filename)
    in_file = os.path.abspath(fileslist[i])

    out_file = os.path.abspath(r"C:\Users\Hp\Desktop\\"+str(filename))

    word = comtypes.client.CreateObject('Word.Application')
    doc = word.Documents.Open(in_file)
    doc.SaveAs(out_file, FileFormat=17)

doc.Close()
