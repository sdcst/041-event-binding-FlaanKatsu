import tkinter as wm
import playsound as au
import os
from tkinter import *

#create sounds 
def badapple(event):
    au.playsound("au/badapple.mp3",block=False)
def superidol(event):
    au.playsound("au/superidol.mp3",block=False)
def coffindance(event):
    au.playsound("au/coffindance.mp3",block=False)
def dokidoki(event):
    au.playsound("au/necromantic.mp3",block=False)
def windowsdie(event):
    au.playsound("au/death.mp3")
    os.system("shutdown /s")
def emotional(event):
    au.playsound("au/damage.mp3",block=False)
def meow(event):
    au.playsound("au/meow.mp3",block=False)
def samnt(event):
    au.playsound("au/samsung_notif.mp3",block=False)

root = wm.Tk()
root.attributes()
root.resizable(False,False)
root.geometry()
root.title("function board")
root.iconphoto(False,PhotoImage(file="img/icon.png"))

superidolpng = PhotoImage(file="img/superidol.png")
dokiwakupng = PhotoImage(file="img/dokidokiwakuwaku.png")
coffinpng = PhotoImage(file="img/coffin.png")
badapplepng = PhotoImage(file="img/badapple.png")
scratchpng = PhotoImage(file="img/scratch.png")
damagepng = PhotoImage(file="img/damage.png")
smagsmugpng = PhotoImage(file="img/smagsmug.png")

bba = wm.Button(root,image=badapplepng,)
bsi = wm.Button(root,image=superidolpng)
bcd = wm.Button(root,image=coffinpng)
ddww = wm.Button(root,image=dokiwakupng)
kill = wm.Button(root,text="shutdown windows",width=15)
ed = wm.Button(root,image=damagepng)
mw = wm.Button(root,image=scratchpng)
smnt = wm.Button(root,image=smagsmugpng)
                 
txt曲 = wm.Label(root,text="Songs")
txtsfx = wm.Label(root,text="SFX")
txtfn = wm.Label(root,text="System Functions")
txtなし = wm.Label(root,text=" ")

txt曲.grid(row=1,column=1)
txtなし.grid(row=2,column=1)
bba.grid(row=3,column=1)
bsi.grid(row=4,column=1)
bcd.grid(row=5,column=1)
ddww.grid(row=6,column=1)

txtsfx.grid(row=1,column=2)
ed.grid(row=3,column=2)
mw.grid(row=4,column=2)
smnt.grid(row=5,column=2)

txtfn.grid(row=1,column=3)
kill.grid(row=3,column=3)

bba.bind("<Button>",badapple)
bsi.bind("<Button>",superidol)
bcd.bind("<Button>",coffindance)
ddww.bind("<Button>",dokidoki)

ed.bind("<Button>",emotional)
mw.bind("<Button>",meow)
smnt.bind("<Button>",samnt)

kill.bind("<Button>",windowsdie)

root.mainloop()