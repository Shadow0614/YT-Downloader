import ffmpeg
from moviepy.editor import VideoFileClip, AudioFileClip
from pytubefix import YouTube

def combine_streams(filename, filetype):

    # print(filetype) #FIXME: filename and filetype are not being read correctly
    # print(filename)

    video_path = f"temp/temp_video.{filetype}"
    audio_path = "temp/temp_audio.webm"
    output_name = f"{filename}.{filetype}"

    video_clip = VideoFileClip(video_path)
    audio_clip = AudioFileClip(audio_path)

    # Set the audio of the video clip
    final_clip = video_clip.set_audio(audio_clip)

    # Write the result to a file with high-quality codecs
    # final_clip.write_videofile(output_name, preset = "ultrafast", logger = "bar", threads=32)

    ffmpeg.input(video_path).output(
    audio=ffmpeg.input(audio_path),
    filename=output_name,
    vcodec='copy',  # Copy the video stream without re-encoding
    acodec='copy',   # Use AAC codec for audio
    strict='experimental'
    ).run()