# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 12:07:37 2023

@author: Ankan Datta
"""

from tkinter import *
from tkinter import filedialog
import os
from PIL import ImageTk, Image
from tkinter import messagebox
import webbrowser


root = Tk()
root.title("HTML IDE")
root.minsize(650, 650)
root.maxsize(650, 650)

open_image = ImageTk.PhotoImage(Image.open("open.png"))
save_image = ImageTk.PhotoImage(Image.open("save.png"))
live = ImageTk.PhotoImage(Image.open("arrow_left.png"))

file_label = Label(root, text = "FILE NAME")
file_label.place(relx = 0.5, rely = 0.02, anchor=CENTER)

file_input = Entry(root)
file_input.place(relx = 0.7, rely = 0.02, anchor=CENTER)

note_text = Text(root, height = 35, width = 80, bg = "grey")
note_text.place(relx = 0.5, rely = 0.5, anchor=CENTER)


name = ""

def openFile(): 
    global name
    note_text.delete(1.0, END)
    file_input.delete(0, END)
    html_file = filedialog.askopenfilename(title = "Open text file", filetypes = (("HTML file", "*.html"), ))
    print(html_file)
    name = os.path.basename(html_file)
    formated_name = name.split('.')[0]
    file_input.insert(END, formated_name)
    root.title(formated_name)
    html_file = open(name, 'r')
    paragraph = text_file.read
    note_text.insert(END, paragraph)
    html_file.close
    
def save_file():
    input_name = file_input.get()
    file = open(input_name + ".html", "w")
    data = note_text.get("1.0", END)
    print(data)
    file.write(data)
    file_input.delete(0,END)
    note_text.delete(1.0, END)
    messagebox.showinfo("Update", "Your file has been saved!")
    
def live_view():
    global name
    webbrowser.open_new_tab(name)
    
    
button1 = Button(root, text = "Open File", image = open_image, command = openFile)
button1.place(relx = 0.03, rely = 0.01)

button2 = Button(root, text = "Save File", image = save_image, command = save_file)
button2.place(relx = 0.09, rely = 0.01)

button3 = Button(root, text = "Start Live", image = live, command = live_view)
button3.place(relx = 0.15, rely = 0.01)

root.mainloop()