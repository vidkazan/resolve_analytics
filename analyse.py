from os import close, read
from tkinter import *
import sys
import time
import subprocess
import os
from tkinter import filedialog
from tkinter import ttk


def getFolderPath(self):
    folder_selected = filedialog.askdirectory()
    folderPath.set(folder_selected)
    folder = folderPath.get()
    files = os.listdir(folder)
    print(files)


gui = Tk()
folderPath = StringVar()
panelFrame = Frame(gui, height = 50, bg = 'gray')
textFrame = Frame(gui, height = 340, width = 600)

panelFrame.pack(side = 'top', fill = 'x')
textFrame.pack(side = 'bottom', fill = 'both', expand = 1)

loadBtn = Button(panelFrame, text="Open directory")
saveBtn = Button(panelFrame, text = 'n/a')
quitBtn = Button(panelFrame, text = 'n/a')

loadBtn.place(x = 10, y = 10, width = 150, height = 30)
saveBtn.place(x = 150, y = 10, width = 40, height = 30)
quitBtn.place(x = 190, y = 10, width = 40, height = 30)

loadBtn.bind("<Button-1>",getFolderPath)
gui.mainloop()

# filePath = "./output/"
# fileExtension = ".txt"
# print('file name without extension:')
# fileOnlyName = str(input())
# fileName = filePath + fileOnlyName + fileExtension
# durationActive = int(0)
# print(fileName)
# print('proj name:')
# project = str(input())
# print('rate:')
# Rate = int(input())
# print('Project: ' + project)

# def spaceCatch(currentLine):
#     currentLine = str(currentLine)
#     index = currentLine.find(' ')
#     return index

# def lineAnalyse(type):
#     currentLine = file.readline()
#     if not currentLine:
#         return -1
#     currentLineSplitted = currentLine.split(' ')
#     currentLineProject = currentLineSplitted[0]
#     currentLineTime = int(currentLineSplitted[1])
#     currentLineDuration = int(currentLineSplitted[2])
#     currentLineActiveness = (currentLineSplitted[3])
#     if (currentLineActiveness == type and currentLineProject == project):
#         return currentLineDuration
#     return 0


# file = open(fileName, "r")
# sum_active = 0
# sum_not_active = 0
# while 1:
#     res_active = lineAnalyse('active\n')
#     if res_active == -1:
#         break
#     sum_active += res_active
#     hours_active = float(sum_active) / 3600
# file.close()
# file = open(fileName, "r")
# while 1:
#     res_not_active = lineAnalyse('not_active\n')
#     if res_not_active == -1:
#         break
#     sum_not_active += res_not_active
#     hours_not_active = float(sum_not_active) / 3600
# print(project + ' hoursActive = ' + str(hours_active) + ' hourRateActive = ' + str(int(Rate/hours_active)) + ' hoursTotal = ' + str(hours_active + hours_not_active) + ' hourRateTotal = ' + str(int(Rate/(hours_active + hours_not_active))))