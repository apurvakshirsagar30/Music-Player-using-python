from tkinter import *
import tkinter as tk
import fnmatch
import os
from pygame import mixer

canvas = tk.Tk()
canvas.title("Music player")
canvas.geometry("600x800")
canvas.config(bg='black')

rootpath = "C:\\Users\HP\Music"
pattern = "*.mp3"

mixer.init()
prev_img = tk.PhotoImage(file=r"prev_new.png")
play_img = tk.PhotoImage(file=r"play_new.png")
stop_img = tk.PhotoImage(file=r"stop_new.png")
next_img = tk.PhotoImage(file=r"next_new.png")

def select():
    label.config(text=listBox.get("anchor"))
    # print("SONG PATH ===>", rootpath + "\\" + listBox.get("anchor"))
    mixer.music.load(rootpath + "\\" + listBox.get("anchor"))
    mixer.music.play()

def stop():
    mixer.music.stop()
    # listBox.select_clear('active')

def play_next():
    next_song = listBox.curselection()
    next_song = next_song[0] + 1
    # print("NEXT song ==> ", next_song)
    next_song_name = listBox.get(next_song)
    label.config(text=next_song_name)

    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()
    listBox.select_clear(0, 'end')
    listBox.activate(next_song)
    listBox.select_set(next_song)

def play_prev():
    prev_song = listBox.curselection()
    prev_song = prev_song[0] - 1
    # print("PREVIOUS song ==> ", prev_song)
    prev_song_name = listBox.get(prev_song)
    label.config(text=prev_song_name)

    mixer.music.load(rootpath + "\\" + prev_song_name)
    mixer.music.play()

    listBox.select_clear(0, 'end')
    listBox.activate(prev_song)
    listBox.select_set(prev_song)


title_label = tk.Label(canvas, text='Music Player System', bg='black', fg='yellow', font=('Times New Roman', 20, 'bold'))
title_label.pack(pady=15)

listBox = tk.Listbox(canvas, fg="cyan", bg="black", width=100, font=('Times New Roman', 14))
listBox.pack(padx=15, pady=15)

label = tk.Label(canvas, text='', bg='black', fg='pink', font=('Times New Roman', 18))
label.pack(pady=15)

top = tk.Frame(canvas, bg="black")
top.pack(padx=10, pady=5, anchor='center')

prevButton = Button(canvas, text="Previous", image=prev_img, height=34, width=34, borderwidth=0, command=play_prev)
prevButton.pack(padx=15, pady=15, in_=top, side='left')

playButton = tk.Button(canvas, text="Play", image=play_img, height=34, width=34, borderwidth=0, command=select)
playButton.pack(padx=15, pady=15, in_=top, side='left')

stopButton = tk.Button(canvas, text="Stop", image=stop_img, height=34, width=34, borderwidth=0, command=stop)
stopButton.pack(padx=15, pady=15, in_=top, side='left')

nextButton = tk.Button(canvas, text="Next", image=next_img, height=34, width=34, borderwidth=0, command=play_next)
nextButton.pack(padx=15, pady=15, in_=top, side='left')

for root, dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files, pattern):
        listBox.insert('end', filename)

canvas.mainloop()
