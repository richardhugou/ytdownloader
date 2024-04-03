from pytube import YouTube
from sys import argv
import os
import tkinter as tk


def download_video_info(video_url):
    try:
        yt = YouTube(video_url)
        print("Title:", yt.title)

        if yt.views:
            print("Views:", yt.views)
        else:
            print("Views information not available.")

        # Get the highest resolution stream
        stream = yt.streams.get_highest_resolution()

        # Set the download path
        download_path = r'D:\Scripts\ytDownloader\Downloads_youtube'
        file_name = stream.default_filename
        full_path = os.path.join(download_path, file_name)

        # Check if the file already exists
        counter = 1
        while os.path.exists(full_path):
            base_name, extension = os.path.splitext(file_name)
            new_name = f"{base_name} ({counter}){extension}"
            full_path = os.path.join(download_path, new_name)
            counter += 1
# how to had a print statement
        
        # Download the video
        stream.download(download_path)

        print(f"\nVideo downloaded to: {full_path}")

    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    from tkinter import simpledialog
    root = tk.Tk()
    root.withdraw()

    youtube_link=simpledialog.askstring(Title="Insérer le lien de la vidéo ici")
    if len(youtube_link) != 2:
        print("Usage: python ytDownloader.py <YouTube video URL>")
    else:
        download_video_info(youtube_link)
    root.destroy()
