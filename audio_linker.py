import ffmpeg
from pytubefix import YouTube

def combine_streams(filename, filetype):

    # print(filetype) #FIXME: filename and filetype are not being read correctly
    # print(filename)

    video_path = f"temp/temp_video.{filetype}"
    audio_path = "temp/temp_audio.webm"
    output_name = f"{filename}.{filetype}"

    video = ffmpeg.input(video_path)
    audio = ffmpeg.input(audio_path)

    ffmpeg.output(video, audio, output_name, vcodec='copy', acodec='aac').run(overwrite_output=True)