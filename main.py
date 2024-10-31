import pytubefix as pt
import audio_linker2 as al
from urllib import request

video_title = ""
video_filetype = ""

# Filters the video based on the provided link, quality, and file type
# Should return a StreamQuery object, similar to a list
def get_video_streams(vid_link, quality, file_type):
    try:
        vid = pt.YouTube(vid_link)
    except TypeError:
        print("Error: YouTube link is invalid")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

    if not quality: # Equivalent to (if quality == ""), b/c python sees empty strings as False
        quality = vid.streams.get_highest_resolution(progressive=False).resolution

    if not file_type:
        file_type = "mp4"

    video_streams = vid.streams.filter(res=quality, file_extension=file_type)

    # If type of vid is correct, filter streams with the specified quality and file type, and return filtered streams
    return video_streams

# # Filters the audio based on the provided link
def get_audio_stream(vid_link):
    try:
        vid = pt.YouTube(vid_link)
    except TypeError:
        print("Error: YouTube link is invalid")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

    audio_stream = vid.streams.filter(only_audio=True).order_by('abr').desc().first()

    return audio_stream

# Checks to make sure that user is connected to the internet
def internet_check():
    try:
        request.urlopen('https://www.youtube.com', timeout=1)
        return True
    except request.URLError:
        print("Error: no internet connection.")
        return False
    

def v_download(video, file_type):
    if not file_type:
        file_type = "mp4"
    print(f"\nDownloading video: {video.title} at {video.resolution} in {file_type} format")
    print("Download in progress...")
    vid_filename = f"temp_video.{file_type}"
    video.download(output_path="temp", filename=vid_filename)
    print("Download complete.\n")

def a_download(audio):
    audio.download(output_path="temp", filename="temp_audio.webm")


# Main function that takes in user input for the YouTube video link, quality, and file type
def main():
    while True:
        vid_link = input("Enter YouTube video link: ")
        if "youtube.com/watch?" in vid_link or "youtu.be/" in vid_link:
            break
        print("Invalid YouTube link. Please enter a valid link.\n")

    while True:
        quality = input("Enter desired video quality, if known (Ex: 720p, 1080p, 1440p, etc). Press enter to skip: ")
        if quality in ["144p", "240p", "360p", "720p", "1080p", "1440p", "2160p"] or quality == "":
            break
        print("\nInvalid video quality. Please enter a valid quality. Press enter to skip.\n")

    while True:
        file_type = input("Enter desired file type, if known (Ex: mp4, m4a, webm). Press enter to skip: ")
        if file_type in ["mp4", "m4a", "webm"] or file_type == "":
            global video_filetype
            video_filetype = file_type
            break
        print("\nInvalid file type. Please enter a valid file type. Press enter to skip.\n")

    # Checks to make sure user is connected to the internet before continuing
    if not internet_check():
        return

    audio_stream = get_audio_stream(vid_link)
    a_download(audio_stream)

    # Checks to make sure that a video stream with the user's specified quality and file type exists, prints error message if it doesn't
    video_streams = get_video_streams(vid_link, quality, file_type)
    for i in range(3):
        if video_streams:
            video = video_streams.get_highest_resolution(progressive=False)
            v_download(video, file_type)
            al.combine_streams(video.title, file_type or "mp4")
            break
        elif i == 0:
            streams = get_video_streams(vid_link, quality, file_type="m4a")
        elif i == 1:
            streams = get_video_streams(vid_link, quality, file_type="webm")
        else:
            print("\nError: No streams found with selected quality and file type. Specified quality might not be available for this video. Please try changing the file type or video quality and try again.")

    if input("Do you want to download another video? (y/n): ").lower() == "y":
        main()



if __name__ == "__main__":
    main()