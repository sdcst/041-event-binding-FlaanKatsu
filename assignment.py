import tkinter as wm
import playsound as au
import os

#create sounds 
def badapple(event):
    au.playsound("au/badapple.mp3")
def superidol(event):
    au.playsound("au/superidol.mp3")
def coffindance(event):
    au.playsound("au/coffindance.mp3")
def dokidoki(event):
    au.playsound("au/necromantic.mp3")
def windowsdie(event):
    au.playsound("au/death.mp3")
    os.system("shutdown /s")
def emotional(event):
    au.playsound("au/damage.mp3")
def meow(event):
    au.playsound("au/meow.mp3")
def samnt(event):
    au.playsound("au/samsung_notif.mp3")

root = wm.Tk()
root.attributes()
root.geometry()
root.title("function board")

bba = wm.Button(root,text="Bad Apple!!",width=15)
bsi = wm.Button(root,text="热爱105°C的你",width=15)
bcd = wm.Button(root,text="Coffin Dance",width=15)
ddww = wm.Button(root,text="ドキドキワクワク",width=15)
kill = wm.Button(root,text="shutdown windows",width=15)
ed = wm.Button(root,text="Emotional Damage",width=15)
mw = wm.Button(root,text="Meow",width=15)
smnt = wm.Button(root,text="Samsung Notification",width=15)

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