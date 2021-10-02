from ftplib import FTP
import ftplib
import tkinter
from tkinter import *


serveur = # adresse du serveur FTP
user=  # votre identifiant
code= # votre mot de passe
ftp = ftplib.FTP(serveur,user,code) # ligne quui permet la connection 
ftp.retrlines('LIST') 



root = Tk()
root.title("Py-FTP")
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nouveau", command="")
filemenu.add_command(label="Ouvrir", command="")
filemenu.add_command(label="envoyé-test", command="")
filemenu.add_command(label="Enregistre", command=(""))
filemenu.add_command(label="liste des fichies ", command="")
filemenu.add_command(label="Sortir", command=root.withdraw)


filemenu.add_separator()

menubar.add_cascade(label="menu", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)

rarmenu= Menu(menubar, tearoff=0)
menubar.add_cascade(label="py-rar",command="")
rarmenu.add_cascade(label="à propos...", command="")
 
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="à propos...", command="")
menubar.add_cascade(label="plus", menu=helpmenu)


label = Label(root,text="")
label.place(x=20,y=20)
button = Button(root,text="Connexion",command="").place(x=0,y=0)
button1 = Button(root,text="deconection",command="").place(x=0,y=25)
button1 = Button(root,text="telecharger",command="").place(x=0,y=50)
button3 = Button(root,text="+",command="").place(x=0,y=75)
button3 = Button(root,text="liste",command="").place(x=0,y=100)




root.config(menu=menubar)
root.mainloop()




