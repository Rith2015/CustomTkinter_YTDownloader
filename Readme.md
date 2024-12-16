# YouTube Downloader
A simple Python-based YouTube downloader application with a graphical user interface (GUI) built using `customtkinter`. This app allows users to preview the video thumbnail and title before downloading the video or audio.
## Features
- **Dark/Light Mode**: Toggle between dark and light modes for the app's appearance.
- **YouTube Video Preview**: Input a YouTube link to display the video thumbnail and title.
- **Download Options**:
  - Download video in MP4 format.
  - Download audio in MP3 format.
## Requirements
- Python 3.7+
- customtkinter
- pytubefix
- pillow
## Installation
1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd <repository-folder>
2. Install the required Python packages using one of the following methods:
    ```bash
    pip install -r requirements.txt
-  Or, by manually installing the necessary packages:
    ```bash
    pip install customtkinter pytube pillow
## Run the application:
    python app.py
## Usage
Enter a valid YouTube video link in the input field.
Click the Show Preview button to display the video thumbnail and title.Choose either MP4 or MP3 to download the video or audio. The files will be saved in the Downloads folder of your system.
## File Structure
- app.py: The main script for the YouTube downloader application.
## Dependencies:
- customtkinter for the GUI.
- pytubefix for downloading YouTube videos.
- Pillow for displaying video thumbnails.
