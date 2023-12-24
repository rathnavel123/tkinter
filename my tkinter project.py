import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os



m=Tk()
m.title('Text to speech')
m.geometry('900x500+200+200')
m.resizable(0,0)
m.configure(bg='purple')


engine=pyttsx3.init()

def speaknow():
    text = text_area.get(1.0,END)
    gender = gender_box.get()
    speed = speed_box.get()
    voices =engine.getProperty('voices')

    def setvoice():
        if (gender == 'Male'):
            engine.setProperty('voice',voices[0].id)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty('voice',voices[1].id)
            engine.say(text)
            engine.runAndWait()
            
    if (text):
            if (speed == 'Fast'):
                engine.setProperty('rate',250)
                setvoice()
            elif (speed == 'Normal'):
                engine.setProperty('rate',150)
                setvoice()
            else:
                engine.setProperty('rate',60)
                setvoice()

def download():
    text = text_area.get(1.0,END)
    gender = gender_box.get()
    speed = speed_box.get()
    voices =engine.getProperty('voices')

    def setvoice():
        if (gender == 'Male'):
            engine.setProperty('voice',voices[0].id)
            path = filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text ,'text.mp3')
            engine.runAndWait()
        else:
            engine.setProperty('voice',voices[1].id)
            path = filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text ,'text.mp3')
            engine.runAndWait()
            
    if (text):
            if (speed == 'Fast'):
                engine.setProperty('rate',250)
                setvoice()
            elif (speed == 'Normal'):
                engine.setProperty('rate',150)
                setvoice()
            else:
                engine.setProperty('rate',60)
                setvoice()





#icons
image_icon=PhotoImage(file='C:/Python311/speak.png')
m.iconphoto(0,image_icon)

#frame
frame=Frame(m,bg='white',height=100,width=900)
frame.place(x=0,y=0)

l=PhotoImage(file='C:/Python311/icons8-speaker-48.png')
Label(frame,image=l,bg='white').place(x=10,y=25)

Label(frame,text ='TEXT TO SPEECH',font='arial 20 bold',bg='white',fg='black').place(x=100,y=30)

text_area=Text(m,font='Roboto 20',bg='white',relief=GROOVE,wrap=WORD)
text_area.place(x=10,y=130,width=500,height=250)

Label(m,text='VOICE',font='arial 15 bold',bg='purple',fg='white').place(x=580,y=160)
Label(m,text='SPEED',font='arial 15 bold',bg='purple',fg='white').place(x=780,y=160)

gender_box=Combobox(m,values=['Male','Female'],font='arial 14',state='r',width=10)
gender_box.place(x=550,y=200)
gender_box.set('Male')


speed_box=Combobox(m,values=['Fast','Normal','Slow'],font='arial 14',state='r',width=10)
speed_box.place(x=750,y=200)
speed_box.set('Normal')


button=Button(m,text='SPEAK',width=10,font='arial 14 bold',command=speaknow).place(x=550,y=280)

save=Button(m,text='SAVE',width=10,bg='lightgreen',font='arial 14 bold',command=download).place(x=750,y=280)



m.mainloop()
