Certainly! Below is the content for a single text file (README.md) that includes instructions on how the script works and how to get it running. You can copy and paste this content into a file named README.md in your project directory.

markdown
Copy code
# YouTube Video Downloader

This Python script allows you to download information about a YouTube video using the `pytube` library. Additionally, it provides the option to create a standalone executable using PyInstaller.

## How it Works

1. The script (`ytDownloader.py`) accepts a YouTube video URL as a command-line argument.

2. It uses the `pytube` library to fetch information about the video, such as title and views.

3. If you haven't installed `pytube` and/or PyInstaller, you can follow the installation instructions below.

4. The script can be executed from the command line by providing the YouTube video URL.

## Usage

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/yt-downloader.git
cd yt-downloader
2. Install Dependencies
bash
Copy code
pip install -r requirements.txt
3. Run the Script
Using Python Interpreter:
bash
Copy code
python ytDownloader.py <YouTube video URL>
Using Executable:
If you want to use the standalone executable:

Navigate to the dist directory after creating the executable.
Run ytDownload.exe and provide the YouTube video URL.
4. Creating Executable with PyInstaller
If you want to create a standalone executable:

bash
Copy code
pip install pyinstaller
pyinstaller --onefile ytDownloader.py
This will create an executable (ytDownload.exe) in the dist directory.

Notes
Make sure to replace <YouTube video URL> with the actual URL of the video you want to download.
Ensure that you have an active internet connection.
The script will display information about the video, and if you created an executable, you can run it directly.
Feel free to customize the script and share your feedback or improvements!
