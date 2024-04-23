
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
git clone https://github.com/richardhugou/ytdownloader.git
cd ytdownloader
```
2. Install Dependencies

```bash
pip install pytube
```

3. Run the Script
Using Python Interpreter:
Copy code
```python ytDownloader.py```
Using Executable:
If you want to use the standalone executable:

Run ytDownload.exe and provide the YouTube video URL.

4. Creating Executable with PyInstaller
If you want to create a standalone executable:
Copy code
```
pip install pyinstaller
pyinstaller --onefile --noconsole ytDownloader.py
```
This will create an executable (ytDownload.exe) in the dist directory.
Navigate to the dist directory after creating the executable.

Notes
Make sure to replace past in the tkinter simpledialog your ```<YouTube video URL>```. It doesn't work offline obviously.
The script will display information about the video, and if you created an executable, you can run it directly.
Feel free to customize the script and share your feedback or improvements!

Improvments
Age restricted content are not downloadable yet, my apologize on that matter
