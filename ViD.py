from tkinter import *
from tkinter import filedialog
from pytube import YouTube
import tkinter as tk
import os
from moviepy.video.io.VideoFileClip import VideoFileClip, AudioFileClip
import shutil
import random

path = "temp"


def selectdir():
    global dirname
    global save
    folder = open("path.txt", "w")
    dirname = filedialog.askdirectory(parent=window,initialdir="/",title="Select a directory")
    folder.write(dirname)
    print(f"Dir selected: {dirname}")

with open("path.txt", "r") as txt:
    for row in txt:
        dirname = row

try:
    print(f"Actual downloads dir: {dirname}")
except:
    True


def mp4():
    print("Starting video download...")

    num = random.randint(0, 9999999999)
    name = str(num).zfill(10) 

    try:
        shutil.rmtree("temp")
    except:
        True
    try:
        link = videos.get()
        video = YouTube(link)
        try:
            video.streams.filter(resolution = "1080p").first().download(path, "video.mp4")
        except:
            try:
                video.streams.filter(resolution = "720p").first().download(path, "video.mp4")
            except:
                try:
                    video.streams.filter(resolution = "480p").first().download(path, "video.mp4")
                except:
                    try:
                        video.streams.filter(resolution = "360p").first().download(path, "video.mp4")
                    except:
                        try:
                            video.streams.filter(resolution = "240p").first().download(path, "video.mp4")
                        except:
                            video.streams.filter(resolution = "144p").first().download(path, "video.mp4")
        
        video.streams.get_audio_only().download(path, "audio.mp3")

        vid = VideoFileClip("temp/video.mp4")
        aud = AudioFileClip("temp/audio.mp3")
        final = vid.set_audio(aud)
    except:
        print("ERROR! - invalid link or directory")
    try:
        final.write_videofile(f"{dirname}/{name}.mp4")
    except:
        try:
            shutil.rmtree("temp")
        except:
            True
    try:
        shutil.rmtree("temp")

    except:
        True

def mp3():
    print("Starting audio download...")
    try:
        link = videos.get()
        audio = YouTube(link)

        audiod = audio.streams.filter(only_audio=True).first()

        out_file = audiod.download(output_path=dirname)

        base, none = os.path.splitext(out_file)
        new_file = base + ".mp3"
        os.rename(out_file, new_file)

        print(f"-100%...")
        print(f"Audio was successfully downloaded in: {dirname}")
    except:
        print("ERROR! - invalid link or directory")

try:
    shutil.rmtree("temp")
except:
    True

try:
    os.mkdir("temp")
except:
    True

window = Tk()

window.title("ViD")
window.resizable(width=0, height=0)
try:
    window.iconbitmap("img\icon.ico")
except:
    True
try:
    logo = PhotoImage(file = "img\logo.png")
except:
    True


border1 = tk.Frame(window, padx=5, pady=5, highlightbackground = "#646464", highlightthickness = 5, bd=5)
border1.pack()
border1.configure(bg = "#A6A6A6")

border = tk.Frame(border1, padx=10, pady=10, highlightbackground = "#646464", highlightthickness = 5, bd=5)
border.pack()

border3 = tk.Frame(border, highlightbackground = "#646464", highlightthickness = 0)
border3.pack()

borderb2 = tk.Frame(border, highlightbackground = "#646464", highlightthickness = 3)
borderb2.pack()
borderb2.configure(bg = "#A6A6A6")

borderspace = tk.Frame(border, highlightbackground = "#646464", highlightthickness = 0)
borderspace.pack()

borderb1 = tk.Frame(border, highlightbackground = "#646464", highlightthickness = 3)
borderb1.pack()
borderb1.configure(bg = "#A6A6A6")

borderspace1 = tk.Frame(border, highlightbackground = "#646464", highlightthickness = 0)
borderspace1.pack()

l = Label(border3, text = "Ξ DOWNLOADER Ξ", font=("impact", 22))
l.pack()

try:
    image = Label(border3, image = logo)
    image.pack()
except:
    True
    
space = Label(border3, text = " ", font = ("reem kufi", 1))
space.pack()

presentation = Label(border3, text = "Insert video link", width = 15, font = ("Franklin Gothic Medium", 13))
presentation.pack()

space = Label(border3, text = " ", font = ("reem kufi", 1))
space.pack()

videos = Entry(borderb2, relief="flat", font = ("arial", 10), width = 25, bd = 3)
videos.focus_force()
videos.pack()

space = Label(borderspace, text = " ", font = ("reem kufi", 5))
space.pack()

b1 = Button(borderb1, text = "Select directory", width = 15, height=1, font = ("Arial Black", 10), relief = "flat", command = selectdir)
b1.pack()
b1.configure(bg="#D9D9D9")

b = Button(borderb1, text = "Download video", width = 15, height=1, font = ("Arial Black", 10), relief = "flat", command = mp4)
b.pack()
b.configure(bg="#D9D9D9")

b2 = Button(borderb1, text = "Download audio", width = 15, height=1, font = ("Arial Black", 10), relief = "flat", command = mp3)
b2.pack()
b2.configure(bg="#D9D9D9")

window.mainloop()
