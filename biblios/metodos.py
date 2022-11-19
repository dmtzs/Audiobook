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
    print(f"Ocurrió el siguiente ERROR de importación: {eImp}")

class extraMethods():
    def resource_path(self, relativePath: str):
        basePath= getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(basePath, relativePath)

    def commandSO(self):
        sistema= platform.system()

        if sistema== "Windows":
            return "cls", sistema
        else:
            return "clear", sistema

    def generateAudio(self, speedRateDes: int, outputname: str, spElec: str, pdftxtReader: PyPDF2, ext: str):
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

    def validateSpinEntryName(self, actName, bande):
        if actName== "":
            print("Entro aqui")
            return 0

        elif actName.isspace():
            return 0

        elif actName== "0" and bande== 1:
            return 0
        
        elif not actName.isnumeric() and bande== 1:
            return 0

        elif (actName.isnumeric()) and (bande== 1) and (len(actName)>3):
            return 0

        else:
            return 1

class funciones(extraMethods):
    sis= ""
    comm= ""
    fileName= ""
    folderName= ""
    fileIco= "Audiolib.ico"

    def __init__(self, titleApp):
        self.titleApp= titleApp

    def GUI(self):
        banderas= [0, 0, 0, 0]# Ruta al archivo seleccionado, Ruta de salida del mp3, Ratio válido, Nombre del archivo mp3 resultante
        # ----------------Otros métodos.----------------
        

        def repoGit():
            webbrowser.open("https://github.com/dmtzs/Audiobook")

        def abrirRuta():
            self.fileName= filedialog.askopenfilename()

            if len(self.fileName) > 1:
                rutaError.config(text= self.fileName, fg= "green", font= ("jost", 8))
                banderas[0]= 1
            else:
                rutaError.config(text= "Please choose a file", fg= "red", font= ("jost", 8))
                banderas[0]= 0

        def abrirRuta2():
            self.folderName= filedialog.askdirectory()

            if len(self.folderName) > 1:
                rutaError2.config(text= self.folderName, fg= "green", font= ("jost", 8))
                banderas[1]= 1
            else:
                rutaError2.config(text= "Please choose a path", fg= "red", font= ("jost", 8))
                banderas[1]= 0

        def audiobookCore():
            if banderas[0]== 0:
                messagebox.showerror("ERROR", "The path to the file shouldnt be empty or should be txt or pdf only")
            elif banderas[1]== 0:
                messagebox.showerror("ERROR", "The output path of the mp3 file shouldnt be empty")
            elif banderas[2]== 0:
                messagebox.showerror("ERROR", "The ratio of the voice shouldnt be 0 or empty and also shouldnt have letters and should be a number of three digits only")
            elif banderas[3]== 0:
                messagebox.showerror("ERROR", "The name of the output mp3 file shouldnt be empty")
            else:
                outputname= fileNameEntry.get()
                speedRateDes= int(spinVelocidad.get())
                spElec= guardCombo.get()

                _, ext= os.path.splitext(self.fileName)
                del _
                
                if ext== ".pdf":
                    pdfReader= PyPDF2.PdfFileReader(open(self.fileName, "rb"))
                    self.generateAudio(speedRateDes, outputname, spElec, pdfReader, ext)

                elif ext== ".txt":
                    with open(self.fileName, encoding= "utf8") as f:
                        txtLines = f.readlines()
                    for elem in range(len(txtLines)):
                        txtLines[elem]= txtLines[elem][:-1]
                    self.generateAudio(speedRateDes-15.4, outputname, spElec, txtLines, ext)
            
        def validateSpinRatio(*args):
            actRatio= spinVelocidad.get()

            banderas[2]= self.validateSpinEntryName(actRatio, 1)
        
        def validateEntryName(*args):
            nameFile= fileNameEntryText.get()

            banderas[3]= self.validateSpinEntryName(nameFile, 0)

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

        def languages():
            radioOp= lengVar.get()

            if radioOp== 1:
                titleLabel.config(text= "Audiobook")
                fileLabel.config(text= "Choose file to read")
                fileLabel2.config(text= "Choose path to save output file")
                saveEntry.config(text= "File")
                saveEntry2.config(text= "Path")
                velocidadLabel.config(text= "Enter speed rate of the voice:")
                fileNameLabel.config(text= "Enter the name of the mp3 file:")
                guardLabel.config(text= "Save and play or just save the audio file?:")
                applyBut.config(text= "Apply")
                labelGit.config(text= "Repository of the program:")
                butGit.config(text= "Repository")

                spinVelocidad.place(x= 240, y= 233)
                fileNameEntry.config(width= 40)
                fileNameEntry.place(x= 240, y= 273.4)
                guardCombo.config(width= 22)
                guardCombo.place(x= 330, y= 316.5)
            else:
                titleLabel.config(text= "Audiolibro")
                fileLabel.config(text= "Elige el archivo a leer")
                fileLabel2.config(text= "Elige la ruta para guardar el archivo resultante")
                saveEntry.config(text= "Archivo")
                saveEntry2.config(text= "Ruta")
                velocidadLabel.config(text= "Ingresa tasa de velocidad de la voz:")
                fileNameLabel.config(text= "Ingresa nombre del archivo mp3:")
                guardLabel.config(text= "Guardar y reproducir o solo guardar el audio?:")
                applyBut.config(text= "Aplicar")
                labelGit.config(text= "Repositorio del programa:")
                butGit.config(text= "Repositorio")

                spinVelocidad.place(x= 285, y= 233)
                fileNameEntry.config(width= 36)
                fileNameEntry.place(x= 260, y= 273.4)
                guardCombo.config(width= 18)
                guardCombo.place(x= 360, y= 316.5)
        # ----------------Componentes del frame----------------
        # ----------------Rutas----------------
        titleLabel= tk.Label(mainWin, fg= "purple", text= "Audiobook", font= ("jost", 25))
        titleLabel.place(relx= 0.5, y= 25, anchor= CENTER)

        fileLabel= tk.Label(mainWin, fg= "black", text= "Choose file to read", font= ("jost", 15))
        fileLabel.place(relx= 0.5, y= 78, anchor= CENTER)

        rutaError= tk.Label(mainWin, fg= "red", text= "Select a file", font= ("jost", 8))
        rutaError.place(x= 90, y= 102)

        saveEntry= tk.Button(mainWin, fg= "white", width= 10, bg= "#794ECF", text= "File", takefocus= False, command= abrirRuta)
        saveEntry.place(x= 10, y= 100)

        fileLabel2= tk.Label(mainWin, fg= "black", text= "Choose path to save output file", font= ("jost", 15))
        fileLabel2.place(relx= 0.5, y= 150, anchor= CENTER)

        rutaError2= tk.Label(mainWin, fg= "red", text= "Select a path", font= ("jost", 8))
        rutaError2.place(x= 90, y= 182)

        saveEntry2= tk.Button(mainWin, fg= "white", width= 10, bg= "#794ECF", text= "Path", takefocus= False, command= abrirRuta2)
        saveEntry2.place(x= 10, y= 180)

        # ----------------Resto de componentes----------------
        velocidadLabel= tk.Label(mainWin, fg= "black", text= "Enter speed rate of the voice:", font= ("jost", 13))
        velocidadLabel.place(x= 10, y= 230)

        spinVelVar= tk.StringVar()
        spinVelocidad= tk.Spinbox(mainWin, from_= 1, to= 200, width= 15, textvariable= spinVelVar)
        spinVelocidad.place(x= 240, y= 233)
        spinVelVar.trace_add("write", validateSpinRatio)
        spinVelVar.set("130")

        fileNameLabel= tk.Label(mainWin, fg= "black", text= "Enter the name of the mp3 file:", font= ("jost", 13))
        fileNameLabel.place(x= 10, y= 270)

        fileNameEntryText= tk.StringVar()
        fileNameEntry= tk.Entry(mainWin, width= 40, textvariable= fileNameEntryText)
        fileNameEntry.focus()
        fileNameEntry.place(x= 240, y= 273.4)
        fileNameEntryText.trace_add("write", validateEntryName)
        fileNameEntryText.set("output")

        guardLabel= tk.Label(mainWin, fg= "black", text= "Save and play or just save the audio file?:", font= ("jost", 13))
        guardLabel.place(x= 10, y= 315)

        valores= ["Save only", "Save and play"]
        valComb= tk.StringVar()
        valComb.set(valores[0])
        guardCombo= ttk.Combobox(mainWin, values= valores, state= "readonly", textvariable= valComb, width= 22)
        guardCombo.place(x= 330, y= 316.5)

        lengVar= tk.IntVar()
        lengVar.set(1)

        lenguajeEn= tk.Radiobutton(mainWin, text= "English", variable= lengVar, value= 1, takefocus= False, command= languages)
        lenguajeEn.place(x= 395, y= 5)

        lenguajeEs= tk.Radiobutton(mainWin, text= "Español", variable= lengVar, value= 2, takefocus= False, command= languages)
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