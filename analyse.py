from os import close, read
import sys
import time

filePath = "C:\\Users\\Totoro\\Desktop\\Resolve_counter\\output\\"
fileExtension = ".txt"
print('file name without extension:')
fileOnlyName = str(raw_input())
fileName = filePath + fileOnlyName + fileExtension
durationActive = int(0)
print(fileName)
print('proj name:')
project = str(raw_input())
print('rate:')
Rate = int(raw_input())
print('Project: ' + project)

def spaceCatch(currentLine):
    currentLine = str(currentLine)
    index = currentLine.find(' ')
    return index

def lineAnalyse(type):
    currentLine = file.readline()
    if not currentLine:
        return -1
    currentLineSplitted = currentLine.split(' ')
    currentLineProject = currentLineSplitted[0]
    currentLineTime = int(currentLineSplitted[1])
    currentLineDuration = int(currentLineSplitted[2])
    currentLineActiveness = (currentLineSplitted[3])
    if (currentLineActiveness == type and currentLineProject == project):
        return currentLineDuration
    return 0

file = open(fileName, "r")
sum_active = 0
sum_not_active = 0
while 1:
    res_active = lineAnalyse('active\n')
    if res_active == -1:
        break
    sum_active += res_active
    hours_active = float(sum_active) / 3600
file.close()
file = open(fileName, "r")
while 1:
    res_not_active = lineAnalyse('not_active\n')
    if res_not_active == -1:
        break
    sum_not_active += res_not_active
    hours_not_active = float(sum_not_active) / 3600
print(project + ' hoursActive = ' + str(hours_active) + ' hourRateActive = ' + str(int(Rate/hours_active)) + ' hoursTotal = ' + str(hours_active + hours_not_active) + ' hourRateTotal = ' + str(int(Rate/(hours_active + hours_not_active))))