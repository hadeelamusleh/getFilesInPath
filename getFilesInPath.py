'''
this programe use to read all files from path
and get report about it (types file , number of files for each one and list of files)
'''
import glob
from pip._vendor.distlib.compat import raw_input
#start function which return a dictionery contane types of files , number of files for each one and list of files
#function start with parameter path (path to read files content
def allFiles(path):
 filesName=glob.glob(path)#get files with full path for each from path
 if(filesName!=[]):#if path is not  uncorrect or empty
     Files_without_path=[]#define dictionary to save file without path
     for i in filesName:#for loop on filesName
        i=i.split("/")#split file about /
        i=i[len(i)-1]#save the file name only(last index from result of split
        Files_without_path.append(i)#save file name in Files_without_path
     allFiles={}#new dictonary to save types of files ,numbers of files for each one and list of files
     for i in range(len(Files_without_path)):#for loop on Files_without_path
       file=Files_without_path[i].split(".")#split file name about . to get type of it
       if(len(file)==1):#if name of file don't content .
          type="folders"# file is folder
       else:#file content .
         type=file[len(file)-1]#save type in variable type
       if type in allFiles:#search in allFiles dictionary about type if found it that mean is not the fisrt file from this type
           allFiles[type]["num_of_files"]=allFiles[type]["num_of_files"]+1#add counter of this type one
           allFiles[type]["files"].append(Files_without_path[i])#add the file name to the list
       else:#if the file is the first file from this type
           allFiles[type]= {"num_of_files":1,"files":[Files_without_path[i]]}#put counter 1 and add file to the list
 else:#if path is empty or error
   print("Empty or Error in path")#print error
 return allFiles#return allFiles with all info

try:#main
    if __name__== '__main__':
       path=raw_input('Enter the path :')#get path from input
       files=allFiles(path)#call function
       print(files)#print result
except ValueError:#error
  print("Error")

