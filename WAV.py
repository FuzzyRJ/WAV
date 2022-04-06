import ctypes
ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 0 )
import tkinter as tk
import speech_recognition as sr
import os
import pyttsx3
import webbrowser
from tkinter.ttk import Label
from tkinter import *
import pyautogui
from pywinauto import application
from datetime import date
from datetime import datetime
trueoffalse = True
app =  application.Application()
recognizer = sr.Recognizer()
window = tk.Tk()
window.geometry("250x60+1350+0")
window.configure(bg='lightgray')
window.resizable(False, False)
window.attributes('-topmost', 1)
window.attributes('-alpha',0.8)
window.overrideredirect(trueoffalse)
window.title("WAV")

#docks app to left side of the screen
def left():
    pyautogui.keyDown("win")
    pyautogui.press("Left")
    pyautogui.keyUp("win")

#docks app to right side of the screen
def right():
    pyautogui.keyDown("win")
    pyautogui.press("Right")
    pyautogui.keyUp("win")

#Maximises one app
def maximise():
    pyautogui.keyDown("altleft")
    pyautogui.keyDown("space")
    pyautogui.press("x")
    pyautogui.keyUp("space")
    pyautogui.keyUp("altleft")

def up():
    pyautogui.keyDown("win")
    pyautogui.press("Up")
    pyautogui.keyUp("win")

#restores app
def down():
    pyautogui.keyDown("win")
    pyautogui.press("Down")
    pyautogui.keyUp("win")

#docks app to top left side of the screen
def upleft():
    pyautogui.keyDown("win")
    pyautogui.press("Left")
    pyautogui.press("Left")
    pyautogui.press("Up")
    pyautogui.keyUp("win")

#docks app to top left side of the screen
def upright():
    pyautogui.keyDown("win")
    pyautogui.press("Right")
    pyautogui.press("Right")
    pyautogui.press("Up")
    pyautogui.keyUp("win")

#docks app to bottom left side of the screen
def bottomleft():
    pyautogui.keyDown("win")
    pyautogui.press("Left")
    pyautogui.press("Left")
    pyautogui.press("Down")
    pyautogui.keyUp("win")

#docks app to bottom right side of the screen
def bottomright():
    pyautogui.keyDown("win")
    pyautogui.press("Right")
    pyautogui.press("Right")
    pyautogui.press("Down")
    pyautogui.keyUp("win")

#minimizes all apps 
def minall():
    pyautogui.keyDown("win")
    pyautogui.press("d")
    pyautogui.keyUp("win")

#minimizes one app
def minone():
    pyautogui.keyDown("altleft")
    pyautogui.keyDown("space")
    pyautogui.press("n")
    pyautogui.keyUp("space")
    pyautogui.keyUp("altleft")

#restores all apps to previous look
def restore():
    pyautogui.keyDown("win")
    pyautogui.keyDown("shift")
    pyautogui.press("m")
    pyautogui.keyUp("win")
    pyautogui.keyUp("shift")

speechOnOff = 0
strlabel = "Off"
strtext = "Say Intro or Introduction"

#changes the lables on the GUI
#and sets speeckOnOff to 1
#so it can go into the function speechReck()
def button(value1):
    strlabel = "Listening...                          "
    label = tk.Label(window, bg="lightgray", text=strlabel)
    label.place(x=70,y=8)
    global speechOnOff
    speechOnOff = value1
    window.update()

