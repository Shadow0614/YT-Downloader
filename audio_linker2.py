# import main
from moviepy.editor import VideoFileClip, AudioFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_merge_video_audio
from pytubefix import YouTube

def combine_streams(filename, filetype):

    # print(filetype) #FIXME: filename and filetype are not being read correctly
    # print(filename)

    video_path = f"temp/temp_video.{filetype}"
    audio_path = "temp/temp_audio.webm"
    output_path = f"{filename}.{filetype}"

    video_clip = VideoFileClip(video_path)
    audio_clip = AudioFileClip(audio_path)

    # Set the audio of the video clip
    final_clip = video_clip.set_audio(audio_clip)

    # Write the result to a file with high-quality codecs
    
# printing logs can be a bottleneck sometimes, so we put ffmpeg_ouput=False
# and logger = None
# you can change video codec(vcodec) or audio codec (acodec) as per your need
    ffmpeg_merge_video_audio(video_path, audio_path, output_path, ffmpeg_output=False, logger="bar")