# Enter script code
import sys
import time
import win32com.client
from os.path import expanduser, join
try:
    import win32api
except ModuleNotFoundError:
    import pip
    pip.main(['install'], 'pypiwin32')
    import win32api

cmd = open(join(expanduser('~'), '.stata-exec_code.txt'),'r').read()
stata_path = "C:\Program Files (x86)\Stata15\StataMP-64.exe"

def StataAutomate(stata_command):
    """ Launch Stata (if needed) and send commands """
    try:
        stata.DoCommandAsync(stata_command)

    except:
        win32api.WinExec(stata_path)
        stata = win32com.client.Dispatch("stata.StataOLEApp")
        stata.DoCommandAsync(stata_command)

StataAutomate("sysuse auto, clear")

stata = win32com.client.Dispatch("stata.StataOLEApp")
stata.DoCommandAsync("sysuse auto, clear")