def speechReck():
    count = 0
    countforsaves = 0
    repeaterYesNo = 0
    textedsaid = []
    savedtext = []
    recognizer = sr.Recognizer()
    while speechOnOff == 1:
        window.update()
        try:
            with sr.Microphone() as source:   
                audio = recognizer.listen(source, phrase_time_limit=4)
                window.update()
        except:
            strlabel = "No microphone detected     "
            label = tk.Label(window, bg="lightgray", text=strlabel)
            label.place(x=70,y=10)
            btn_on.configure(bg="gray")
            break
        try:
            text = recognizer.recognize_google(audio)
            textedsaid.append(text)
            strtext = "You said: " + text + "                                   "
            label2 = tk.Label(window, bg="lightgray", text=strtext)
            label2.place(x=70,y=28)
            window.update()
            text = str(text.lower())

            #opens the instructions 
            if "intro" in text:
                dirname = os.path.dirname(__file__)
                file = "instructions.txt"
                location = (dirname + "\\" + file)
                os.startfile(location)

            elif "lock" in text:
                #the GUI will unlock from its position so you can move it around
                if "un" in text:
                    trueoffalse = False
                    window.overrideredirect(trueoffalse)
                    window.update()
                #the GUI will lock back to the position it started at
                else:
                    trueoffalse = True
                    window.overrideredirect(trueoffalse)
                    window.attributes('-topmost', 1)
                    window.attributes('-alpha',0.8)
                    window.geometry("250x60+1350+0")
                    window.update()

            elif "repeat" in text or "repeating" in text:
                #stops repeating everything you say
                if "stop" in text:
                    repeaterYesNo = 0
                #repeats the previous thing you said 
                elif "that" in text and count > 0:
                    engine = pyttsx3.init()
                    engine.say(textedsaid[count-1])
                    engine.runAndWait()
                #alows the program to repeat everything you say
                else:
                    repeaterYesNo = 1

            #repeats everything you say if activated
            elif repeaterYesNo == 1:
                engine = pyttsx3.init()
                engine.say(text)
                engine.runAndWait()
            
            #reads out the saves 
            elif "save" in text:
                if "1" in text or "one" in text:
                    engine = pyttsx3.init()
                    engine.say(savedtext[0])
                    engine.runAndWait()

                elif "2" in text or "two" in text:
                    engine = pyttsx3.init()
                    engine.say(savedtext[1])
                    engine.runAndWait()
                    
                elif "3" in text or "three" in text:
                    engine = pyttsx3.init()
                    engine.say(savedtext[2])
                    engine.runAndWait()
                    
                elif "4" in text or "four" in text:
                    engine = pyttsx3.init()
                    engine.say(savedtext[3])
                    engine.runAndWait()
                    
                elif "5" in text or "five" in text:
                    engine = pyttsx3.init()
                    engine.say(savedtext[4])
                    engine.runAndWait()
                    
                elif "6" in text or "six" in text:
                    engine = pyttsx3.init()
                    engine.say(savedtext[5])
                    engine.runAndWait()
                    
                elif "7" in text or "seven" in text:
                    engine = pyttsx3.init()
                    engine.say(savedtext[6])
                    engine.runAndWait()
                    
                elif "8" in text or "eight" in text:
                    engine = pyttsx3.init()
                    engine.say(savedtext[7])
                    engine.runAndWait()
                    
                elif "9" in text or "nine" in text:
                    engine = pyttsx3.init()
                    engine.say(savedtext[8])
                    engine.runAndWait()
                    
                elif "10" in text or "ten" in text:
                    engine = pyttsx3.init()
                    engine.say(savedtext[9])
                    engine.runAndWait()

                elif "read" in text or "play" in text:
                    for i in range(countforsaves):
                        engine = pyttsx3.init()
                        engine.say(savedtext[i])
                        engine.runAndWait()
                #saves the previous text said
                elif count > 0:
                    savedtext.append(textedsaid[count-1])
                    countforsaves += 1
                #doesn't save if no previous text is said
                elif count == 0:
                    strtext = "need prior input"
                    label2 = tk.Label(window, bg="lightgray", text=strtext)
                    label2.place(x=70,y=28)
            
            elif "open schoology" in text:
                engine = pyttsx3.init()
                engine.say("opening schoology")
                engine.runAndWait()
                webbrowser.open('https://app.schoology.com/login')

            #google searches what you say
            elif "google" in text:
                text = text.replace("google ", "")
                webbrowser.open("https://www.google.com/search?q=" + text) 
                
            elif "dock" in text or "doc" in text:
                if "left" in text:
                    if "upper" in text or "top" in text:
                        maximise()
                        upleft()
                    elif "lower" in text or "bottom" in text:
                        maximise()
                        bottomleft()
                    else:
                        maximise()
                        left()

                elif "right" in text:
                    if "upper" in text or "top" in text:
                        maximise()
                        upright()
                    elif "lower" in text or "bottom" in text:
                        maximise()
                        bottomright()
                    else:
                        maximise()
                        right()

            elif "up" in text or "maximize" in text:
                maximise()

            elif "shrink" in text:
                down()

            elif "minimize" in text:
                if "all" in text:
                    minall()
                else:
                    minone()

            elif "restore" in text:
                restore()

            elif "open g drive" in text:
                os.system("start G:\\")
        
            elif "open file explorer" in text:
                app.start("Quick access")

            #opens what every app is on your hotbar
            elif "hotbar" in text or "hot bar" in text:
                if "one" in text or "1" in text:
                    pyautogui.hotkey("win", "1")

                elif "two" in text or "2" in text:
                    pyautogui.hotkey("win", "2")

                elif "three" in text or "3" in text:
                    pyautogui.hotkey("win", "3")

                elif "four" in text or "4" in text:
                    pyautogui.hotkey("win", "4")

                elif "five" in text or "5" in text:
                    pyautogui.hotkey("win", "5")

                elif "six" in text or "6" in text:
                    pyautogui.hotkey("win", "6")

                elif "seven" in text or "7" in text:
                    pyautogui.hotkey("win", "7")

                elif "eight" in text or "8" in text:
                    pyautogui.hotkey("win", "9")

                elif "nine" in text or "9" in text:
                    pyautogui.hotkey("win", "9")

                elif "ten" in text or "10" in text:
                    pyautogui.hotkey("win", "0")

            elif "task view" in text or "task switcher" in text:
                pyautogui.hotkey("ctrl", "alt", "tab")

            elif "close window" in text:
                pyautogui.hotkey("alt", "F4")

            elif "task manager" in text:
                pyautogui.hotkey("ctrl", "shift", "esc")

            elif "tab" in text:
                if "reopen" in text:
                    pyautogui.hotkey("ctrl", "shift", "t")
                    
                elif "open" in text:
                    pyautogui.hotkey("ctrl", "t")

                elif "close" in text:
                    pyautogui.hotkey("ctrl", "w")

            elif "game bar" in text:
                pyautogui.hotkey("win", "g")

            elif "calculator" in text:
                if "open" in text:
                    engine = pyttsx3.init()
                    engine.say("opening calculator")
                    engine.runAndWait()
                    os.startfile("calc.exe")

                elif "close" in text:
                    engine = pyttsx3.init()
                    engine.say("closing calculator")
                    engine.runAndWait()
                    os.system("TASKKILL /F /IM calculator.exe")

            elif "firefox" in text:
                if "open" in text:
                    engine = pyttsx3.init()
                    engine.say("opening Firefox")
                    engine.runAndWait()
                    os.startfile("firefox.exe")

                elif "close" in text:
                    engine = pyttsx3.init()
                    engine.say("closing Firefox")
                    engine.runAndWait()
                    os.system("TASKKILL /F /IM firefox.exe")
                    
            elif "chrome" in text:
                if "open" in text:
                    engine = pyttsx3.init()
                    engine.say("opening Chrome")
                    engine.runAndWait()
                    os.startfile("chrome.exe")

                elif "close" in text:
                    engine = pyttsx3.init()
                    engine.say("closing Chrome")
                    engine.runAndWait()
                    os.system("TASKKILL /F /IM chrome.exe")

            elif "edge" in text:
                if "open" in text:
                    engine = pyttsx3.init()
                    engine.say("opening edge")
                    engine.runAndWait()
                    os.startfile("msedge.exe")

                elif "close" in text:
                    engine = pyttsx3.init()
                    engine.say("closing edge")
                    engine.runAndWait()
                    os.system("TASKKILL /F /IM msedge.exe")

            elif "visual studio" in text:
                if "code" in text:
                    if "open" in text:
                        engine = pyttsx3.init()
                        engine.say("opening visual studio code")
                        engine.runAndWait()
                        os.startfile("G:\Microsoft VS Code\Visual Studio Code.lnk")
                    elif "close" in text:
                        engine = pyttsx3.init()
                        engine.say("closing visual studio code")
                        engine.runAndWait()
                        os.startfile("TASKKILL /F /IM Code.exe")
                else:
                    if "open" in text:
                        engine = pyttsx3.init()
                        engine.say("opening visual studio")
                        engine.runAndWait()
                        os.startfile("C:\Program Files (x86)\Microsoft Visual Studio\\2017\Professional\Common7\IDE\devenv.exe")

                    elif "close" in text:
                        engine = pyttsx3.init()
                        engine.say("closing visual studio")
                        engine.runAndWait()
                        os.system("TASKKILL /F /IM devenv.exe")

            elif "word" in text:
                if "open word" in text:
                    engine = pyttsx3.init()
                    engine.say("opening Word")
                    engine.runAndWait()
                    os.startfile("WINWORD.EXE")

                elif "close word" in text:
                    engine = pyttsx3.init()
                    engine.say("closing Word")
                    engine.runAndWait()
                    os.system("TASKKILL /F /IM WINWORD.EXE")

            elif "excel" in text:
                if "open excel" in text:
                    engine = pyttsx3.init()
                    engine.say("opening Excel")
                    engine.runAndWait()
                    os.startfile("EXCEL.EXE")

                elif "close excel" in text:
                    engine = pyttsx3.init()
                    engine.say("closing Excel")
                    engine.runAndWait()
                    os.system("TASKKILL /F /IM EXCEL.EXE")

            elif "access" in text:
                if "open access" in text:
                    engine = pyttsx3.init()
                    engine.say("opening Access")
                    engine.runAndWait()
                    os.startfile("MSACCESS.EXE")

                elif "close access" in text:
                    engine = pyttsx3.init()
                    engine.say("closing Access")
                    engine.runAndWait()                
                    os.system("TASKKILL /F /IM MSACCESS.EXE")

            elif "powerpoint" in text:
                if "open powerpoint" in text:
                    engine = pyttsx3.init()
                    engine.say("opening Power Point")
                    engine.runAndWait()
                    os.startfile("POWERPNT.EXE")

                elif "close powerpoint" in text:
                    engine = pyttsx3.init()
                    engine.say("closing Power Point")
                    engine.runAndWait()
                    os.system("TASKKILL /F /IM POWERPNT.EXE")
            
            elif "date" in text or "time" in text:
                if "date and time" in text:
                    now = datetime.now()
                    dt_string = now.strftime("%B %d %Y, %X")
                    engine = pyttsx3.init()
                    engine.say(dt_string)
                    engine.runAndWait()            

                elif "date" in text:
                    today = date.today()
                    d2 = today.strftime("%B %d %Y")
                    engine = pyttsx3.init()
                    engine.say(d2)
                    engine.runAndWait()      

                else:
                    now = datetime.now()
                    dt_string = now.strftime("%X")
                    engine = pyttsx3.init()
                    engine.say(dt_string)
                    engine.runAndWait()
            
            elif "stop listening" in text or "cancel" in text:
                strlabel = "Off                          "
                label = tk.Label(window, bg="lightgray", text=strlabel)
                label.place(x=70,y=10)
                btn_on.configure(bg="gray")
                break

            count += 1
        except:
            strtext = "Could not understand audio           "
            label2 = tk.Label(window, bg="lightgray", text=strtext)
            label2.place(x=70,y=28)

#closes the GUI
def close():
    window.quit()
    window.update()

#gets the location for the microphone image for the butten
dirname2 = os.path.dirname(__file__)
file2 = "Microphone.png"
location2 = (dirname2 + "\\" + file2)
click_btn= PhotoImage(file=location2)

#puts the microphone image on the button 
img_label= Label(image=click_btn)

#creates the on button
btn_on = Button(window, image=click_btn, command=lambda: [button(1),speechReck()], height = 50, width = 55, borderwidth=0)
btn_on.place(x=2,y=4)

#creates the closes button
btn_close = Button(window, text="X",command=close, activebackground = "red", bg="lightgray", height = 1, width = 2)
btn_close.place(x=225,y=0)

#label for the status of the speechReck()
label = Label(window, bg="lightgray", text=strlabel)
label.place(x=70,y=8)

#label for what you say and errors
label2 = Label(window, bg="lightgray", text=strtext)
label2.place(x=70,y=28)

window.mainloop()