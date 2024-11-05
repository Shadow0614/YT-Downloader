import pytubefix as pt
from urllib import error
import main.av_linker as al

class Video:
    def __init__(self, url, resolution, filetype, status_label=None):
        """Initialize Video object with user selections for url, resolution, and filetype"""
        self.url = url
        self.resolution = resolution
        self.filetype = filetype
        self.status_label = status_label


    def validate_url(self):
        """Check if the URL is valid and get available streams"""
        if not self.url:
            # self.status_label.configure(text="Please enter a URL", text_color="white")
            # print("Please enter a URL") # Print to console instead of GUI
            # ABOVE TWO LINES FOR DEBUGGING
            return False
            
        try:
            self.video = pt.YouTube(self.url)
            return True
        except error.URLError:
            self.status_label.configure(text="Error: No internet connection", text_color="red")
            return False
        except Exception:
            # self.status_label.configure(text="Error: Invalid YouTube URL", text_color="red")
            # print("Error: Invalid YouTube URL") # Print to console instead of GUI
            # ABOVE TWO LINES FOR DEBUGGING
            return False


    def get_available_resolutions(self):
        """Get list of available resolutions for current url and filetype"""
        if not self.validate_url(): # If entered URL is invalid
            return ["Select Resolution"]
            
        # Get all streams for current filetype
        streams = self.video.streams.filter(file_extension=self.filetype)
        
        # Extract unique resolutions
        self.resolutions = []
        for stream in streams:
            if stream.resolution and (stream.resolution not in self.resolutions):
                self.resolutions.append(stream.resolution)
                
        # Sort resolutions from highest to lowest
        self.resolutions.sort(key = lambda x: int(x[0:-1]), reverse=True) # Sort by resolution. Lambda maps res like "1080p" to 1080
        
        # If we found resolutions, return them. Otherwise return ["No resolutions available"]
        return self.resolutions if self.resolutions else ["No resolutions available, change file type"]


    def download_audio(self):
        """Download the audio stream for the video"""
        audio = self.video.streams.filter(only_audio=True, file_extension="webm").order_by("abr").first() # Get audio stream with the highest bitrate
        audio.download(output_path="temp", filename="temp_audio.webm")


    def download(self):
        """Download the video with user selected options"""
        if not self.validate_url():
            if not self.url:
                self.status_label.configure(text="Please enter a URL", text_color="white")
            else:
                self.status_label.configure(text="Error: Invalid YouTube URL", text_color="red")
            return
            
        if self.resolution == "Select Resolution":
            self.status_label.configure(text="Please select a resolution", text_color="white")
            return
            
        try:
            stream = self.video.streams.filter(res=self.resolution, file_extension=self.filetype).first()
            self.title = stream.title
            
            if not stream: # If no streams are found for selected parameters
                self.status_label.configure(text="Error: Selected resolution not available, please select another resolution", text_color="red")
                return
            
            stream.download(output_path="temp", filename="temp_video." + self.filetype)
            self.download_audio()
            self.status_label.configure(text="Downloading...", text_color="white")
            al.combine_streams(self.title, self.filetype)
            
            self.status_label.configure(text="Download complete!", text_color="#3cbd17") # Color is light green
            
        except error.URLError:
            self.status_label.configure(text="Error: Lost internet connection", text_color="red")

        except Exception as e:
            self.status_label.configure(
                text=f"Error during download: {str(e)}", 
                text_color="red"
            )