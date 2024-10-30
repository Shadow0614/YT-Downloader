streams = get_video_streams(vid_link, file_type, quality)
if streams:
    video = streams.get_highest_resolution(progressive=False)
    print(f"Downloading video: {video.title}")
    video.download()
    print("Download complete.")
else:
    print("Error: No streams found with selected quality and file type. Specified quality might not be available for this video. Please try changing the file type or video quality and try again.")