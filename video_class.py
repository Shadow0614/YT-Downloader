import pytubefix as pt
from consts import RESOLUTIONS, FILETYPES

class Video:
    def __init__(self):
        self.filetype = "mp4"
        try:
            self.resolution = 
        except:
            print("Error: YouTube link is invalid")


    def get_user_input(self): # Prompts user to input desired video link, resolution, and file type
        while True:
                self.url = input("Enter YouTube video link: ")
                try:
                    pt.YouTube(self.url) # Try to create a YouTube object with the given url
                except:
                    print("\nInvalid YouTube link. Please enter a valid link.\n")
                    continue # Skip the rest of the loop and start the next iteration
                break

        while True:
            self.filetype = input("Enter desired file type, if known (Ex: mp4, m4a, webm). Press enter to skip: ")
            if self.filetype in FILETYPES:
                break
            elif self.filetype == "":
                self.filetype = "mp4"
                break
            print("\nInvalid file type. Please enter a valid file type. Press enter to skip.\n")

        while True:
            self.resolution = input("Enter desired video resolution, if known (Ex: 720p, 1080p, 1440p, etc). Press enter to skip: ")
            if self.resolution in RESOLUTIONS:
                break
            elif self.resolution == "":
                self.resolution = pt.YouTube(self.url).streams.filter(file_extension=self.filetype).order_by('resolution').desc().first().resolution # If resolution is not specified by user, set it to the highest resolution available for the specified file type.
                break
            print("\nInvalid video resolution. Please enter a valid resolution. Press enter to skip.\n")


    def download(self):
        try:
            video = pt.YouTube(self.url)
            self.streams = video.streams.filter(file_extension=self.filetype).order_by('resolution').desc()
            for s in self.streams:
                print(s)
        except TypeError:
            print("Error: YouTube link is invalid")
            return
        except Exception as e:
            print(f"Error: {e}")
            return

        # video_streams = vid.streams.filter(res=self.resolution, file_extension=self.filetype)
        # vid_filename = f"temp_video.{self.filetype}"
        # video_streams.first().download(output_path="temp", filename=vid_filename)

test = Video("https://www.youtube.com/watch?v=BxdSUGBs0gM")
test.get_user_input()
print(test.url, test.resolution, test.filetype)