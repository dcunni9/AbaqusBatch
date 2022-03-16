import os
import sys
import re

#ask for the general directory
txt = input("Please input general directory path - must be empty and in the data drive (e.g = D:/Users/HULCUSER/dcunni9/AbaqusData): ")
usersubfolder = txt
usersubfolder= re.sub('"', '', usersubfolder)
usersubfolder = re.sub('\\\\',"/", usersubfolder)

#1. Indicates where the queued files are
inputdirectory = usersubfolder +"/MultiQueuedFiles"
#2. Indicates where the inp files need to go
datadirectory = usersubfolder +"/QueryOdb_OneInpFileOnly"
#3. Indicates where the odb and inp files need to be stored afterwards
exportdirectory = usersubfolder +"/DataArchive"

def runanalysis(path, workingdirectory):

    head, tail = os.path.split(path)
    os.chdir(workingdirectory + "/")
    if (os.path.isfile(head + '/' + tail[:-4] + '.inp')) == True:
        print("test exists")
        print(" input=" + head + '/' + tail[:-4] + '.inp')
        os.system('abaqus job=' + tail[:-4] + " input=" + head + '/' + tail[:-4] + '.inp interactive cpus=8')
        os.replace(workingdirectory + "/" + tail[:-4] + '.odb', head + '/' + tail[:-4] + '.odb')

    else:
        print("No inps you liar!!")

files = os.listdir(inputdirectory)
for f in files:
    print("Moving " + f + " to data directory.")
    os.replace(inputdirectory + "/" + f, datadirectory + "/" + f)
    
    runanalysis(datadirectory + "/" + f,exportdirectory)

    os.replace (datadirectory + "/" + f, exportdirectory + "/" + f)
    if os.path.exists(datadirectory + "/" + f[:-4] + '.odb'):
        os.replace(datadirectory + "/" + f[:-4] + '.odb', exportdirectory + '/' + f[:-4] + '.odb')

print("Done all batched analyses!")