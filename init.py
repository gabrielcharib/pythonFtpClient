from ftplib import FTP
import os
import ftplib
import tkinter
from tkinter import *



#ftp = ftplib.FTP(serveur,user,code) # ligne quui permet la connection 
#ftp.retrlines('LIST') 

#methode utiliser pour retouner le nom de l'utilisateur 
def recupUsernam ():
    global user
    list = os.getcwd()
    listTempo = list.split('/')
    user = listTempo[2]


def a():  
    racine0=tkinter.Tk()
    bouton0=tkinter.Button(racine0, text="Quitter", command=racine0.withdraw)  
    bouton0.pack(side=tkinter.RIGHT)
    bouton=tkinter.Button(racine0, text="licence", command="") 
    bouton.pack(side=tkinter.TOP)
    mot0=tkinter.Label(racine0, text="CHARIB FREEWARE BETA (FTP) 0.0.1.b")
    racine0.geometry("260x100")
    mot0.pack(side=tkinter.BOTTOM)
    racine0.mainloop()

def localDir():
    global directory 
    global listOfFiles
    recupUsernam()
    directory= '/users/'
    directory += user
    list = os.listdir(directory)
    listOfFiles = Listbox (mainframe,height=35,width=120)
    for i in range (len(list)) :
        listOfFiles.insert(i,list[i])
    listOfFiles.pack()


   

##attention tout ça c'est des variables locales eviter un max
root = Tk()
root.title("Py-FTP")
root.geometry('850x800')



Frame1 = Frame(root, borderwidth=2, relief=GROOVE)
Frame1.pack(side=LEFT, padx=30, pady=30)

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=1)
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
helpmenu.add_command(label="à propos...", command=a)
menubar.add_cascade(label="plus", menu=helpmenu)

#ceation de la frame de gauche 
mainframe = Frame(root, background="bisque")
mainframe.place(x=0, y=125, anchor="nw", width=385, height=460)


label = Label(root,text=" ")
label.place(x=20,y=20)
buttonConnexion = Button(root,text="Connexion",command="").place(x=0,y=0)
buttonDeconnection = Button(root,text="deconection",command="").place(x=0,y=25)
buttonTelecharger = Button(root,text="telecharger",command="").place(x=0,y=50)
button3 = Button(root,text="+",command="").place(x=0,y=75)
button4 = Button(root,text="liste",command="").place(x=0,y=100)

#mettre des chose dans la frame
labelLocal = Label(mainframe,text="local").place(x=0,y=0)

scrollbar = Scrollbar (mainframe)
scrollbar.pack(side= RIGHT , fill=Y)
#user = recupUsernam

directory = ''
user = "defaut"
listOfFiles = ''

localDir()


scrollbar.config(command=listOfFiles.yview)

root.config(menu=menubar)
root.mainloop()




