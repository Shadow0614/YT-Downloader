import main
from moviepy.editor import VideoFileClip, AudioFileClip
from pytubefix import YouTube

filetype = main.video_filetype
filename = main.video_title

def combine_streams():

    print(filetype) #FIXME: filename and filetype are not being read correctly
    print(filename)

    video_path = f"temp/temp_video.{filetype}"
    audio_path = "temp/temp_audio.webm"
    output_path = f"{filename}.{filetype}"

    video_clip = VideoFileClip(video_path)
    audio_clip = AudioFileClip(audio_path)

    # Set the audio of the video clip
    final_clip = video_clip.set_audio(audio_clip)

    # Write the result to a file with high-quality codecs
    final_clip.write_videofile(output_path, codec='libx265', audio_codec='aac')