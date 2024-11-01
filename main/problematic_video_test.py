from pytubefix import YouTube

vid = YouTube("https://www.youtube.com/watch?v=NI9LXzo0UY0")

for stream in vid.streams:
    print(stream)