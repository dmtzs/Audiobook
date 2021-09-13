try:
    import PyPDF2
    import pyttsx3
    import time
except ImportError as eImp:
    print(f"Ocurrió el siguiente error de importación: {eImp}")

def ReadBook():
    textoCompleto= ""

    pdfReader= PyPDF2.PdfFileReader(open(r"C:\Users\Diego\OneDrive\Documentos\Cuentos y cosas varias\Sombra.pdf", "rb"))
    speaker= pyttsx3.init()
    speaker.setProperty("rate", 125)
    speaker.setProperty("volume", 1.0)
    

    for pageNum in range(pdfReader.numPages):
        text= pdfReader.getPage(pageNum).extractText()
        speaker.say(text)
        speaker.runAndWait()
        textoCompleto+= text

    speaker.stop()

    speaker.save_to_file(textoCompleto, "audio.mp3")
    speaker.runAndWait()

if __name__== "__main__":
    try:
        ReadBook()
    except KeyboardInterrupt:
        print("Cerrando programa porque se presionó Ctrl + C")
    except Exception as errEx:
        print(f"Ocurrió el siguiente error: {errEx}")
    finally:
        print("Finalizando programa")