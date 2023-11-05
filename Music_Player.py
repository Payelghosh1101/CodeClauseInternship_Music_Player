from tkinter import *
import tkinter as tk
from tkinter import filedialog
from pygame import mixer

class MP:
    def __init__(self, win):
        win.geometry('400x400')
        win.title('Music Player')
        win.resizable(0, 0)


        self.play_restart = tk.StringVar()
        self.pause_resume = tk.StringVar()
        self.play_restart.set('Play')
        self.pause_resume.set('Pause')

        load_button = Button(win, text='Load', width='10', font=('Arial', 20), background='DodgerBlue', command=self.Load)
        load_button.place(x = 200, y = 40, anchor='center')


        play_button = Button(win, textvariable=self.play_restart, width='10', font=('Arial', 20), background='MediumSeaGreen', command=self.Play)
        play_button.place(x = 200, y = 150, anchor='center')

        pause_button = Button(win, textvariable=self.pause_resume, width='10', font=('Arial', 20), background='green', command=self.Pause)
        pause_button.place(x = 200, y = 260, anchor='center')

        stop_button = Button(win, text='stop', width='10', font=('Arial', 20), background='Tomato', command=self.Stop)
        stop_button.place(x = 200, y = 370, anchor='center')

        self.music_file = False
        self.playing_state = False



    def Load(self):
        self.music_file = filedialog.askopenfilename()
        print("Loaded : ", self.music_file)
        self.play_restart.set('Play')

    def Play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()
            self.playing_state = False
            self.play_restart.set('Restart')
            self.pause_resume.set('Pause')


    def Pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state = True
            self.pause_resume.set('Resume')
        else:
            mixer.music.unpause()
            self.playing_state = False
            self.pause_resume.set('Pause')

    def Stop(self):
        mixer.music.stop()

root = Tk()
MP(root)
root.mainloop()


