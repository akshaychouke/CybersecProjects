import requests
from termcolor import colored

# Welcome Page 
print(colored("*********************************************************************************","red"))
print(colored("*\t\t\t\t\t\t\t\t\t\t*","red"))
print(colored("*\t\t\t\t\t\t\t\t\t\t*","red"))
print(colored("*\t\t\t\t\t\t\t\t\t\t*","red"))
print(colored("*\t\t\t\t\t\t\t\t\t\t*","red"))
print(colored("*\t\t\t Welcome to The Directory Brute Forcer\t\t\t*","red"))
print(colored("*\t\t\t\t\t\t\t\t\t\t*","red"))
print(colored("*\t\t\t\t\t\t\t\t\t\t*","red"))
print(colored("*\t\t\t\t\t\t\t\t\t\t*","red"))
print(colored("*\t\t\t\t\t\t\t\t\t\t*","red"))
print(colored("*********************************************************************************","red"))

#Taking the domain and worlist as input from user
domain = input("Enter the domain to be BruteForced : ")
file_name = input("Enter Wordlist file :")
f = open(file_name, "r")		# opens the file with read only permission

print(colored("\t\t\t\t\t The Reachable directories are -  \t\t\t\t\t",'green'))

#reading the wordlist line by line
for i in f.readlines():
    url = domain+"/"+i[0:len(i)-1]
    response = requests.get(url)            # will store the response of requested web page
    if response.status_code == 200:
        print(colored(url,'yellow'))
print(colored("\t\t\t\t\t Thanks Visit Again \t\t\t\t\t",'green'))
f.close() 		# closes file
