#impotar librerias
from socket import TCP_QUICKACK
import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
import os
import re
from tkinter import font
from matplotlib.pyplot import text  
from yaml import load
import fitz
from googlesearch import search
import wget

def  pdf_text(ruta):
      texto = ""
      t.delete(0,END)
      documento = fitz.open(ruta)
      for i  in range( documento.pageCount):
         pagina  = documento.loadPage(i)
         texto = texto + pagina.getText() 
      
      lista = list(texto)
      num = 0
      x  = 0
      y = 40

      while  num <  len(lista):
         num = num + 40
         a = lista[x:y]
         cadena = " ".join(a)
         t.insert(END,(cadena))
         t.insert(END,("\n"))
         x = x + 40
         y = y +40

    
def get_value():
   e_text=Buscador.get() + ".pdf"
   results = search(e_text)
   for r in results:
       link = r
       var = os.path.exists("/home/ricardo/Documentos/proyecto_Automatas/miarchivo.pdf")  
       if (var == True): 
            os.remove("/home/ricardo/Documentos/proyecto_Automatas/miarchivo.pdf")
       wget.download(link,"/home/ricardo/Documentos/proyecto_Automatas/miarchivo.pdf")
       ruta = "/home/ricardo/Documentos/proyecto_Automatas/miarchivo.pdf"
       y = pdf_text(ruta)            #<---- llamada a la  funcion pdf_text 
       if (r  == r):
           break
   print (link)

def ExpresionR():
      ruta = "/home/ricardo/Documentos/proyecto_Automatas/miarchivo.pdf"
      texto = ""
      documento = fitz.open(ruta)
      for i  in range( documento.pageCount):
         pagina  = documento.loadPage(i)
         texto = texto + pagina.getText() 
      getText = str(Palabra.get())
      if re.search(r'^[a-zA-ZÀ-ÿ\u00f1\u00d1]+$',getText):
         patron = re.compile(getText)
         fa = patron.findall(texto)
         x = str(len(fa))
         y = ttk.Label(root, text="el nùmero de palabras encontradas es:"+ x, background="#525E75" ,foreground="#F1DDBF").place(x=480,y=330)
      else:
         y = ttk.Label(root, text="***********palabra invalida***********" ,background="#525E75",foreground="#F1DDBF").place(x=480,y=330)

# interfaz
root = tk.Tk()
root.geometry("770x500")
root.configure(background="#525E75")
tk.Label(root,text="Buscador web: ",font=("Arial",16),bg="#525E75",fg="#F1DDBF").place(x=340,y=0)
Buscador = tk.StringVar()
tk.Entry(root, textvariable=Buscador ,width= 50).place(x=230,y=25)
tk.Button(root,text="Buscar" , font=("Arial",16),bg="#92BA92" ,command= get_value ).place(x=350,y=45)
t = Listbox(root ,width= 60,height=30)
t.place(x=50,y=90)
tk.Label(root,text=" Palabra:",font=("Arial",16),fg="#F1DDBF",bg="#525E75").place(x=550,y=200)
Palabra = tk.StringVar()
ttk.Entry(root,textvariable= Palabra ,width= 30).place(x=500,y=235)
tk.Button(root,text="Buscar",font=("Arial",14),bg="#92BA92",command=ExpresionR ).place(x=550,y=260)
root.mainloop()
