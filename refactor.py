from consts import RESOLUTIONS, FILETYPES
from video_class import Video



# Usage
try:
    
    
    costarica = Video("https://www.youtube.com/watch?v=BxdSUGBs0gM", "720p")
    get_user_input(costarica)
    print(costarica.url, costarica.resolution, costarica.filetype)
except Exception as e:
    print(f"Error: {e}")