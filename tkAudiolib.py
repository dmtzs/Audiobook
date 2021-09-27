try:
    from biblios import metodos
except ImportError as eImp:
    print(f"Ocurrió el siguiente error de importación: {eImp}")

# Llamada a programa principal
if __name__== "__main__":
    mainTitleApp= "Audiobook"
    titleApp= "Audiobook app"

    # Instancia de la clase dentro de bilbios
    met= metodos.funciones(titleApp, mainTitleApp)
    
    met.GUI()