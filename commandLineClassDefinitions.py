import tkinter as tk

class commandLine():
    """
        The command line class can be avoided, but makes things easier for readibility and management.
        It will not contain functions, but will have variables. UNDER ONE EXCEPTION:
            It will have functions for creating StoneRock-Projects.
        variable descriptions:
            cd: Current working directory. The default is "UNDEFINED/". There has to be at least one parent directory, but it cannot be the directory with the system code.
            
    """
    def __init__(self):
        self.cd = "UNDEFINED/"
        self_ALLCOMMANDS_ = ["cd", "newfile", "newdir", "deletedir","listfiles", "editfile", "deletefile", "newProject", "deleteProject"] 
"""
class projectGui():
    def __init__(self):
        super(projectCore)
        def cfpg():
            _=open(str(self.newfileE.get),"r")
            _.close()
        self.root = tk.Tk()
        self.newfileB = tk.Button(self.root, text="Create File", command=lambda:cfpg()).pack()
        self.newfileE = tk.Entry(self.root)
        self.newfileE.pack()
        self.root.mainloop()
class projectCore():
  "" This is the core class for Projects  ""
    def __init__(self):
        self.defaultProjectPath = "PROJECTS/"
        self.gui = projectGui()
        
    def startgui(self):
        pgui = projectGui()
"""
if __name__ == '__main__':
    cmdtest = commandLine()
    print("\"" + cmdtest.cd + "\"   :   commandLine.")

