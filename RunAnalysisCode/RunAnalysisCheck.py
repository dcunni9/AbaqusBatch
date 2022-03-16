import os 
import sys 
import pandas as pd
import matplotlib.pyplot as plt
from pylab import *
from mpl_toolkits.mplot3d import axis3d
import numpy as np
import requests
from discord import *
import pygame
import plotly.express as px
from AnalysisStart import *

#important! When you're evaluating a batch, make sure you're evaluating something like CPRESS - a nodal calucated field output or the batch will not run. 
#also, make sure to update DataAnalysisManual if you are evaluating stress. 

#1. SETTINGS 
#start by putting all the files you want to create plots want to analyze in one folder. 
#do you want to start the process from the .inp files? (1) or do you want to start the process from the .odb files?
do_you_want_to_run_analysis = 1 #please make sure you have a .inp file in the same folder as "QueryOdb_onefileonly"
use_matplotlib_0_use_pyplot_1 = 1 #1 for pyplot, 0 for matplotlib
use_AbaqusGUI_0_noGUI_1 = 1 #0 for GUI, 1 for noGUI
show_figures_after = 0 #0 for nofigs, 1 for figs
have_you_already_run_xydata = 1 #1 for if you already have xydata saved and just need to modify plot settings.
#if you evaluate an element-nodal field output you will not be able to run multiple batches. 
what_do_you_want_to_evaluate = 'CPRESS' #choose S, CPRESS, E etc. Might need to update run abaqus GUI based on what you're evaluating 

#2. Next, indicate where your .inp or .odb files are stored during each analysis (the folder path) - this should be in the data drive(biggest one)
datadirectory = "E:/Users/hulcuser/Documents/AbaqusData/QueryOdb_onefileonly"
#3. Next, indicate where the .py files have been stored. 
root_path = 'C:/Users/HULCUSER/Desktop/AbaqusResult/AbaqusDataAnalysis'
#4. Indicate where you would like to store the output .csv files for reference and analysis later on. 
dataanalysisdirectory = "E:/Users/hulcuser/Documents/AbaqusData/Archive/ArchivedforAnalysis"
#5. Indicate where you want to store your output figures for easy access. 
figuredirectory = "E:/Users/hulcuser/Documents/AbaqusData/Archive/FiguresforAnalysis"
#6. Indicate where you want to store your temp files. 
tempfiledirectory = "E:/Users/hulcuser/Documents/AbaqusData/Archive/TempFiles"
#7. Indicate the working directory that you want to use. 
workingdirectory = "E:/Users/hulcuser/Documents/AbaqusData/Archive/ArchivedforTesting"

files = os.listdir(datadirectory)
for f in files:
    if f.endswith(".inp"):
        database_path =  str(datadirectory) + "/" + f
        print(database_path)
head, tail = os.path.split(database_path)
if do_you_want_to_run_analysis == 1:
    runanalysis(database_path, root_path, workingdirectory)

#info. this portion of the code plays the soundbyte indicating that the analysis is complete (if it has run), and that data extraction has now begun.
pygame.init()
pygame.mixer.music.load(root_path +"/SoundBytes/sir-there-are-still-terabytes-of-calculations-needed-before-an-actual-flight-is.mp3")
pygame.mixer.music.play(0)
clock = pygame.time.Clock()
clock.tick(10)
while pygame.mixer.music.get_busy():
    pygame.event.poll()
    clock.tick(10) 

#this portion of the code will change whether or not the Abaqus GUI is active. 
if use_AbaqusGUI_0_noGUI_1 == 1:
    if what_do_you_want_to_evaluate == 'S':
        print("Too bad, in order to evaluate stress you're going to have to use the GUI")
        print("This will take a while! Be patient please. You will have to be present to confirm 'Yes to all' in prompt.")
        if have_you_already_run_xydata == 0:
            os.system('abaqus cae replay=' + root_path + '/DataAnalysisManual.rpy')
    else:
        print("noGUI")
        os.system('abaqus cae noGUI='+ root_path + "/AnalysisCheck.py") #for no GUI
