import socket
from colorama import Fore, Back, Style
#s.settimeout(5)
print(Back.BLACK+Fore.RED+"-"*100)
print(Back.BLACK+Fore.GREEN+"\t\t\t\t Welcome to Basic Port Scanner \t\t\t\t\t")
print(Back.BLACK+Fore.RED+"-"*100)
print(Style.RESET_ALL)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
target = input("Enter the IP you to be scanned: ")
print("port  state")
for port in range(3304,3308):
    if s.connect_ex((target, port)):
        print(Fore.CYAN+"{}  closed".format(port))
    else:
        print(Fore.LIGHTMAGENTA_EX+"{}  open".format(port))
print(Style.RESET_ALL)