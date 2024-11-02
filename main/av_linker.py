import ffmpeg
import re

def combine_streams(filename, filetype):
    sanitized_filename = re.sub(r'[<>:"/\\|?*]', '_', filename) # Replace special characters with underscores

    video_path = f"temp/temp_video.{filetype}"
    audio_path = "temp/temp_audio.webm"
    output_name = f"{sanitized_filename}.{filetype}"

    video = ffmpeg.input(video_path)
    audio = ffmpeg.input(audio_path)

    ffmpeg.output(video, audio, output_name, vcodec='copy', acodec='aac').run(overwrite_output=True)