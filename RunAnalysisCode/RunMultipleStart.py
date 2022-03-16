import os
import sys

#1. Indicate where all the .inp files are located
inputdirectory = "E:/Users/hulcuser/Documents/AbaqusData/MultiQueuedFiles"
#2. Indicate where the inp files need to go
datadirectory = "E:/Users/hulcuser/Documents/AbaqusData/QueryOdb_onefileonly"
#3. Indicate where the odb and inp files need to be stored afterwards
exportdirectory = "E:/Users/hulcuser/Documents/AbaqusData/Archive/ArchivedMultiQueue"

files = os.listdir(inputdirectory)
for f in files:
    #if f.endswith(".inp"):
    print("Moving " + f + " to data directory.")
    os.replace(inputdirectory + "/" + f, datadirectory + "/" + f)
    import RunAnalysisCheck
    RunAnalysisCheck
    os.replace (datadirectory + "/" + f, exportdirectory + "/" + f)
    if os.path.exists(datadirectory + "/" + f[:-4] + '.odb'):
        os.replace(datadirectory + "/" + f[:-4] + '.odb', exportdirectory + '/' + f[:-4] + '.odb')