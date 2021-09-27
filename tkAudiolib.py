try:
    from biblios import metodos
except ImportError as eImp:
    print(f"Ocurrió el siguiente error de importación: {eImp}")

# Llamada a programa principal
if __name__== "__main__":
    mainTitleApp= "Audiobook"
    titleApp= "Audiobook app"

    try:
        # Llamadas a la GUI
        met= metodos.funciones(titleApp, mainTitleApp)
        met.GUI()
    except KeyboardInterrupt:
        print("Se presionó Ctrl + C")
    except Exception as ex:
        print(f"Ocurrió el siguiente ERROR: {ex}")
    finally:
        print("Finalizando programa")