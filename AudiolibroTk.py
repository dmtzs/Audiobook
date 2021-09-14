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

# Methods
def abrirRuta():
    global fileName

    fileName= filedialog.askopenfilename()

    if len(fileName) > 1:
        rutaError.config(text= fileName, fg= "green", font= ("jost", 8))
    else:
        rutaError.config(text= "Por favor elije una ruta", fg= "red", font= ("jost", 8))

# Instance of the class
met= metodos.funciones(mainWin)

# Initializing frame components
met.configWindow()

titleLabel= tk.Label(mainWin, fg= "purple", text= "Audiobook application", font= ("jost", 25))
titleLabel.place(x= 90, y= 5)

fileLabel= tk.Label(mainWin, fg= "black", text= "Choose file to read", font= ("jost", 15))
fileLabel.place(x= 160, y= 68)

saveEntry= tk.Button(mainWin, width= 10, bg= "#1DC90F", fg= "white", text= "Ruta", command= abrirRuta)
saveEntry.place(x= 10, y= 100)

rutaError= tk.Label(mainWin, text= "Selecciona archivo", fg= "red", font= ("jost", 8))
rutaError.place(x= 90, y= 102)

mainWin.mainloop()