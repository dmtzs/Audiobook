try:
    import platform
    import tkinter as tk
    from biblios import metodos
    from tkinter import ttk
    from tkinter import filedialog
except ImportError as eImp:
    print(f"Ocurrió el error: {eImp}")

mainWin= tk.Tk()
mainWin.title("Audiolibro")
mainWin.resizable(width= False, height= False)
mainWin.iconbitmap("./Audiolib.ico")
screenWidth = mainWin.winfo_screenwidth()# Ancho del área de visualización
screenHeight = mainWin.winfo_screenheight()# Alto del área de visualización
sistema= platform.system()

if sistema== "Windows":
    width= 400
    height= 450
else:
    width= 1000
    height= 1050
left = (screenWidth - width) / 2
top = (screenHeight - height) / 2
mainWin.geometry(f"{int(width)}x{int(height)}+{int(left)}+{int(top)}")
mainWin.mainloop()