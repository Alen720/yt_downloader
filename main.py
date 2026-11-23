import yt_dlp

def download(url: str):
    yt_opts = {
        "format": "bestvideo+bestaudio/best",
        "merge_output_format": "mp4"
    }

    try:
        with yt_dlp.YoutubeDL(yt_opts) as ydl:
            ydl.download([url])

        print("Video downloaded succsessfuly!")
    except Exception as e:
        print("Error: ", str(e))

video_url = input("Enter the video URL: ").strip()

download(video_url)
