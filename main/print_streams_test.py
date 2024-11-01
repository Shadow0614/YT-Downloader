import pytubefix as pt

video = "https://www.youtube.com/watch?v=BxdSUGBs0gM"

vid = pt.YouTube(video)

for s in vid.streams:
    print(s)