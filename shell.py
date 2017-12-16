from commandLineClassDefinitions import *
from tkinter import Tk
import tkinter.messagebox as mb
import os
import shutil

cmd = commandLine()

# Set up the commands

_ALL_ = ["cd", "newfile", "newdir", "deletedir","listfiles", "editfile", "deletefile", "newProject", "deleteProject"] 

def cd(infp):
    if len(str(infp).split("/")) > 1:
        if os.path.exists(infp):
            cmd.cd = infp
        else:
            print("FileError at command <cd>: File path must exist. To create a new directory, use the 'newdir' function")
    else:
        print("SyntaxError at command <cd>: Must be a child directory of the System code folder")
def newdir(infp1):
    if not os.path.exists(str(cmd.cd) + str(infp1)):
        os.makedirs(str(cmd.cd) + str((infp1)))
    else:
        print("FileError at command <newdir>: File already exists")
def deletedir(fname):
    if os.path.exists(str(cmd.cd) + str(fname)):
        ddir = Tk()
        if mb.askyesno  == True:
            shutil.rmtree(str(cmd.cd) + fname)
    print("FileError at command <deletedir>: Folder not found. Use 'newdir' to create a folder")
def listfiles(self):
    f = []
    for (dirpath, dirnames, filenames) in os.walk(cmd.cd):
        print(f.extend(filenames))
def newfile(nfin):
    _=open(str(cmd.cd) + nfin, "w")
    _.close()
def editfile(ftbep, text):
    ft = open(str(cmd.cd) + ftbep, "a")
    ft.write(str(text))
def deletefile(fname):
    e=open(str(cmd.cd) + fname)
    ddir = Tk()
    if mb.askyesno  == True:
        os.remove(str(cmd.cd) + fname)
    print("FileError at command <deletefile>: File not found. Use 'newfile' to create a file")
def newProject():
    return None
def deleteProject():
    return None

# Set up the command loop

while True:
    ucmd = input(cmd.cd + ">")
    if ucmd.upper() == "STOP":
        break
    elif ucmd.upper() == "CD":
        cdin = input("cd>")
        cd(cdin)
    elif ucmd.upper() == "NEWDIR":
        ndin = input("newdir>")
        newdir(ndin)
    elif ucmd.upper() == "DELETEDIR":
        ddin = input("deletedir>")
        deletedir(ddin)
    elif ucmd.upper() == "LISTFILES":
        listfiles()
    elif ucmd.upper() == "NEWFILE":
        nffn = input("newfile>")
        newfile(nffn)
    elif ucmd.upper() == "EDITFILE":
        fn = input("editfile> /filename ")
        fnt = input("editfile> /text ")
        editfile(fn, fnt)
    elif ucmd.upper() == "DELETEFILE":
        fnd = input("deletefile>")
        deletefile(fnd)
    elif ucmd.upper() == "PYTHON":
        pye = input("python> ")
        exec(str(pye))
