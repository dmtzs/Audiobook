try:
    import tkinter as tk
    from tkinter import ttk, filedialog
    from biblios import metodos
except ImportError as eImp:
    print(f"Ocurrió el siguiente error de importación: {eImp}")

fileName= ""

# Otros métodos
def abrirRuta():
    global fileName

    fileName= filedialog.askopenfilename()

    if len(fileName) > 1:
        rutaError.config(text= fileName, fg= "green", font= ("jost", 8))
    else:
        rutaError.config(text= "Please choose a path", fg= "red", font= ("jost", 8))

# Declaración de frame principal
mainWin= tk.Tk()

# Instancia de la clase dentro de bilbios
met= metodos.funciones(mainWin)

# Inicialización de configuración de frame principal de tkinter
met.configWindow()

# Componentes del frame
titleLabel= tk.Label(mainWin, fg= "purple", text= "PDF Audiobook", font= ("jost", 25))
titleLabel.place(x= 130, y= 5)

fileLabel= tk.Label(mainWin, fg= "black", text= "Choose file to read", font= ("jost", 15))
fileLabel.place(x= 160, y= 68)

saveEntry= tk.Button(mainWin, fg= "white", width= 10, bg= "#794ECF", text= "Path", command= abrirRuta)
saveEntry.place(x= 10, y= 100)

rutaError= tk.Label(mainWin, fg= "red", text= "Select a file", font= ("jost", 8))
rutaError.place(x= 90, y= 102)

velocidadLabel= tk.Label(mainWin, fg= "black", text= "Enter speed rate of the voice:", font= ("jost", 13))
velocidadLabel.place(x= 10, y= 140)

spinVelVar= tk.StringVar()
spinVelVar.set("125")
spinVelocidad= tk.Spinbox(mainWin, from_= 1, to= 200, width= 15, textvariable= spinVelVar)
spinVelocidad.place(x= 240, y= 143)

fileNameLabel= tk.Label(mainWin, fg= "black", text= "Enter the name of the mp3 file:", font= ("jost", 13))
fileNameLabel.place(x= 10, y= 180)

fileNameEntryText= tk.StringVar()
fileNameEntryText.set("output")
fileNameEntry= tk.Entry(mainWin, width= 40, textvariable= fileNameEntryText)
fileNameEntry.place(x= 240, y= 183.4)

guardLabel= tk.Label(mainWin, fg= "black", text= "Save and play or just save the audio file?:", font= ("jost", 13))
guardLabel.place(x= 10, y= 225)

valores= ["Save only", "Save and play"]
valComb= tk.StringVar()
valComb.set(valores[0])
guardCombo= ttk.Combobox(mainWin, values= valores, state= "readonly", textvariable= valComb)
guardCombo.place(x= 330, y= 226.5)

lengVar= tk.IntVar()
lengVar.set(1)

lenguajeEn= tk.Radiobutton(mainWin, text= "English", variable= lengVar, value= 1)
lenguajeEn.place(x= 395, y= 15)

lenguajeEs= tk.Radiobutton(mainWin, text= "Español", variable= lengVar, value= 2)
lenguajeEs.place(x= 395, y= 40)

applyBut= tk.Button(mainWin, fg= "white", width= 10, bg= "#794ECF", text= "Apply")# Aún necesitamos agregar un método para validar el formulario de la app.
applyBut.place(x= 196, y= 280)

mainWin.mainloop()