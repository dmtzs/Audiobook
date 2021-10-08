try:
    import os
    import sys
    import platform
    import PyPDF2
    import pyttsx3
    import webbrowser
    import tkinter as tk
    from tkinter.constants import CENTER
    from tkinter import ttk, filedialog, messagebox
except ImportError as eImp:
    print(f"Ocurriò el siguiente ERROR de importación: {eImp}")

class extraMethods():
    def resource_path(self, relativePath):
        basePath= getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(basePath, relativePath)

    def commandSO(self):
        sistema= platform.system()

        if sistema== "Windows":
            return "cls", sistema
        else:
            return "clear", sistema

    def generateAudio(self, speedRateDes, outputname, spElec, pdftxtReader, ext):
        try:
            speaker= pyttsx3.init()
            speaker.setProperty("rate", speedRateDes)
            speaker.setProperty("volume", 1.0)

            if ext== ".pdf":
                textoCompleto= ""

                for pageNum in range(pdftxtReader.numPages):
                    text= pdftxtReader.getPage(pageNum).extractText()
                    textoCompleto+= text

                    if spElec== "Save and play":
                        speaker.say(text)
                        speaker.runAndWait()
                    else:
                        speaker.runAndWait()

                speaker.stop()

                speaker.save_to_file(textoCompleto, f"{self.folderName}/{outputname}.mp3")
                speaker.runAndWait()
            else:
                if spElec== "Save and play":
                    speaker.say(pdftxtReader)
                    speaker.runAndWait()
                else:
                    speaker.runAndWait()

                speaker.stop()

                speaker.save_to_file(pdftxtReader, f"{self.folderName}/{outputname}.mp3")
                speaker.runAndWait()

            messagebox.showinfo("Éxito", "File converted in audio format with success!!")

        except Exception:
            messagebox.showerror("ERROR", "Something failed at the moment we try to reads the file, be sure that is a PDF or TXT file")

    def messageDialog(self, nameFile):
        if nameFile== "":
            messagebox.showerror("ERROR", "The name of the file shouldn´t be empty")

            return 1
        else:
            return 0

