import os
import sys

#1. Indicate where all the .inp files are located
usersubfolder = "D:/Users/HULCUSER/dcunni9/AbaqusData"

inputdirectory = "E:/Users/hulcuser/Documents/AbaqusData/MultiQueuedFiles"
#2. Indicate where the inp files need to go
datadirectory = "E:/Users/hulcuser/Documents/AbaqusData/QueryOdb_onefileonly"
#3. Indicate where the odb and inp files need to be stored afterwards
exportdirectory = "E:/Users/hulcuser/Documents/AbaqusData/Archive/ArchivedMultiQueue"

files = os.listdir(inputdirectory)
for f in files:
    print("Moving " + f + " to data directory.")
    os.replace(inputdirectory + "/" + f, datadirectory + "/" + f)
    import RunAnalysisCheck
    RunAnalysisCheck
    os.replace (datadirectory + "/" + f, exportdirectory + "/" + f)
    if os.path.exists(datadirectory + "/" + f[:-4] + '.odb'):
        os.replace(datadirectory + "/" + f[:-4] + '.odb', exportdirectory + '/' + f[:-4] + '.odb')

pygame.mixer.music.load(root_path + "/SoundBytes/test-complete-preparing-to-power-down-and-begin-diagnostics.mp3")
pygame.mixer.music.play(0)
clock = pygame.time.Clock()
clock.tick(10)
while pygame.mixer.music.get_busy():
    pygame.event.poll()
    clock.tick(10) 