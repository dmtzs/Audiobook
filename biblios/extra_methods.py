try:
    import os
    import sys
    import pyttsx3
    import platform
    from tkinter import messagebox
except ImportError as e_imp:
    print(f"Ocurrió el siguiente ERROR de importación en el archivo {__file__}: {e_imp}")

class ExtraMethods():
    def resource_path(self, relativePath: str) -> str:
        basePath= getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(basePath, relativePath)

    def commandSO(self) -> tuple[str, str]:
        sistema= platform.system()

        if sistema== "Windows":
            return "cls", sistema
        else:
            return "clear", sistema

    def generate_audio(self, speed_rate_des: int, outputname: str, spElec: str, pdf_txt_reader, ext: str) -> None:
        try:
            speaker= pyttsx3.init()
            speaker.setProperty("rate", speed_rate_des)
            speaker.setProperty("volume", 1.0)

            if ext== ".pdf":
                textoCompleto= ""

                for pageNum in range(pdf_txt_reader.numPages):
                    text= pdf_txt_reader.getPage(pageNum).extractText()
                    textoCompleto+= text

                    if spElec== "Save and play":
                        speaker.say(text)
                        speaker.runAndWait()
                    else:
                        speaker.runAndWait()

                speaker.stop()

                speaker.save_to_file(textoCompleto, f"{self.folder_name}/{outputname}.mp3")
                speaker.runAndWait()
            else:
                if spElec== "Save and play":
                    speaker.say(pdf_txt_reader)
                    speaker.runAndWait()
                else:
                    speaker.runAndWait()

                speaker.stop()

                speaker.save_to_file(pdf_txt_reader, f"{self.folder_name}/{outputname}.mp3")
                speaker.runAndWait()

            messagebox.showinfo("Éxito", "File converted in audio format with success!!")

        except Exception:
            messagebox.showerror("ERROR", "Something failed at the moment we try to reads the file, be sure that is a PDF or TXT file")

    def validate_spin_entry_name(self, act_name: str, bande: int) -> int:
        if act_name== "":
            print("Entro aqui")
            return 0

        elif act_name.isspace():
            return 0

        elif act_name == "0" and bande== 1:
            return 0
        
        elif not act_name.isnumeric() and bande== 1:
            return 0

        elif (act_name.isnumeric()) and (bande== 1) and (len(act_name)>3):
            return 0

        else:
            return 1