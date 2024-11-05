# Lets python recognize the YT Downloader folder as a package,
# so imports like "import main.av_linker" work properly.

import gui.gui_main as g

if __name__ == "__main__":
    g.root.mainloop() # Start the main loop