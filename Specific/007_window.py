from itertools import count, cycle
from tkinter import *
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk
import os

def shut_down():
    os.system("shutdown /s /t 0")
    root.destroy()

def restart():
    os.system("shutdown /r /t 1")
    root.destroy()

def sleep():
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    root.destroy()

class ImageLabel(ctk.CTkLabel):
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        frames = []
        self.place_configure(x=120, y=50, anchor='nw')
        try:
            for i in count(1):
                frames.append(ImageTk.PhotoImage(im.copy().resize((500,450), Image.Resampling.LANCZOS)))
                im.seek(i)
        except EOFError:
            pass
        self.frames = cycle(frames)

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(frames) == 1:
            self.configure(image=next(self.frames))
        else:
            self.next_frame()

    def unload(self):
        self.configure(image=None)
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.configure(image=next(self.frames))
            self.after(self.delay, self.next_frame)

#demo :
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
root = ctk.CTk()
root.geometry("800x470+450+160")
wid = 800
hgt = 470
root.title("Shut Down Windows")
root.iconbitmap(os.path.join( os.getcwd(), r"Specific\panda.ico" ))
root.resizable(False,False)
my_can=Canvas(root , width=wid , height=hgt, bg="black", highlightbackground="white" ,highlightthickness=2)
my_can.pack( fill="both", expand=True)
img_1 = Image.open(os.path.join( os.getcwd(), r"Specific\panda_background.jpg" ))
pht_1 = ImageTk.PhotoImage(img_1.resize((1000,588), Image.Resampling.LANCZOS))
my_can.create_image( 0, 0 , image=pht_1 , anchor="nw")
lbl = ImageLabel(my_can)
lbl.pack()
lbl.load(os.path.join( os.getcwd(), r"Specific\animation.gif"))

shut = ctk.CTkButton(master=root, text="Shut Down", text_font=("Berlin Sans FB",20), width=150, height=20, corner_radius=10,
         text_color="white", fg_color="#520ccf", hover_color="#854bff", bg_color="#f2cdff", command = shut_down)
shut_win = my_can.create_window(750 , 250 , anchor="nw" , window=shut )

res = ctk.CTkButton(master=root, text="Restart", text_font=("Berlin Sans FB",20), width=153, height=20, corner_radius=10,
         text_color="white", fg_color="#7024de", hover_color="#b050e8", bg_color="#f2cdff", command=restart)
res_win = my_can.create_window(750 , 310 , anchor="nw" , window=res )

slp = ctk.CTkButton(master=root, text="Sleep", text_font=("Berlin Sans FB",20), width=153, height=20, corner_radius=10,
        text_color="white", fg_color="#264bc8", hover_color="#5e5fd3", bg_color="#f2cdff", command=sleep)
slp_win = my_can.create_window(750 , 370 , anchor="nw" , window=slp )

root.mainloop()
