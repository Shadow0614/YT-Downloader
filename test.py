import pytubefix as pt

def get_audio_streams(vid_link):
    try:
        vid = pt.YouTube(vid_link)
    except TypeError:
        print("Error: YouTube link is invalid")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

    audio_streams = vid.streams.filter(only_audio=True)

    for s in audio_streams:
        print(s)

get_audio_streams("https://www.youtube.com/watch?v=9bZkp7q19f0")