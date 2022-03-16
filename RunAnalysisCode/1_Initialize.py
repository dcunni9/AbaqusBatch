import os
import shutil
#Indicate a general folder in the DATA drive (drive with largest available memory) where you would like your code to work in. 
txt = input("Please input directory path - must be empty and in the data drive (e.g = D:/Users/HULCUSER/dcunni9/AbaqusData): ")
usersubfolder = txt
#"D:/Users/HULCUSER/dcunni9/AbaqusData"

#this portion of the code will create your MultiQueuedFiles, QueryOdb_oneinpfileonly, and DataArchive folders. 
if len(os.listdir(usersubfolder) ) == 0:
    os.mkdir(usersubfolder + "/MultiQueuedFiles")
    os.mkdir(usersubfolder + "/QueryOdb_oneinpfileonly")
    os.mkdir(usersubfolder + "/DataArchive")
    shutil.copyfile("IEEE_citation.txt", usersubfolder + "/IEEE_citation.txt")
else:
    print("This is not an empty directory, please use an empty directory.")