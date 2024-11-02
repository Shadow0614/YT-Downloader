class video:
    def __init__(self, link, title, resolution, filetype):
        self.title = title
        self.resolution = resolution
        self.filetype = filetype

test = video("test", "1080p", "mp4")
print(test.title)
print(test.resolution)
print(test.filetype)