class funciones(extraMethods):
    sis= ""
    comm= ""
    fileName= ""
    folderName= ""
    fileIco= "Audiolib.ico"

    def __init__(self, titleApp, mainTitleApp):
        self.titleApp= titleApp
        self.mainTitleApp= mainTitleApp

    def GUI(self):
        # ----------------Otros métodos.----------------
        def repoGit():
            webbrowser.open("https://github.com/dmtzs/Audiobook")

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
            outputname= fileNameEntry.get()
            speedRateDes= int(spinVelocidad.get())
            spElec= guardCombo.get()

            _, ext= os.path.splitext(self.fileName)

            if ext== ".pdf":
                pdfReader= PyPDF2.PdfFileReader(open(self.fileName, "rb"))
                self.generateAudio(speedRateDes, outputname, spElec, pdfReader, ext)

            elif ext== ".txt":
                with open(self.fileName, encoding= "utf8") as f:
                    txtLines = f.readlines()
                for elem in range(len(txtLines)):
                    txtLines[elem]= txtLines[elem][:-1]
                self.generateAudio(speedRateDes-15.4, outputname, spElec, txtLines, ext)

            else:
                messagebox.showerror("ERROR", "You should select only TXT and/or PDF files")

        def validateEntryName(*args):
            nameFile= fileNameEntry.get()

            self.messageDialog(nameFile)

        # ----------------Instrucciones de la GUI principal.----------------
        mainWin= tk.Tk()
        mainWin.title(self.titleApp)
        mainWin.resizable(width= False, height= False)
        try:
            imaIco= self.resource_path(self.fileIco)
            mainWin.iconbitmap(imaIco)
        except Exception:
            mainWin.iconbitmap("Audiolib.ico")
        screenWidth = mainWin.winfo_screenwidth()# Ancho del área de visualización
        screenHeight = mainWin.winfo_screenheight()# Alto del área de visualización
        self.comm, self.sis= self.commandSO()

        if self.sis== "Windows":
            width= 500
            height= 550
        else:
            width= 1000
            height= 1050
        left = (screenWidth - width) / 2
        top = (screenHeight - height) / 2
        mainWin.geometry(f"{int(width)}x{int(height)}+{int(left)}+{int(top)}")

        # ----------------Componentes del frame----------------
        # ----------------Rutas----------------
        titleLabel= tk.Label(mainWin, fg= "purple", text= self.mainTitleApp, font= ("jost", 25))
        titleLabel.place(relx= 0.5, y= 25, anchor= CENTER)

        fileLabel= tk.Label(mainWin, fg= "black", text= "Choose file to read", font= ("jost", 15))
        fileLabel.place(relx= 0.5, y= 78, anchor= CENTER)

        rutaError= tk.Label(mainWin, fg= "red", text= "Select a file", font= ("jost", 8))
        rutaError.place(x= 90, y= 102)

        saveEntry= tk.Button(mainWin, fg= "white", width= 10, bg= "#794ECF", text= "File", takefocus= False, command= abrirRuta)
        saveEntry.place(x= 10, y= 100)

        fileLabel= tk.Label(mainWin, fg= "black", text= "Choose path to save output file", font= ("jost", 15))
        fileLabel.place(relx= 0.5, y= 150, anchor= CENTER)

        rutaError2= tk.Label(mainWin, fg= "red", text= "Select a path", font= ("jost", 8))
        rutaError2.place(x= 90, y= 182)

        saveEntry2= tk.Button(mainWin, fg= "white", width= 10, bg= "#794ECF", text= "Path", takefocus= False, command= abrirRuta2)
        saveEntry2.place(x= 10, y= 180)

        # ----------------Resto de componentes----------------
        velocidadLabel= tk.Label(mainWin, fg= "black", text= "Enter speed rate of the voice:", font= ("jost", 13))
        velocidadLabel.place(x= 10, y= 230)

        spinVelVar= tk.StringVar()
        spinVelVar.set("130")
        spinVelocidad= tk.Spinbox(mainWin, from_= 1, to= 200, width= 15, textvariable= spinVelVar)
        spinVelocidad.place(x= 240, y= 233)

        fileNameLabel= tk.Label(mainWin, fg= "black", text= "Enter the name of the mp3 file:", font= ("jost", 13))
        fileNameLabel.place(x= 10, y= 270)

        fileNameEntryText= tk.StringVar()
        fileNameEntryText.set("output")
        fileNameEntry= tk.Entry(mainWin, width= 40, textvariable= fileNameEntryText)
        fileNameEntry.focus()
        fileNameEntry.place(x= 240, y= 273.4)
        fileNameEntryText.trace_add("write", validateEntryName)

        guardLabel= tk.Label(mainWin, fg= "black", text= "Save and play or just save the audio file?:", font= ("jost", 13))
        guardLabel.place(x= 10, y= 315)

        valores= ["Save only", "Save and play"]
        valComb= tk.StringVar()
        valComb.set(valores[0])
        guardCombo= ttk.Combobox(mainWin, values= valores, state= "readonly", textvariable= valComb)
        guardCombo.place(x= 330, y= 316.5)

        lengVar= tk.IntVar()
        lengVar.set(1)

        lenguajeEn= tk.Radiobutton(mainWin, text= "English", variable= lengVar, value= 1, takefocus= False)
        lenguajeEn.place(x= 395, y= 5)

        lenguajeEs= tk.Radiobutton(mainWin, text= "Español", variable= lengVar, value= 2, takefocus= False)
        lenguajeEs.place(x= 395, y= 30)

        applyBut= tk.Button(mainWin, fg= "white", width= 10, bg= "#794ECF", text= "Apply", takefocus= False, command= audiobookCore)# Aún necesitamos agregar un método para validar el formulario de la app.
        applyBut.place(x= 196, y= 370)

        # Label to github repository
        labelGit= tk.Label(mainWin, text= "Repository of the program:", font= ("jost", 10))
        labelGit.place(x= 130, y= 525)

        # Button to repository
        butGit= tk.Button(mainWin, width= 10, bg= "#794ECF", fg= "white", text= "Repository", takefocus= False, command= repoGit)
        butGit.place(x= 290, y= 523)


        mainWin.mainloop()