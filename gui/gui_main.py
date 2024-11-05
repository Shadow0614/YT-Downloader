import customtkinter as ctk

url = None
filetype = None
res = None

# Define functions that will be called when the URL, file type, and resolution are updated by the user
def url_update(var_name, index, mode):
    url = inp_url.get()
    # print(url) For debugging

def filetype_update(var_name, index, mode):
    filetype = inp_filetype.get()
    # print(filetype) For debugging

def res_update(var_name, index, mode):
    res = inp_res.get()
    # print(res) For debugging

# Create the main window
root = ctk.CTk()
root.title("YT Downloader V2.0")
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
url_label.grid(row=0, column=0, columnspan=2, pady=(10,0))

# Declare and watch the URL entry variable
inp_url = ctk.StringVar(value="")
inp_url.trace_add("write", url_update)

url_entry = ctk.CTkEntry(url_frame, width=350, textvariable=inp_url)
url_entry.grid(row=1, column=0, columnspan=2, pady=20)

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
inp_filetype = ctk.StringVar(value="mp4")
inp_filetype.trace_add("write", filetype_update)

# Set up radio buttons
radio1 = ctk.CTkRadioButton(inner_radio_frame, text="MP4 (Select this if you're not sure)", 
                           variable=inp_filetype, value="mp4")
radio2 = ctk.CTkRadioButton(inner_radio_frame, text="M4A", 
                           variable=inp_filetype, value="m4a")
radio3 = ctk.CTkRadioButton(inner_radio_frame, text="WEBM", 
                           variable=inp_filetype, value="webm")

# Position radio buttons vertically in the inner frame
radio1.grid(row=1, column=0, padx=10, pady=5, sticky="w")
radio2.grid(row=2, column=0, padx=10, pady=5, sticky="w")
radio3.grid(row=3, column=0, padx=10, pady=5, sticky="w")

# Create inner frame for dropdown menu
inner_dropdown_frame = ctk.CTkFrame(options_frame, fg_color="transparent")
inner_dropdown_frame.grid(row=0, column=3)

# Declare and watch the resolution variable
inp_res = ctk.StringVar(value="Select Resolution")
inp_res.trace_add("write", res_update)
                        
# Create and position dropdown menu                )
dropdown = ctk.CTkOptionMenu(inner_dropdown_frame, 
                           values=["144p", "Choice 2", "Choice 3"],
                           variable=inp_res,
                           width=200)
dropdown.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

# Create and position download button
button_frame = ctk.CTkFrame(root, fg_color="transparent")
button_frame.grid(row=2, column=0, columnspan=2)

# Center the download button
button_frame.grid_columnconfigure(0, weight=1)
button_frame.grid_columnconfigure(1, weight=1)

download_button = ctk.CTkButton(button_frame, text="Download", width=120, cursor="hand2")
download_button.grid(row=0, column=0, columnspan=2, pady=(0,10))

# Start the application
root.mainloop()