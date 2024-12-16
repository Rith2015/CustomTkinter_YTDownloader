import tkinter
import customtkinter
from pytubefix import YouTube
from urllib.request import urlopen
from PIL import Image, ImageTk
import io
import os

# System Settings
customtkinter.set_appearance_mode("Dark") 
customtkinter.set_default_color_theme("dark-blue")

# Our app Frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Downloader")

# Appearance modes
def toggle_appearance():
    if customtkinter.get_appearance_mode() == "Dark":
        customtkinter.set_appearance_mode("Light")
        switch_button.configure(text="Dark mode")
    else:
        customtkinter.set_appearance_mode("Dark")
        switch_button.configure(text="Light mode")

# button to switch the appearance mode
switch_button = customtkinter.CTkButton(app, text="Light mode", command=toggle_appearance, width=80, height=20)
switch_button.pack(padx=10, pady=10, anchor='nw')

# Adding UI Elements
title_label = customtkinter.CTkLabel(app, text="Input a YouTube link")
title_label.pack(pady=10) 
# Thumbnail preview
thumbnail_label = customtkinter.CTkLabel(app, text="") 
thumbnail_label.pack(pady=10)
# Video title label
video_title_label = customtkinter.CTkLabel(app, text="", font=("Arial", 14)) 
video_title_label.pack(pady=10)
# Frame for URL input and search button
input_frame = customtkinter.CTkFrame(app)  
input_frame.pack(pady=10) 

# Link Input field inside input frame
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(input_frame, width=350, height=40, textvariable=url_var)
link.pack(side="left", padx=10) 

# Button to preview thumbnail inside input frame
preview_button = customtkinter.CTkButton(input_frame, text="Show Preview", command=lambda: show_thumbnail(), width=120)
preview_button.pack(side="left")

# Thumbnail preview logic
def show_thumbnail():
    yt_link = link.get()
    try:
        yt_object = YouTube(yt_link)
        thumbnail_url = yt_object.thumbnail_url  # Get thumbnail URL
        # Fetch the thumbnail image
        image_data = urlopen(thumbnail_url).read()
        img = Image.open(io.BytesIO(image_data))
        img = img.resize((360, 200))
        img_tk = ImageTk.PhotoImage(img)
        # Update thumbnail label
        thumbnail_label.configure(image=img_tk, text="")
        thumbnail_label.image = img_tk 
    
        # Update video title
        video_title_label.configure(text=f"{yt_object.title}")
    except Exception as e:
        thumbnail_label.configure(text="Invalid or no YouTube link provided.", image=None)
        thumbnail_label.image = None
        video_title_label.configure(text="")

# Download Buttons
def download_content(content_type="video"):
    try:
        yt_link = link.get()
        yt_object = YouTube(yt_link)
        home_path = os.path.expanduser("~")
        download_folder = os.path.join(home_path, "Downloads")

        if content_type == "video":
            content = yt_object.streams.get_highest_resolution()
        elif content_type == "audio":
            content = yt_object.streams.get_audio_only()
        else:
            print("Invalid content type selected.")
            return
        content.download(output_path=download_folder)
        print(f"{content_type.capitalize()} download complete!")
    except Exception as e:
        print(f"Error: {str(e)} - YouTube link is invalid")

# Frame for Buttons
button_frame = customtkinter.CTkFrame(app) 
button_frame.pack(pady=20) 

Video = customtkinter.CTkButton(button_frame, text="MP4", command=lambda: download_content("video"), width=100, height=40)
Audio = customtkinter.CTkButton(button_frame, text="MP3", command=lambda: download_content("audio"), width=100, height=40)

Video.pack(side="left", padx=10) 
Audio.pack(side="left", padx=10)

# Run the app
app.mainloop()
