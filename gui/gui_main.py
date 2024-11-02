import customtkinter as ctk

# Initialize the main window
app = ctk.CTk()
app.title("YT Downloader v1.0")
app.geometry("800x600")

# URL Entry
url_label = ctk.CTkLabel(app, text="YouTube URL:")
url_label.pack(pady=(60,20))
url_entry = ctk.CTkEntry(app, width=300)
url_entry.pack(pady=5)

# Download Button
download_button = ctk.CTkButton(app, text="Download", command=None)
download_button.pack(pady=20)

# Status Label
status_label = ctk.CTkLabel(app, text="")
status_label.pack(pady=10)

# Run the application
app.mainloop()