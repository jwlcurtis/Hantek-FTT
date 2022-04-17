# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 12:00:36 2020

@author: Logan
"""

import tkinter as tk
from tkinter import filedialog
from PIL import Image
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt



def Title_Set():
    global Title
    Title=str(Title_IN.get())
    Title_Label["text"]=Title
    
def dt_Set():
    global dt
    dt=str(dt_IN.get())
    dt_Label["text"]=dt
    
def File_Name_Set_Fun():
    global File_Name
    File_Name=str(File_Name_IN.get())
    File_Label["text"]=File_Name
def getBit ():
    import_file_path= filedialog.askopenfilename()
    im = Image.open(import_file_path)
    # summarize some details about the image
    border1 = (20, 55, 640, 448 ) # left, up, right, bottom
    im=im.crop(box=border1)   
    pixels = im.load()
    width, height = im.size
    x_coords = []
    y_coords=[]
    for x in range(width):
        for y in range(height):
            if pixels[x, y] == (255, 255, 0):
             x_coords.append(x)
             y_coords.append(y)
    
    delta_t = float(dt) #sec
    N = len(y_coords)
    T = delta_t/25
    x = np.linspace(0.0, N*T, N)
    xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
    N = len(y_coords)         
    yf = sp.fft.fft(y_coords)
    plt.plot(xf,2.0/N * np.abs(20*np.log(yf[0:N//2]/0.001)))
    plt.title(Title)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Intensity (dBm)')
    plt.grid()
   #plt.show()
    plt.savefig(File_Name)
    root.destroy()
                
root= tk.Tk()   
root.grid()
root.title("FFT")

Title_IN=tk.StringVar()
Title_Input=tk.Entry(root, width=15, textvariable=Title_IN)
Title_Input.grid(row=0,column=0,padx=30,pady=10)

Title_Set= tk.Button(root,text="Set Title", command= Title_Set) # Creates Title Set
Title_Set.grid(row=0,column=1,pady=10) #Places Title Set

Title_Label=tk.Label(root,text="",width= 30,relief="solid")
Title_Label.grid(row=0,column=2,pady=10)

File_Name_IN=tk.StringVar()
File_Name_Input=tk.Entry(root, width=15, textvariable=File_Name_IN)
File_Name_Input.grid(row=1,column=0,padx=30,pady=10)

File_Name_Set= tk.Button(root,text="Set File Name", command= File_Name_Set_Fun) # Creates Title Set
File_Name_Set.grid(row=1,column=1,pady=10) #Places Title Set

File_Label=tk.Label(root,text="",width= 30,relief="solid")
File_Label.grid(row=1,column=2,pady=10)

dt_IN=tk.StringVar()
dt_Input=tk.Entry(root, width=15, textvariable=dt_IN)
dt_Input.grid(row=2,column=0,padx=30,pady=10)

dt_Set= tk.Button(root,text="Set dt", command= dt_Set) # Creates Title Set
dt_Set.grid(row=2,column=1,pady=10) #Places Title Set

dt_Label=tk.Label(root,text="",width= 30,relief="solid")
dt_Label.grid(row=2,column=2,pady=10)

Open= tk.Button(root,text="    Open File    ", command= getBit) # Creates Title Set
Open.grid(row=3,column=0,pady=10) #Places Title Set
root.mainloop()