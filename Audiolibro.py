try:
    import PyPDF2
    import pyttsx3
    import time
except ImportError as eImp:
    print(f"Ocurrió el siguiente error de importación: {eImp}")

def ReadBook():
    pdfReader= PyPDF2.PdfFileReader(open(r"C:\Users\Diego\OneDrive\Documentos\Cuentos y cosas varias\sombra.pdf", "rb"))
    speaker= pyttsx3.init()
    rate= speaker.getProperty("rate")
    print(rate)
    time.sleep(100)

    for pageNum in range(pdfReader.numPages):
        text= pdfReader.getPage(pageNum).extractText()
        speaker.say(text)
        speaker.runAndWait()

    speaker.stop()

    speaker.save_to_file(text, "audio.mp3")
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