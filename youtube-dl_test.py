import youtube_dl

def get_video_info(url):
    # Set youtube-dl options to extract metadata without downloading
    ydl_opts = {
        'quiet': True,
        'skip_download': True,
        'force_generic_extractor': True,
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            # Extract information from the video URL
            info = ydl.extract_info(url, download=False)
            # Display video details
            print("Title:", info.get('title', 'N/A'))
            print("Description:", info.get('description', 'N/A'))
            print("Publish Date:", info.get('upload_date', 'N/A'))
        except Exception as e:
            print("An error occurred:", str(e))

# Prompt the user for a YouTube video link
video_url = input("Enter the YouTube video URL: ")
get_video_info(video_url)