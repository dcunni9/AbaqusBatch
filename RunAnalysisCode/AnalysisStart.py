import os 
import sys 
import pygame
from discord import *
import pygame

def runanalysis(path, root_path, workingdirectory):

    pygame.init()
    pygame.mixer.music.load(root_path + "/SoundBytes/working-on-a-secret-project-are-we-sir.mp3")
    pygame.mixer.music.play(0)
    clock = pygame.time.Clock()
    clock.tick(10)
    while pygame.mixer.music.get_busy():
        pygame.event.poll()
        clock.tick(10) 

    head, tail = os.path.split(path)
    os.chdir(workingdirectory + "/")
    if (os.path.isfile(head + '/' + tail[:-4] + '.inp')) == True:
        print("test exists")
        webhook_url = "<https://discord.com/api/webhooks/907991398073126992/ob6eJzwrlFTsvVNa6m6xUX2rachlx3f6DAX6sAPiIZBn-qCe-ELb15vn2au5W5nH4Pms>"
        webhook = Webhook.from_url(webhook_url, adapter=RequestsWebhookAdapter())
        webhook.send("Analysis of " + (tail[:-4]) + " has started.")
        os.system('abaqus job=' + tail[:-4] + " input=" + head + '/' + tail[:-4] + '.inp interactive cpus=8')
        os.replace(workingdirectory + "/" + tail[:-4] + '.odb', head + '/' + tail[:-4] + '.odb')

    else:
        print("You're not running analysis, you liar! I hope that there's an .odb file in the datadirectory or you'll get an error!")

    

