import yt_dlp as youtube_dl

def download_video(url, download_path):
    ydl_opts = {
        'outtmpl': f'{download_path}%(title)s.%(ext)s',
        'format': 'best'
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=snYu2JUqSWs"
    download_path = "/Users/sabyasachiganguli/Desktop/"
    download_video(url, download_path)
