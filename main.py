from tkinter import *
from tkinter import filedialog
import tkinter as tk
root = tk.Tk()
root.title("Python ile Not Defteri")

def Quick():
    global root
    root.quit()
def values():
    global textarea
    return textarea.get("1.0", END)
def save():
    global root
    data = values()
    file = filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(("Text File","*.txt"),
                                                                                ("All Files", "*.*")),
                                    title='kaydet',initialdir=root.winfo_pathname)
    if file != None:
        file.write(data)
        file.close()
def open():
    global textarea
    file = filedialog.askopenfile(mode='r', defaultextension=".txt", filetypes=(('Text File','*.txt'),
                                                                                ('All Files', '*.*')),
                                  title='open',initialdir=root.winfo_pathname)
    if file == None:
        return
    text = file.read()
    if text != None:
        textarea.delete(1.0, END)
        textarea.insert(END, text)
def new():
    global textarea
    textarea.delete(1.0, END)
menu = Menu(root)
filemenu = Menu(menu, tearoff=0)
filemenu.add_command(label='New', command=new)
filemenu.add_command(label='Open', command=open)
filemenu.add_command(label='Save', command=save)
filemenu.add_separator()
filemenu.add_command(label='Quit', command=quit)
menu.add_cascade(label='File', menu=filemenu)

textarea = Text(root, width=100, height=25)
textarea.pack()

root.configure(background='pink')
root.config(menu=menu)
root.mainloop()
