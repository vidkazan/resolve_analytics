import sys
import time
from types import NoneType
import DaVinciResolveScript as dvr_script
from win32gui import GetWindowText, GetForegroundWindow
filePath = "C:\\Users\\Totoro\\Desktop\\Resolve_counter\\output\\"
fileExtension = ".txt"
resolveName = 'DaVinci Resolve by Blackmagic Design'

def fileNameGenerator():
    ts = time.localtime()
    year = str(ts.tm_year)
    mon = str(ts.tm_mon)
    name = filePath + str(mon) + str(year) + fileExtension
    return name

def activeWinCheck():
    activeWindow = GetWindowText(GetForegroundWindow())[0:36]
    if(activeWindow != resolveName):
        return str('not_active')
    return str('active')

file = open(fileNameGenerator(), "a")
if not file:
    print('file: error')
    exit()
resolve = dvr_script.scriptapp("Resolve")
while not resolve:
    time.sleep(1)
    print('waiting for Resolve')
    resolve = dvr_script.scriptapp("Resolve")
projectManager = resolve.GetProjectManager()
print(resolve)
while projectManager:
    if not (dvr_script.scriptapp("Resolve")):
        break
    project = projectManager.GetCurrentProject()
    if project:
        name = project.GetName()
        if name:
            print('Project: ' + name)
            start_timestamp = time.time()
            isResolveActiveWin = activeWinCheck()
            while ((project.GetName() == name) and (activeWinCheck() == isResolveActiveWin)):
                time.sleep(1)
                current_timestamp = time.time()
            if(current_timestamp and (int(current_timestamp - start_timestamp) > 10)):
                duration = current_timestamp - start_timestamp
                file.write(name + ' ' + str(int(start_timestamp)) + ' ' + str(int(duration)) + ' ' + isResolveActiveWin + '\n')
                print(name + ' ' + str(int(start_timestamp)) + ' ' + str(int(duration)) + ' ' + isResolveActiveWin)
    time.sleep(1)
print('exiting')
file.close()