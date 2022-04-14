import tkinter as tk
from tkinter import *
from tkinter import ttk
from turtle import heading

import unittest
from selenium.webdriver.common.keys import  Keys
from selenium import  webdriver
import  time



root = Tk()
root.geometry("700x450")
ttk.Label(root,text="documento a buscar:").place(x=350,y=0)
ttk.Entry(root,width= 50).place(x=250,y=20)
ttk.Button(root,text="Buscar").place(x=350,y=45)
t = tk.Text(root,width= 40,height=20)
t.place(x=50,y=75)
ttk.Label(root,text="palabara:").place(x=500,y=200)
ttk.Entry(root,width= 30).place(x=450,y=235)
ttk.Button(root,text="Buscar").place(x=500,y=270)
root.mainloop()

def  escraper ():
    return


