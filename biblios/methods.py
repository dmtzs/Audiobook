try:
    import os
    import PyPDF2
    import webbrowser
    import tkinter as tk
    from . import extra_methods
    from tkinter.constants import CENTER
    from tkinter import ttk, filedialog, messagebox
except ImportError as eImp:
    print(f"Ocurrió el siguiente ERROR de importación: {eImp}")


class Funciones(extra_methods.ExtraMethods):
    sis= ""
    comm= ""
    file_name= ""
    folder_name= ""
    file_ico= "Audiolib.ico"

    def __init__(self, title_app):
        self.title_app= title_app

    def GUI(self) -> None:
        banderas= [0, 0, 0, 0]# Ruta al archivo seleccionado, Ruta de salida del mp3, Ratio válido, Nombre del archivo mp3 resultante
        # ----------------Otros métodos.----------------
        

        def repo_git() -> None:
            webbrowser.open("https://github.com/dmtzs/Audiobook")

        def open_route() -> None:
            self.file_name= filedialog.askopenfilename()

            if len(self.file_name) > 1:
                ruta_error.config(text= self.file_name, fg= "green", font= ("jost", 8))
                banderas[0]= 1
            else:
                ruta_error.config(text= "Please choose a file", fg= "red", font= ("jost", 8))
                banderas[0]= 0

        def open_route2() -> None:
            self.folder_name= filedialog.askdirectory()

            if len(self.folder_name) > 1:
                ruta_error2.config(text= self.folder_name, fg= "green", font= ("jost", 8))
                banderas[1]= 1
            else:
                ruta_error2.config(text= "Please choose a path", fg= "red", font= ("jost", 8))
                banderas[1]= 0

        def audiobook_core() -> None:
            if banderas[0]== 0:
                messagebox.showerror("ERROR", "The path to the file shouldnt be empty or should be txt or pdf only")
            elif banderas[1]== 0:
                messagebox.showerror("ERROR", "The output path of the mp3 file shouldnt be empty")
            elif banderas[2]== 0:
                messagebox.showerror("ERROR", "The ratio of the voice shouldnt be 0 or empty and also shouldnt have letters and should be a number of three digits only")
            elif banderas[3]== 0:
                messagebox.showerror("ERROR", "The name of the output mp3 file shouldnt be empty")
            else:
                outputname= file_nameEntry.get()
                speedRateDes= int(spin_velocidad.get())
                spElec= guard_comb.get()

                _, ext= os.path.splitext(self.file_name)
                del _
                
                if ext== ".pdf":
                    pdfReader= PyPDF2.PdfFileReader(open(self.file_name, "rb"))
                    self.generate_audio(speedRateDes, outputname, spElec, pdfReader, ext)

                elif ext== ".txt":
                    with open(self.file_name, encoding= "utf8") as f:
                        txtLines = f.readlines()
                    for elem in range(len(txtLines)):
                        txtLines[elem]= txtLines[elem][:-1]
                    self.generate_audio(speedRateDes-15.4, outputname, spElec, txtLines, ext)
            
        def validate_spin_ratio(*args):
            actRatio= spin_velocidad.get()

            banderas[2]= self.validate_spin_entry_name(actRatio, 1)
        
        def validate_entry_name(*args):
            nameFile= file_nameEntryText.get()

            banderas[3]= self.validate_spin_entry_name(nameFile, 0)

        # ----------------Instrucciones de la GUI principal.----------------
        main_win= tk.Tk()
        main_win.title(self.title_app)
        main_win.resizable(width= False, height= False)
        try:
            imaIco= self.resource_path(self.file_ico)
            main_win.iconbitmap(imaIco)
        except Exception:
            main_win.iconbitmap("Audiolib.ico")
        screenWidth = main_win.winfo_screenwidth()# Ancho del área de visualización
        screenHeight = main_win.winfo_screenheight()# Alto del área de visualización
        self.comm, self.sis= self.commandSO()

        if self.sis== "Windows":
            width= 500
            height= 550
        else:
            width= 1000
            height= 1050
        left = (screenWidth - width) / 2
        top = (screenHeight - height) / 2
        main_win.geometry(f"{int(width)}x{int(height)}+{int(left)}+{int(top)}")

        def languages():
            radioOp= leng_var.get()

            if radioOp== 1:
                title_label.config(text= "Audiobook")
                file_label.config(text= "Choose file to read")
                file_label2.config(text= "Choose path to save output file")
                save_entry.config(text= "File")
                save_entry2.config(text= "Path")
                velocidad_label.config(text= "Enter speed rate of the voice:")
                file_nameLabel.config(text= "Enter the name of the mp3 file:")
                guardLabel.config(text= "Save and play or just save the audio file?:")
                apply_but.config(text= "Apply")
                label_git.config(text= "Repository of the program:")
                but_git.config(text= "Repository")

                spin_velocidad.place(x= 240, y= 233)
                file_nameEntry.config(width= 40)
                file_nameEntry.place(x= 240, y= 273.4)
                guard_comb.config(width= 22)
                guard_comb.place(x= 330, y= 316.5)
            else:
                title_label.config(text= "Audiolibro")
                file_label.config(text= "Elige el archivo a leer")
                file_label2.config(text= "Elige la ruta para guardar el archivo resultante")
                save_entry.config(text= "Archivo")
                save_entry2.config(text= "Ruta")
                velocidad_label.config(text= "Ingresa tasa de velocidad de la voz:")
                file_nameLabel.config(text= "Ingresa nombre del archivo mp3:")
                guardLabel.config(text= "Guardar y reproducir o solo guardar el audio?:")
                apply_but.config(text= "Aplicar")
                label_git.config(text= "Repositorio del programa:")
                but_git.config(text= "Repositorio")

                spin_velocidad.place(x= 285, y= 233)
                file_nameEntry.config(width= 36)
                file_nameEntry.place(x= 260, y= 273.4)
                guard_comb.config(width= 18)
                guard_comb.place(x= 360, y= 316.5)
        # ----------------Componentes del frame----------------
        # ----------------Rutas----------------
        title_label = tk.Label(main_win, fg= "purple", text= "Audiobook", font= ("jost", 25))
        title_label.place(relx= 0.5, y= 25, anchor= CENTER)

        file_label = tk.Label(main_win, fg= "black", text= "Choose file to read", font= ("jost", 15))
        file_label.place(relx= 0.5, y= 78, anchor= CENTER)

        ruta_error= tk.Label(main_win, fg= "red", text= "Select a file", font= ("jost", 8))
        ruta_error.place(x= 90, y= 102)

        save_entry = tk.Button(main_win, fg= "white", width= 10, bg= "#794ECF", text= "File", takefocus= False, command= open_route)
        save_entry.place(x= 10, y= 100)

        file_label2= tk.Label(main_win, fg= "black", text= "Choose path to save output file", font= ("jost", 15))
        file_label2.place(relx= 0.5, y= 150, anchor= CENTER)

        ruta_error2= tk.Label(main_win, fg= "red", text= "Select a path", font= ("jost", 8))
        ruta_error2.place(x= 90, y= 182)

        save_entry2= tk.Button(main_win, fg= "white", width= 10, bg= "#794ECF", text= "Path", takefocus= False, command= open_route2)
        save_entry2.place(x= 10, y= 180)

        # ----------------Resto de componentes----------------
        velocidad_label = tk.Label(main_win, fg= "black", text= "Enter speed rate of the voice:", font= ("jost", 13))
        velocidad_label.place(x= 10, y= 230)

        spin_vel_var = tk.StringVar()
        spin_velocidad= tk.Spinbox(main_win, from_= 1, to= 200, width= 15, textvariable= spin_vel_var)
        spin_velocidad.place(x= 240, y= 233)
        spin_vel_var.trace_add("write", validate_spin_ratio)
        spin_vel_var.set("130")

        file_nameLabel= tk.Label(main_win, fg= "black", text= "Enter the name of the mp3 file:", font= ("jost", 13))
        file_nameLabel.place(x= 10, y= 270)

        file_nameEntryText= tk.StringVar()
        file_nameEntry= tk.Entry(main_win, width= 40, textvariable= file_nameEntryText)
        file_nameEntry.focus()
        file_nameEntry.place(x= 240, y= 273.4)
        file_nameEntryText.trace_add("write", validate_entry_name)
        file_nameEntryText.set("output")

        guardLabel= tk.Label(main_win, fg= "black", text= "Save and play or just save the audio file?:", font= ("jost", 13))
        guardLabel.place(x= 10, y= 315)

        valores= ["Save only", "Save and play"]
        val_comb = tk.StringVar()
        val_comb.set(valores[0])
        guard_comb= ttk.Combobox(main_win, values= valores, state= "readonly", textvariable= val_comb, width= 22)
        guard_comb.place(x= 330, y= 316.5)

        leng_var = tk.IntVar()
        leng_var.set(1)

        lenguaje_en = tk.Radiobutton(main_win, text= "English", variable= leng_var, value= 1, takefocus= False, command= languages)
        lenguaje_en.place(x= 395, y= 5)

        lenguaje_es = tk.Radiobutton(main_win, text= "Español", variable= leng_var, value= 2, takefocus= False, command= languages)
        lenguaje_es.place(x= 395, y= 30)

        apply_but = tk.Button(main_win, fg= "white", width= 10, bg= "#794ECF", text= "Apply", takefocus= False, command= audiobook_core)# Aún necesitamos agregar un método para validar el formulario de la app.
        apply_but.place(x= 196, y= 370)

        # Label to github repository
        label_git = tk.Label(main_win, text= "Repository of the program:", font= ("jost", 10))
        label_git.place(x= 130, y= 525)

        # Button to repository
        but_git = tk.Button(main_win, width= 10, bg= "#794ECF", fg= "white", text= "Repository", takefocus= False, command= repo_git)
        but_git.place(x= 290, y= 523)


        main_win.mainloop()