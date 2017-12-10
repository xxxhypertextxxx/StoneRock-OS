class commandLine():
    """
        The command line class can be avoided, but makes things easier for readibility and management.
        It will not contain functions, but will have variables.
        variable descriptions:
            cd: Current working directory. The default is "UNDEFINED/bin/". There has to be at least one parent directory, but it cannot be the directory with the system code.
            UDM: User-Defined-Moduals. These python based moduals are imported automaticly on run of the Command Line.  To use the python code inside, or python code in genaral, use exec then type the python code.
            AIM: Automaticly-Imported-Moduals. These built-in python moduals are immported automaticly on run of the Command Line.  To use the python code inside, or python code in genaral, use exec then type the python code.
    """
    def __init__(self):
        self.cd = "UNDEFINED/bin/"
        self.UDM = []
        self.AIM = []
        
if __name__ == '__main__':
    cmdtest = commandLine()
    print(cmdtest.cd)
    print(cmdtest.UDM)
    print(cmdtest.AIM)
