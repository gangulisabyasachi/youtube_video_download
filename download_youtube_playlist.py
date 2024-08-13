import yt_dlp as youtube_dl

def download_playlist(playlist_url, download_path):
    ydl_opts = {
        'outtmpl': f'{download_path}%(playlist_title)s/%(title)s.%(ext)s',  # Save each video in a folder named after the playlist
        'format': 'best'
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

if __name__ == "__main__":
    playlist_url = "https://www.youtube.com/playlist?list=PLu0W_9lII9aiXlHcLx-mDH1Qul38wD3aR"
    download_path = "/Users/sabyasachiganguli/Desktop/new/"
    download_playlist(playlist_url, download_path)
