<p align="center">
  <img width="200" src="https://github.com/dmtzs/Audiobook/blob/master/abimg.png" alt="logo">
  <h1 align="center" style="margin: 0 auto 0 auto;">Audiobook</h1>
  <h5 align="center" style="margin: 0 auto 0 auto;">PDF and TXT audio book with python</h5>
</p>

<p align="center">
    <img src="https://img.shields.io/github/last-commit/dmtzs/Audiobook">
    <img src="https://img.shields.io/github/issues/dmtzs/Audiobook?label=issues">
    <img src="https://img.shields.io/github/stars/dmtzs/Audiobook">
</p>

## The project
This is an desktop application in which we can read a PDF and TXT files and transform the text of these files into 
a voice that will read you all the PDF as a audiobook so if you have a tale or something like that 
it can be readed with this program.

## Installation, libraries and considerations
- For its correct installation and edition directly using code you need first python 3 installed in your computer.
- Run the next commands in order to install all libraries and run the code if you prefer to clone the repository:
<br>

In windows
```
pip install -r requirements.txt
```
```
python tkAudiolib.py
```
In linux
```
pip3 install -r requirements.txt
```
```
python3 tkAudiolib.py
```
- For creating the executable file in windows you need to execute the next command:
<br>

In linux
```
pyinstaller --noconfirm --onefile --windowed --add-data "./Audiolib.ico:." --name "AudioLibro" --icon "./Audiolib.ico" "./tkAudiolib.py"
```
In windows
```
pyinstaller --noconfirm --onefile --windowed --add-data "./Audiolib.ico;." --name "AudioLibro" --icon "./Audiolib.ico" "./tkAudiolib.py"
```
- If you dont want to use code and install anything then you might be interested in downloading directly the exe file by [clicking here](https://github.com/dmtzs/Audiobook/releases) and 
then just run the program after unziping the file.
- For some command information for the pyttsx3 library [click here](https://ichi.pro/es/construye-tu-propio-audiolibro-en-7-lineas-de-codigo-python-210934534284465)

## Documentation
The documentation is still in development but the link will be here.

## Test the application
In the releases part is one file that you can use in order to make a test with the application.
<br>
Just download that file and the executable and choose that file in order to be used in the program.
