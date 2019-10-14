#!/usr/bin/python
import glob,os,hashlib,winsound


FREQ = 2500  
DUR = 1000  

def Beep(frequency,duration):
    winsound.Beep(frequency, duration)

def create_checksum(filename):
    hasher = hashlib.md5()
    with open(filename,'rb') as file:
        hasher.update(file.read())
    print(hasher.hexdigest())

def infect():
    for file in glob.glob("*.py"):
        if file == __file__:
            continue
        print(file)





infect()