from os import access, close, read
from tkinter import *
import sys
import time
import subprocess
import os
from tkinter import filedialog
from tkinter import ttk

class Active(object):
    def __init__(self, time, duration):
        self.time = 0
        self.duration = 0

class Passive(object):
    def __init__(self, time, duration):
        self.time = 0
        self.duration = 0

class Project(object):
    def __init__(self, name, rate):
        self.name = "projectName"
        self.rate = 0
        self.active = []
        self.passive = []
        self.durationActive = 0
        self.durationPassive = 0
        self.durationAll = 0

    def printAllElems(self):
        print(self.name)
        print(self.rate)
        print(self.active)
        print(self.passive)

    def getTimeActive(self):
        return self.timeActive

    def getTimePassive(self):
        return self.timePassive

    def getProjectName(self):
        return self.name 

def configFileRead():
    if os.path.isfile(configFileName):
        configFile = open(configFileName, "r")
    else:
        return
    filePath = configFile.readline()
    if not filePath:
        return 
    return filePath

def getFolderPath(self):
    folder_selected = filedialog.askdirectory()
    folderPath.set(folder_selected)
    filePath = folderPath.get()
    filePath += "/"
    configFile = open(configFileName, "w")
    configFile.write(filePath)

def durationSumm(proj):
    res = 0
    k = 0
    while k < len(proj.active):
        res += proj.active[k].duration
        k+=1
    proj.durationActive = res
    res = 0
    k = 0
    while k < len(proj.passive):
        res += proj.passive[k].duration
        k+=1
    proj.durationPassive = res
    proj.durationAll = proj.durationActive + proj.durationPassive

def drawProjects(self):
    j = 0
    while j < len(projects):
        durationSumm(projects[j])
        j+=1
    projects.sort(key = lambda Project: (float(Project.durationActive) / float(Project.durationAll)))
    j=0
    while j < len(projects):
        l = Label(bg='#991212')
        l.place(x = 5, y = 45 + j * 30, width = (projects[j].durationAll)/60 * 5, height = 30)
        l1 = Label(bg='#127744', text=(projects[j].name + " " + str((projects[j].durationAll)/60) + " " + str(float(projects[j].durationActive/float(projects[j].durationAll)))))
        l1.place(x = 5, y = 45 + j * 30, width = (projects[j].durationActive)/60 * 5, height = 30)
        j+=1


def spaceCatch(currentLine):
    currentLine = str(currentLine)
    index = currentLine.find(' ')
    return index

def contains(list, value):
    c = 0
    while c < len(list):
        if list[c].name == value:
            return c
        c+=1
    return -1

def appendActivePassive(elem,currentLineTime, currentLineDuration,currentLineActiveness):
    if(currentLineActiveness):
                active = Active(currentLineTime, currentLineDuration)
                active.duration = currentLineDuration
                active.time = currentLineTime
                elem.active.append(active)
    if not (currentLineActiveness):
        passive = Passive(currentLineTime, currentLineDuration)
        passive.duration = currentLineDuration
        passive.time = currentLineTime
        elem.passive.append(passive)

def lineAnalyse(currentFile):
    currentLine = currentFile.readline()
    if not currentLine or len(currentLine) < 1:
        return -1
    else:
        currentLineSplitted = currentLine.split(' ')
        currentLineProject = currentLineSplitted[0]
        currentLineTime = int(currentLineSplitted[1])
        currentLineDuration = int(currentLineSplitted[2])
        currentLineActiveness = (currentLineSplitted[3])
        currentLineActiveness = currentLineActiveness[:-2]
        if(currentLineActiveness == "active"):
            currentLineActiveness = 1
        else:
            currentLineActiveness = 0
        index = contains(projects,currentLineProject)
        if index == -1:
            newProj = Project(currentLineProject, 1000)
            newProj.name = currentLineProject
            appendActivePassive(newProj,currentLineTime,currentLineDuration,currentLineActiveness)
            projects.append(newProj)
        else:
            appendActivePassive(projects[index],currentLineTime,currentLineDuration,currentLineActiveness)
        return 1

def readFile(currentFileName):
    print(">>> scanning " + currentFileName)
    currentFile = open(filePath + currentFileName, "r")
    while 1:
        res = lineAnalyse(currentFile)
        if res < 0:
            currentFile.close
            return

def readFiles(files):
    i = 0
    while i < len(files):
        readFile(files[i])
        i+=1
    j = 0

projects = []
configFileName = "config.txt"

gui = Tk()
gui.title("Resolve Counter Analyse")
gui.geometry("1900x1000")
gui.resizable(0,0)

folderPath = StringVar()

loadBtn = Button(gui, text="Open directory")
projBtn = Button(gui, text = 'Projects')
quitBtn = Button(gui, text = 'n/a')

loadBtn.place(x = 5, y = 5, width = 130, height = 30)
projBtn.place(x = 135, y = 5, width = 80, height = 30)
quitBtn.place(x = 215, y = 5, width = 40, height = 30)

filePath = configFileRead()
if(filePath):
    files = os.listdir(filePath)
    readFiles(files)

loadBtn.bind("<Button-1>",getFolderPath)
projBtn.bind("<Button-1>",drawProjects)
gui.mainloop()