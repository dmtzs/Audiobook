try:
    from biblios import methods
except ImportError as eImp:
    print(f"Ocurrió el siguiente error de importación: {eImp}")

# Llamada a programa principal
if __name__== "__main__":
    title_app= "Audiobook app"

    try:
        # Llamadas a la GUI y los métodos
        met= methods.Funciones(title_app)
        met.GUI()
    except KeyboardInterrupt:
        print("Se presionó Ctrl + C")
    except Exception as ex:
        print(f"Ocurrió el siguiente ERROR: {ex}")
    finally:
        print("Finalizando programa")