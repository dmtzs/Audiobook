try:
    import platform
    import tkinter as tk
    from biblios import metodos
    from tkinter import ttk
    from tkinter import filedialog
except ImportError as eImp:
    print(f"Ocurrió el error: {eImp}")

mainWin= tk.Tk()
met= metodos.funciones(mainWin)
met.configWindow()

mainWin.mainloop()