if use_AbaqusGUI_0_noGUI_1 == 0:
    if what_do_you_want_to_evaluate == 'S':        
        print("This will take a while! Be patient please. You will have to be present to confirm 'Yes to all' in prompt.")
        os.system('abaqus cae replay=' + root_path + '/DataAnalysisManual.rpy')
    else:
        print("GUI")
        os.system('abaqus cae script='+ root_path + "/AnalysisCheck.py") #for GUI
    

if os.path.exists("abaqus.rpy"):
    os.remove("abaqus.rpy")

pygame.init()
pygame.mixer.music.load(root_path +"/SoundBytes/tell-you-what-throw-a-little-hot-rod-red-in-there-yes-that-should-help-you-keep-a-low-profile.mp3")
pygame.mixer.music.play(0)
clock = pygame.time.Clock()
clock.tick(10)
while pygame.mixer.music.get_busy():
    pygame.event.poll()
    clock.tick(10) 


###NEED TO REDO THIS - NOT WORKING! 

#data = pd.read_csv(tempfiledirectory +'/temppt1.txt', sep='/s+', names =['node', 'x-data', 'y-data', 'z-data'], index_col=0)
#data2 = pd.read_csv(tempfiledirectory +'/temppt2.txt', names =['OutputScalar'])
#data3 = pd.read_csv(tempfiledirectory +'/temppt3.txt', names =['node'])
#data2.insert(0, 'node', data3)
#data2.groupby('node').mean().reset_index()

#update this manually CPRESS to S until we can figure it out 

#datafinal = pd.concat([data2, data], axis =1, join="inner") #this is for S

#datafinal.to_csv(r"C:/Users/HULCUSER/Desktop/finaltest.csv")
#dataskip = 10
#x = datafinal.iloc[::dataskip,2]
#y = datafinal.iloc[::dataskip,3]
#z = datafinal.iloc[::dataskip,4]
#C = datafinal.iloc[::dataskip,1]
if what_do_you_want_to_evaluate == 'S':
    skip = 20
    print("Processing xy element data from "+ (tail[:-4]) +".odb (60s+ for 2Gb xy data file)")
    data = np.genfromtxt("E:/Users/hulcuser/Documents/AbaqusData/Archive/ArchivedforTesting/"+ "xyoutput" +".csv", delimiter=',', usecols = (3,6,7,8,12), dtype=float, skip_footer = 160000)
    data = np.asarray(data)
    print(data)
    data = np.delete(data, np.where(data[:,0] != '"TOTALBONE'), axis = 0)
    print(data)     
    #columns = pd.read_csv("E:/Users/hulcuser/Documents/AbaqusData/Archive/ArchivedforTesting/"+ "xyoutput" +".csv", index_col=0, nrows=0).columns.tolist()
    #print(columns)
    #data = pd.read_csv("E:/Users/hulcuser/Documents/AbaqusData/Archive/ArchivedforTesting/"+ "xyoutput" +".csv", usecols = ['Part Instance Name', 'X', 'Y', 'Z', 'S-Max. Principal'], low_memory = False)
    #data.columns = [c.replace(' ', '_') for c in data.columns]
    #data = data[data.Part_Instance_Name == 'TOTALBONE-1']
    #data.columns = ['Bone','X','Y','Z','S']
    #data = data.drop(columns = ['Bone'])
    #print(data)
    #print(data[0:8,:])
    #xyzc = data.iloc[:,:].values
    #del data
    #print(xyzc)
    #x = xyzc[::skip,0]
    #y = xyzc[::skip,1]
    #z = xyzc[::skip,2]
    #C = xyzc[::skip,3]

    print("Writing figure")


