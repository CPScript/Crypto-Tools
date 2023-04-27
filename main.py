import time
import os
import sys
import subprocess
from os  import system
from subprocess import call
from platform import platform


# delete
puk = platform()[0], platform()[1],  platform()[2], platform()[3], platform()[4], platform()[5], platform()[6]

if puk == ('W', 'i', 'n', 'd', 'o', 'w', 's'):
    delet = 'cls'
    dr = '\\'
else:
    delet = 'clear'
    dr = '/'

os.system(delet)
time.sleep(1)
print("Loading BTC tools...")
time.sleep(7)
os.system(delet)
call(["python", "Bitcoin/main.py"])
