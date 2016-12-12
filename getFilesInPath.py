import glob
from pip._vendor.distlib.compat import raw_input
def allFiles(path):
 filesName=glob.glob(path)
 if(filesName!=[]):
     sortedFiles=[]
     for i in filesName:
        i=i.split("/")
        i=i[len(i)-1]
        sortedFiles.append(i)
     allFiles={}
     for i in range(len(sortedFiles)):
       file=sortedFiles[i].split(".")
       if(len(file)==1):
           path="folders"
       else:
         path=file[len(file)-1]
       if path in allFiles:
           allFiles[path]["num_of_files"]=allFiles[path]["num_of_files"]+1
           allFiles[path]["files"].append(sortedFiles[i])
       else:
           allFiles[path]= {"num_of_files":1,"files":[sortedFiles[i]]}
 else:
   print("Error in path")
 return allFiles

try:
 path=raw_input('Enter the path :')
 files=allFiles(path)
except ValueError:
 print("Error")
