from termcolor import colored
from tqdm import tqdm
import zipfile


wl = input("enter the wordlist: ")#for wordlist  
zp = input("enter the zip file: ")#for zip file
var = ""
wordlist = [password.strip() for password in open(wl,encoding='cp437')]
zip_file = zipfile.ZipFile(zp)

for i in tqdm(wordlist,desc = "checking :"):
    try:
        zip_file.extractall(pwd=i.encode())
        var = i
        break
    except :
        #print(i)
        continue
print(colored("[+] password is : {}".format(var),"green"))