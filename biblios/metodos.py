try:
    import platform
    import os
except ImportError as eImp:
    print(f"Ocurriò el siguiente ERROR de importación: {eImp}")

class funciones():
    sis= ""
    comm= ""
    folderName= ""

    def __init__(self, mainFrame):
        self.mainWin= mainFrame

    def commandSO(self):
        sistema= platform.system()

        if sistema== "Windows":
            return "cls", sistema
        else:
            return "clear", sistema

    def configWindow(self):
        self.mainWin.title("Audiolibro")
        self.mainWin.resizable(width= False, height= False)
        self.mainWin.iconbitmap("./Audiolib.ico")
        screenWidth = self.mainWin.winfo_screenwidth()# Ancho del área de visualización
        screenHeight = self.mainWin.winfo_screenheight()# Alto del área de visualización
        self.comm, self.sis= self.commandSO()

        if self.sis== "Windows":
            width= 500
            height= 550
        else:
            width= 1000
            height= 1050
        left = (screenWidth - width) / 2
        top = (screenHeight - height) / 2
        self.mainWin.geometry(f"{int(width)}x{int(height)}+{int(left)}+{int(top)}")