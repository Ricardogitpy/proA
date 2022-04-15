import tkinter as tk
from tkinter import *
from tkinter import ttk
from turtle import heading
import os
import re  
from yaml import load
import fitz
from googlesearch import search
import wget


def  pdf_text(ruta):
      texto = ""
      
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
       y = pdf_text(ruta)
       if (r  == r):
           break
   print (link)

def ExpresionR():
      print("si funciono")
      ruta = "/home/ricardo/Documentos/proyecto_Automatas/miarchivo.pdf"
      texto = ""
      documento = fitz.open(ruta)
      for i  in range( documento.pageCount):
         pagina  = documento.loadPage(i)
         texto = texto + pagina.getText() 
      getText = str(Palabra.get())
      if re.search(r'^[a-zA-Z]+$',getText):
        # Validacion para que se ingrese solo una palabra usando una ER para detectar espacios.
          if re.search(r'[ ]',getText):
             y = ttk.Label(root, text="palabra invalida").place(x=550,y=300)
          else:
             patron = re.compile(getText)
             fa = patron.findall(texto)
             x = str(len(fa))
             y = ttk.Label(root, text="el numero de palabras encontradas es:"+x).place(x=480,y=300)
      else:
         y = ttk.Label(root, text="palabra invalida").place(x=550,y=300)



root = Tk()
root.geometry("770x450")
ttk.Label(root,text="documento a buscar:").place(x=350,y=0)
Buscador = tk.StringVar()
ttk.Entry(root, textvariable=Buscador ,width= 50).place(x=250,y=20)
ttk.Button(root,text="Buscar", command= get_value ).place(x=350,y=45)
t = Listbox(root ,width= 60,height=30)
t.place(x=50,y=75)
ttk.Label(root,text="palabra:").place(x=550,y=200)
Palabra = tk.StringVar()
ttk.Entry(root,textvariable= Palabra ,width= 30).place(x=480,y=235)
ttk.Button(root,text="Buscar",command=ExpresionR ).place(x=550,y=270)
root.mainloop()