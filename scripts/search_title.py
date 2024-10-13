import yt_dlp

def download(name, vids):
    path = "./videos"
    ydl_opts = {
        'outtmpl' : f'{path}/%(title)s.%(ext)s',
        'format' : 'best',
        'noplaylist' : True,
        'max_downloads' : vids,
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([f'ytsearch{vids}:{name}'])
        except yt_dlp.utils.MaxDownloadsReached:
            print("Maximum number of downloads reached, stopping.")
        except yt_dlp.utils.ExtractorError as e:
            print(f"Error downloading video: {e}")
        
    