else:    
    #data = np.genfromtxt(tempfiledirectory +'/temppt1.txt', dtype=None, encoding=None, delimiter=' ')
    data = pd.read_csv(tempfiledirectory +'/temppt1.txt', delimiter=' ', header = None)
    data = np.array(data)
    #print(data[0:8,:])
    #data2 = np.genfromtxt(tempfiledirectory +'/temppt2.txt', dtype=float, encoding=None, delimiter=' ')
    data2 = pd.read_csv(tempfiledirectory +'/temppt2.txt', header = None)
    data2 = np.array(data2)
    #print(data2[0:8,:])
    #data3 = np.genfromtxt(tempfiledirectory +'/temppt3.txt', dtype=float, encoding=None, delimiter=' ')
    data3 = pd.read_csv(tempfiledirectory +'/temppt3.txt', delimiter=' ', header = None)
    data3 = np.array(data3)
    #print(data3[0:8,:])
    #datafinal = np.insert(data2, 0, data3, axis=1)
    datafinal = np.insert(data, 0, data2, axis=1)
    #print(datafinal[0:8,:])
    x = data[::1,1]
    y = data[::1,2]
    z = data[::1,3]
    C = data2[::1,0]

    #data.columns are "CPRESS", "x-coord", "y-coord", "z-coord"

if use_matplotlib_0_use_pyplot_1 == 0:
    #to do the graphing using matplotlib 
    #set colour mapping scheme
    colmap = cm.ScalarMappable(cmap=cm.Reds)
    colmap.set_array(C)
    #plot the figure as a 3D scatter with heatmap 
    fig = plt.figure()
    ax = fig.add_subplot(111, projection ='3d')
    ax.scatter(x,y,z, c = cm.Reds(C/max(C)))
    plt.xlabel("x axis")
    plt.ylabel("y axis") 
    head, tail = os.path.split(database_path)
    plt.savefig(figuredirectory + "/"+ (tail[:-4]) +".png")
    plt.show()


elif use_matplotlib_0_use_pyplot_1 == 1:
    #using plotly instead
    upperrange = 0.47 #x.max()
    df= {'x-coordinates [mm]': x, 'y-coordinates [mm]':y, 'z-coordinates [mm]':z, what_do_you_want_to_evaluate:C}
    min = np.min(C)
    max = np.max(C)
    values = pd.DataFrame(data=df)
    head, tail = os.path.split(database_path)
    values.to_csv(dataanalysisdirectory + "/" + (tail[:-4]) +".csv")
    #fig = px.scatter_3d(values, x='x-coordinates [mm]', y='y-coordinates [mm]', z='z-coordinates [mm]', color ='magnitude', color_continuous_scale=px.colors.sequential.Reds, range_color=[0,2])
    fig = px.scatter_3d(values, x='x-coordinates [mm]', y='y-coordinates [mm]', z='z-coordinates [mm]', color =what_do_you_want_to_evaluate, color_continuous_scale=px.colors.diverging.RdYlGn_r, range_color=[0,upperrange])
    fig.update_traces(marker=dict(size=2))
    if show_figures_after == 1:
        fig.show()
    #saving the figure using plotly HTML
    fig.write_html(figuredirectory + "/" + (tail[:-4]) +'.html')

webhook_url = "<https://discord.com/api/webhooks/907991398073126992/ob6eJzwrlFTsvVNa6m6xUX2rachlx3f6DAX6sAPiIZBn-qCe-ELb15vn2au5W5nH4Pms>"
webhook = Webhook.from_url(webhook_url, adapter=RequestsWebhookAdapter())
webhook.send("Analysis of " + (tail[:-4]) + " is complete.")

pygame.mixer.music.load(root_path + "/SoundBytes/test-complete-preparing-to-power-down-and-begin-diagnostics.mp3")
pygame.mixer.music.play(0)
clock = pygame.time.Clock()
clock.tick(10)
while pygame.mixer.music.get_busy():
    pygame.event.poll()
    clock.tick(10) 
    


     
