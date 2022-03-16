import os
#IT'S IMPORTANT THAT YOU ONLY RUN THIS ONCE, OR YOU WILL LOSE ALL YOUR WORK! 
#Indicate a general folder in the DATA drive (drive with largest available memory) where you would like your code to work in. 
usersubfolder = "D:/Users/HULCUSER/dcunni9/AbaqusData"

#this portion of the code will create your MultiQueuedFiles, QueryOdb_oneinpfileonly, and DataArchive folders. 



os.mkdir(usersubfolder + "/MultiQueuedFiles")
os.mkdir(usersubfolder + "/QueryOdb_oneinpfileonly")
os.mkdir(usersubfolder + "/DataArchive")