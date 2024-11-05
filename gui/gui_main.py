import customtkinter as ctk
from gui.video_class import Video


# Define functions that will be called when user clicks the download button
def download_clicked(var_name=None, index=None, mode=None):
    """Runs when download button is clicked"""
    video = Video(url.get(), res.get(), filetype.get(), url_status_label)
    video.download()

def update_resolutions(var_name=None, index=None, mode=None):
    """Update resolutions in dropdown when URL or filetype changes"""
    video = Video(url.get(), res.get(), filetype.get(), url_status_label)
    resolutions = video.get_available_resolutions()
    dropdown.configure(values=resolutions)
    res.set("Select Resolution") # Reset selected resolution to default when URL or filetype changes
        
    # res.set(resolutions[0]) # Sets the resolution to the first available resolution in the dropdown when URL or filetype is changed

# Create the main window
root = ctk.CTk()
root.title("YT Downloader v2.0")
icon_path = r"_internal\gui\tesseract.ico" # When exported as an exe file with pyinstaller
# icon_path = "gui\tesseract.ico" # When running source code directly
root.iconbitmap(icon_path)
root.geometry("750x480")

# Configure equal column widths and center vertically
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)  # Space above url_frame
root.grid_rowconfigure(1, weight=1)  # url_frame
root.grid_rowconfigure(2, weight=1)  # options_frame
root.grid_rowconfigure(3, weight=1)  # download button
# root.grid_rowconfigure(4, weight=1)  # Space below download button

# Create and position the URL entry section
url_frame = ctk.CTkFrame(root, fg_color="transparent")
url_frame.grid(row=0, column=0, columnspan=2)

# Center the URL entry components
url_frame.grid_columnconfigure(0, weight=1)
url_frame.grid_columnconfigure(1, weight=1)

# Add URL label and entry
url_label = ctk.CTkLabel(url_frame, text="Enter YouTube Video URL:")
url_label.grid(row=0, column=0, columnspan=2, pady=(0,0))

# Declare and watch the URL entry variable
url = ctk.StringVar(value="")
url.trace_add("write", update_resolutions)

url_entry = ctk.CTkEntry(url_frame, width=350, textvariable=url)
url_entry.grid(row=1, column=0, columnspan=2, pady=20)

url_status_label = ctk.CTkLabel(url_frame, text="", text_color="red", font=("Monaspace Neon", 14, "normal"))
url_status_label.grid(row=2, column=0, columnspan=2, pady=0)

# Create main options frame
options_frame = ctk.CTkFrame(root, fg_color="transparent")
options_frame.grid(row=1, column=0, columnspan=2, sticky="nsew")

# Configure options frame columns for equal spacing
options_frame.grid_columnconfigure(0, weight=1)  # Left padding
options_frame.grid_columnconfigure(1, weight=1)  # First inner frame
options_frame.grid_columnconfigure(2, weight=1)  # Space between frames
options_frame.grid_columnconfigure(3, weight=1)  # Second inner frame
options_frame.grid_columnconfigure(4, weight=1)  # Right padding

# Create inner frame for radio buttons
inner_radio_frame = ctk.CTkFrame(options_frame, fg_color="transparent")
inner_radio_frame.grid(row=0, column=1)

# Center the inner radio frame
options_frame.grid_rowconfigure(0, weight=1)

# Add label above radio buttons
radio_label = ctk.CTkLabel(inner_radio_frame, text="Select File Type")
radio_label.grid(row=0, column=0, padx=10, pady=(0,10))

# Declare and watch the file type variable
filetype = ctk.StringVar(value="mp4")
filetype.trace_add("write", update_resolutions)

# Set up radio buttons
radio1 = ctk.CTkRadioButton(inner_radio_frame, text="MP4 (Select this if you're not sure)", 
                           variable=filetype, value="mp4")
radio2 = ctk.CTkRadioButton(inner_radio_frame, text="M4A", 
                           variable=filetype, value="m4a")
radio3 = ctk.CTkRadioButton(inner_radio_frame, text="WEBM", 
                           variable=filetype, value="webm")

# Position radio buttons vertically in the inner frame
radio1.grid(row=1, column=0, padx=10, pady=5, sticky="w")
radio2.grid(row=2, column=0, padx=10, pady=5, sticky="w")
radio3.grid(row=3, column=0, padx=10, pady=5, sticky="w")

# Create inner frame for dropdown menu
inner_dropdown_frame = ctk.CTkFrame(options_frame, fg_color="transparent")
inner_dropdown_frame.grid(row=0, column=3)

# Declare and watch the resolution variable
res = ctk.StringVar(value="Select Resolution")
                        
# Create and position dropdown menu                )
dropdown = ctk.CTkOptionMenu(inner_dropdown_frame, 
                           values=["Select Resolution"],
                           variable=res,
                           width=200)
dropdown.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

# Create and position download button
button_frame = ctk.CTkFrame(root, fg_color="transparent")
button_frame.grid(row=2, column=0, columnspan=2)

# Center the download button
button_frame.grid_columnconfigure(0, weight=1)
button_frame.grid_columnconfigure(1, weight=1)

# Configure download button
download_button = ctk.CTkButton(button_frame, text="Download", width=140, cursor="hand2", command=download_clicked)
download_button.grid(row=0, column=0, columnspan=2, pady=(0,10))

# Start the application
if __name__ == "__main__":
    root.mainloop()