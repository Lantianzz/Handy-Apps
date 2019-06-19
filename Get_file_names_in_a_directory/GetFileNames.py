# -*- coding: utf-8 -*-
r"""
Created on Fri Nov 24 21:38:04 2017

@author: _Lantian


Instructions for pyinstaller:

after install pyinstaller using pip install,
    use pyinstaller.exe from ...\Scripts the same way as we use pip install
    and type -F path after the exe (-F means put all info into one exe)
Example: pyinstaller.exe -F E:\xxxx

Then we can find our exe file inn ...\Scripts\dist
"""

import os
import csv
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def walk(dirname):
    """
    This function is from a book called Think Python 
    written by Allen B. Downey.

    It walks through a directory, gets names of all files
    and calls itself recursively on all the directories
    """
    file_list=[]
    for name in os.listdir(dirname):
        path=os.path.join(dirname,name)
        if os.path.isfile(path):
            file_list.append(path)
        else:
            walk(path)
    return file_list            

def save_csv(file,target_list):
    """write list into csv.
    argument newline must be used, 
    or there will be empty lines between every two lines of codes"""
    csvFile=open(file,'w', newline='',encoding='utf_8_sig') 
    writer=csv.writer(csvFile)
    for i in range(len(target_list)):
        writer.writerow(target_list[i])
    csvFile.close()

def write_list(dirname):
    
    file_list = walk(dirname)
    #split the folder names and file names into different columns
    lists=[item.split('\\') for item in file_list] 

    #write data into csv files
    save_csv(dirname+r'\file_names.csv',lists)

def get_path():
    dirname=name.get()
    write_list(dirname)
    messagebox.showinfo(title='Succeed',message='output is in:'+dirname)
    

#GUI

win=tk.Tk()
#add a title
win.title('For Maggie: Put file names in a directory into csv')
#add a label
ttk.Label(win,text=r'Enter path (example: E:\programs\files)'
          ).grid(column=0,row=0)
#add a text box entry widget
name=tk.StringVar()
name_entered=ttk.Entry(win,width=70,textvariable=name)
name_entered.grid(column=1,row=0)
#add a click button
action=ttk.Button(win,text='Run',command=get_path)
action.grid(column=0,row=2)
#place cursor
name_entered.focus() 
#start GUI
win.mainloop()

