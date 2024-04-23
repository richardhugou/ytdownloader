from pytube import YouTube
from tkinter import simpledialog, filedialog
import os
import tkinter as tk

def downloadvideoinfo(youtubelink):
    try:
        yt = YouTube(youtubelink)
        print("Title:", yt.title)

        if yt.views:
            print("Views:", yt.views)
        else:
            print("Views information not available.")

        # Filter streams by resolution and get the highest resolution stream
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

        # Ask user to select download directory
        download_path = filedialog.askdirectory(title="Select Download Directory")

        # Set the download path
        file_name = stream.default_filename
        full_path = os.path.join(download_path, file_name)

        # Check if the file already exists
        counter = 1
        while os.path.exists(full_path):
            base_name, extension = os.path.splitext(file_name)
            new_name = f"{base_name} ({counter}){extension}"
            full_path = os.path.join(download_path, new_name)
            counter += 1

        # Download the video
        stream.download(download_path)

        print(f"\nVideo downloaded to: {full_path}")

    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    
    youtube_link = simpledialog.askstring(title="Insérer le lien de la vidéo ici", prompt="")
    downloadvideoinfo(youtube_link)
    root.destroy()