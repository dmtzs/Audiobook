try:
    import platform
    import tkinter as tk
    from biblios import metodos
    from tkinter import ttk
    from tkinter import filedialog
except ImportError as eImp:
    print(f"Ocurrió el error: {eImp}")

fileName= ""
# Declaration of the main frame
mainWin= tk.Tk()

# Other methods
def abrirRuta():
    global fileName

    fileName= filedialog.askopenfilename()

    if len(fileName) > 1:
        rutaError.config(text= fileName, fg= "green", font= ("jost", 8))
    else:
        rutaError.config(text= "Por favor elije una ruta", fg= "red", font= ("jost", 8))

# Instance of the class
met= metodos.funciones(mainWin)

# Initializing main frame components
met.configWindow()

# Title of the application
titleLabel= tk.Label(mainWin, fg= "purple", text= "Audiobook application", font= ("jost", 25))
titleLabel.place(x= 90, y= 5)

# Components for the selected file
fileLabel= tk.Label(mainWin, fg= "black", text= "Choose file to read", font= ("jost", 15))
fileLabel.place(x= 160, y= 68)

saveEntry= tk.Button(mainWin, width= 10, bg= "#1DC90F", fg= "white", text= "Ruta", command= abrirRuta)
saveEntry.place(x= 10, y= 100)

rutaError= tk.Label(mainWin, text= "Selecciona archivo", fg= "red", font= ("jost", 8))
rutaError.place(x= 90, y= 102)

# Components for the speed rate of the voice
velocidadLabel= tk.Label(mainWin, fg= "black", text= "Enter speed rate of the voice:", font= ("jost", 13))
velocidadLabel.place(x= 10, y= 140)

spinVelVar= tk.StringVar()
spinVelVar.set("125")
spinVelocidad= tk.Spinbox(mainWin, from_= 0, to= 200, width= 15, textvariable= spinVelVar)
spinVelocidad.place(x= 240, y= 143)

# Components for writing the name of the result file
fileNameLabel= tk.Label(mainWin, fg= "black", text= "Enter the name of the mp3 file:", font= ("jost", 13))
fileNameLabel.place(x= 10, y= 180)

fileNameEntryText= tk.StringVar()
fileNameEntryText.set("output")
fileNameEntry= tk.Entry(mainWin, width= 40, textvariable= fileNameEntryText)
fileNameEntry.place(x= 240, y= 183.4)

# Components for the action we want to perform, saving and playing the audio file or just saving the audio file
guardLabel= tk.Label(mainWin, fg= "black", text= "Save and play or just save the audio file?:", font= ("jost", 13))
guardLabel.place(x= 10, y= 225)

valores= ["Save and play", "Save only"]
guardCombo= ttk.Combobox(mainWin, values= valores, state= "readonly")
guardCombo.place(x= 330, y= 226.5)

mainWin.mainloop()