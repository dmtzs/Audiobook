from tkinter.constants import CENTER
from pyttsx3 import speak


try:
    import os
    import sys
    import platform
    import PyPDF2
    import pyttsx3
    import tkinter as tk
    from tkinter import ttk, filedialog, messagebox
except ImportError as eImp:
    print(f"Ocurriò el siguiente ERROR de importación: {eImp}")

class funciones():
    sis= ""
    comm= ""
    fileName= ""
    folderName= ""
    fileIco= "Audiolib.ico"
    mainWin= tk.Tk()

    def __init__(self, titleApp, mainTitleApp):
        self.titleApp= titleApp
        self.mainTitleApp= mainTitleApp

    def resource_path(self, relativePath):
        basePath= getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(basePath, relativePath)

    def commandSO(self):
        sistema= platform.system()

        if sistema== "Windows":
            return "cls", sistema
        else:
            return "clear", sistema

    def GUI(self):
        # ----------------Otros métodos.----------------
        def abrirRuta():
            self.fileName= filedialog.askopenfilename()

            if len(self.fileName) > 1:
                rutaError.config(text= self.fileName, fg= "green", font= ("jost", 8))
            else:
                rutaError.config(text= "Please choose a file", fg= "red", font= ("jost", 8))

        def abrirRuta2():
            self.folderName= filedialog.askdirectory()

            if len(self.folderName) > 1:
                rutaError2.config(text= self.folderName, fg= "green", font= ("jost", 8))
            else:
                rutaError2.config(text= "Please choose a path", fg= "red", font= ("jost", 8))

        def audiobookCore():
            speedRateDes= int(spinVelocidad.get())
            outputname= fileNameEntry.get()
            spElec= guardCombo.get()
            textoCompleto= ""

            pdfReader= PyPDF2.PdfFileReader(open(self.fileName, "rb"))
            speaker= pyttsx3.init()
            speaker.setProperty("rate", speedRateDes)
            speaker.setProperty("volume", 1.0)

            for pageNum in range(pdfReader.numPages):
                text= pdfReader.getPage(pageNum).extractText()
                textoCompleto+= text

                if spElec== "Save and play":
                    speaker.say(text)
                    speaker.runAndWait()
                else:
                    speaker.runAndWait()

            speaker.stop()

            speaker.save_to_file(textoCompleto, f"{self.folderName}/{outputname}.mp3")
            speaker.runAndWait()

        # ----------------Instrucciones de la GUI principal.----------------
        self.mainWin.title(self.titleApp)
        self.mainWin.resizable(width= False, height= False)
        try:
            imaIco= self.resource_path(self.fileIco)
            self.mainWin.iconbitmap(imaIco)
        except Exception:
            self.mainWin.iconbitmap("Audiolib.ico")
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

        # ----------------Componentes del frame----------------
        # ----------------Rutas----------------
        titleLabel= tk.Label(self.mainWin, fg= "purple", text= self.mainTitleApp, font= ("jost", 25))
        titleLabel.place(relx= 0.5, y= 25, anchor= CENTER)

        fileLabel= tk.Label(self.mainWin, fg= "black", text= "Choose file to read", font= ("jost", 15))
        fileLabel.place(relx= 0.5, y= 78, anchor= CENTER)

        rutaError= tk.Label(self.mainWin, fg= "red", text= "Select a file", font= ("jost", 8))
        rutaError.place(x= 90, y= 102)

        saveEntry= tk.Button(self.mainWin, fg= "white", width= 10, bg= "#794ECF", text= "File", command= abrirRuta)
        saveEntry.place(x= 10, y= 100)

        fileLabel= tk.Label(self.mainWin, fg= "black", text= "Choose path to save output file", font= ("jost", 15))
        fileLabel.place(relx= 0.5, y= 150, anchor= CENTER)

        rutaError2= tk.Label(self.mainWin, fg= "red", text= "Select a path", font= ("jost", 8))
        rutaError2.place(x= 90, y= 182)

        saveEntry2= tk.Button(self.mainWin, fg= "white", width= 10, bg= "#794ECF", text= "Path", command= abrirRuta2)
        saveEntry2.place(x= 10, y= 180)

        # ----------------Resto de componentes----------------
        velocidadLabel= tk.Label(self.mainWin, fg= "black", text= "Enter speed rate of the voice:", font= ("jost", 13))
        velocidadLabel.place(x= 10, y= 230)

        spinVelVar= tk.StringVar()
        spinVelVar.set("130")
        spinVelocidad= tk.Spinbox(self.mainWin, from_= 1, to= 200, width= 15, textvariable= spinVelVar)
        spinVelocidad.place(x= 240, y= 233)

        fileNameLabel= tk.Label(self.mainWin, fg= "black", text= "Enter the name of the mp3 file:", font= ("jost", 13))
        fileNameLabel.place(x= 10, y= 270)

        fileNameEntryText= tk.StringVar()
        fileNameEntryText.set("output")
        fileNameEntry= tk.Entry(self.mainWin, width= 40, textvariable= fileNameEntryText)
        fileNameEntry.place(x= 240, y= 273.4)

        guardLabel= tk.Label(self.mainWin, fg= "black", text= "Save and play or just save the audio file?:", font= ("jost", 13))
        guardLabel.place(x= 10, y= 315)

        valores= ["Save only", "Save and play"]
        valComb= tk.StringVar()
        valComb.set(valores[0])
        guardCombo= ttk.Combobox(self.mainWin, values= valores, state= "readonly", textvariable= valComb)
        guardCombo.place(x= 330, y= 316.5)

        lengVar= tk.IntVar()
        lengVar.set(1)

        lenguajeEn= tk.Radiobutton(self.mainWin, text= "English", variable= lengVar, value= 1)
        lenguajeEn.place(x= 395, y= 5)

        lenguajeEs= tk.Radiobutton(self.mainWin, text= "Español", variable= lengVar, value= 2)
        lenguajeEs.place(x= 395, y= 30)

        applyBut= tk.Button(self.mainWin, fg= "white", width= 10, bg= "#794ECF", text= "Apply", command= audiobookCore)# Aún necesitamos agregar un método para validar el formulario de la app.
        applyBut.place(x= 196, y= 370)

        self.mainWin.mainloop()