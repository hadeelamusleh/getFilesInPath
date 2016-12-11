import glob
import re
from pip._vendor.distlib.compat import raw_input
try:
   path=raw_input('Enter the path :')
except ValueError:
    print("Error")


filesName=glob.glob(path)
if(filesName!=[]):
    print(filesName);
    filesName=str(filesName).strip('[]')
    filesName= re.sub('[\']', '', filesName)
    filesName=filesName.split(",")
    for i in range(len(filesName)):
        file=filesName[i].split("/")
        file=file[len(file)-1]
        filesName[i]=file
        sortedFiles=filesName
    for i in range(len(sortedFiles)):
        for j in range(len(sortedFiles)):
            file1=sortedFiles[i].split(".")
            pathFile1=file1[len(file1)-1]
            file2 = sortedFiles[j].split(".")
            pathFile2 = file2[len(file2) - 1]
            if(pathFile1> pathFile2):
                 temp=sortedFiles[i]
                 sortedFiles[i]=sortedFiles[j]
                 sortedFiles[j]=temp
    print("In your path have %d files"%len(sortedFiles))
    first=sortedFiles[0].split(".")
    firstpath=first[len(first)-1]
    print("the  %s file is :"%firstpath)
    for i in range(len(sortedFiles)):
        file=sortedFiles[i].split(".")
        path=file[len(file)-1]
        if(path==firstpath):
            print("\t %s"%sortedFiles[i])
        else:
            firstpath=path
            print("the %s file is :"%path)
            print("\t %s"%sortedFiles[i])
else:
    print("Error in path")