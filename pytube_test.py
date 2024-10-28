import pytubefix as pt
#Have to use pytubefix instead of pytube for now. Can switch back when "HTTP Error 400: Bad Request" error is fixed.

def startDownload(vid_link: str):
    try:
        yt = pt.YouTube(vid_link)
        video = yt.streams.get_highest_resolution("1440p") #FIXME: Might not work properly, replace with get_highest_resolution()
        # print(video)
        for stream in yt.streams:
            print(stream) if "1080" in str(stream) else print("No stream found")
        # Uncomment the next line to download the video
        # video.download()

    # Handle multiple exceptions that might occur
    except pt.exceptions.RegexMatchError:
        print("Error: YouTube link is invalid")
    except pt.exceptions.VideoUnavailable:
        print("Error: The requested video is unavailable.")
    except pt.exceptions.PytubeFixError as ex:
        print(f"Error: Pytube error occurred: {ex}")
    except pt.exceptions.VideoPrivate:
        print("Error: The requested video is private")
    except Exception as ex:
        print(f"Error: An unexpected error occurred: {ex}")


link1 = "https://www.youtube.com/watch?v=5CIDmO9k44w"

link2 = "https://www.youtube.com/watch?v=OlNWCpFdVMA"

startDownload(link2)