import threading
from tkinter import *
from PIL import ImageTk,Image
import requests
from math import *
import keyboard

# Importing The Modules#

labels = []

API_KEY = 'a7e402d0-3fa4-49d0-a966-3a93145e2a60'

def fetch(url):
    r = requests.get(url)
    data = r.json()
    return data

def drawscoreboard(name,apikey,window,y):
    uuid = fetch(f'https://api.mojang.com/users/profiles/minecraft/{name}')
    uuid = uuid['id']
    hyapi = fetch(f'https://api.hypixel.net/player?key={apikey}&uuid={uuid}')
    losses = hyapi['player']['stats']['Bedwars']["losses_bedwars"]
    wins = hyapi['player']['stats']['Bedwars']["wins_bedwars"]
    level = (hyapi['player']['achievements']['bedwars_level'])
    stat3 = (hyapi['player']['stats']["Bedwars"]["final_kills_bedwars"])
    stat6 = (hyapi['player']['stats']["Bedwars"]["final_deaths_bedwars"])
    Fkdr = stat3 / stat6
    Fkdr = round(Fkdr, 3 - int(floor(log10(abs(Fkdr)))) - 1)
    Fkdr = str(Fkdr)
    scoreboard = Label(window,text=f'{name}                  {level}                  {Fkdr}                   {wins}                   {losses}',font=('Josefin Sans', 16), bg='gray').place(x=0, y=y)
    labels.append(scoreboard)




nw = Tk() # Creating The Window

def settings():
    root = Tk()


def overlay():
    count = 150
    path = r'C:\Users\User\.lunarclient\offline\1.8\logs\latest.log'
    while True:
        with open(path) as file:
            lines = file.readlines()
            for line in lines:
                if 'ONLINE:' in line:
                    for i in line.split():
                        try:
                            if i.replace(',', '') != 'oTrojang':
                                drawscoreboard(i.replace(',', ''),API_KEY,nw,count)
                                open(path, 'w').close()
                                count += 50
                        except:
                            pass
                if 'joined (' in line:
                    for i in line.split():
                        try:
                            print(count)
                            if i.replace(',', '') != 'oTrojang':
                                drawscoreboard(i.replace(',', ''), API_KEY, nw, count)
                                open(path, 'w').close()
                                count += 50
                        except:
                            pass

def ov():
    t = threading.Thread(target=overlay).start()

def move(event):
    x, y = nw.winfo_pointerxy()
    nw.geometry(f"+{x}+{y}")

def keylisten():
    while True:
        if keyboard.is_pressed('G'):
            print(labels)

def keys():
    t = threading.Thread(target=keylisten).start()



nw.geometry('800x500') # Changing The Size Of The Window
nw.title('NightWare Overlay')
nw.wm_attributes('-alpha',0.5)
nw.configure(bg='gray')
nw.wm_attributes("-topmost", 1)
nw.overrideredirect(1)
nw.bind('<B1-Motion>',move)
titlebar = ImageTk.PhotoImage(image=Image.open('titlebar.png'))
bar = Label(nw,image=titlebar,bg='#404040').place(x=0,y=0)


scoreboard = Label(nw,text='Name                  Star                  FKDR                   Wins                   Losses',font=('Josefin Sans',16),bg='gray').place(x=0,y=100)

nw.after(0,ov)
nw.after(0,keys)
mainloop()
