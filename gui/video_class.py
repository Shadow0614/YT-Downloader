import pytubefix as pt
import urllib

class Video:
    def __init__(self, url, resolution, filetype, status_label=None):
        self.url = url
        self.resolution = resolution
        self.filetype = filetype
        self.status_label = status_label


        # self.resolution = pt.YouTube(self.url).streams.filter(file_extension=self.filetype).order_by('resolution').desc().first().resolution # If resolution is not specified by user, set it to the highest resolution available for the specified file type.

        # self.__resolutions = []
        # for stream in pt.YouTube(self.url).streams.filter(file_extension=filetype.get()).order_by('resolution').desc():
        #     self.__resolutions.append(stream.resolution)
        # for i in range(10):
        #     for r in self.__resolutions:
        #         if self.__resolutions.count(r) > 1:
        #             self.__resolutions.remove(r)
        # print(self.__resolutions)


    def download(self):
        try:
            video = pt.YouTube(self.url)
            
        except urllib.error.URLError:
            self.status_label.configure(text="Error: No internet connection.", text_color="red")

        except Exception as e:
            print(f"Error: {e}")
            self.status_label.configure(text="Error: Invalid URL", text_color="red")
            return
        
        # self.status_label.configure(text="Downloading...", text_color="white")
        self.streams = video.streams.filter(res=self.resolution, file_extension=self.filetype).order_by('resolution').desc()
        for s in self.streams:
            print(s)