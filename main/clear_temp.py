import os
import shutil

# This file is imported and run in av_linker.py

def delete_temp():
    """Deletes temp folder and all its contents"""
    main_folder_path = os.path.dirname(os.path.abspath(__file__)) # Directory where this python file is located
    project_dir = os.path.dirname(main_folder_path) # Directory where main, gui, temp folders are located
    temp_folder_path = os.path.join(project_dir, 'temp') # Joins temp folder to the root directory path

    if os.path.exists(temp_folder_path) and os.path.isdir(temp_folder_path): # Checks if temp folder exists and is a directory
        shutil.rmtree(temp_folder_path) # Deletes temp folder and all its contents
        print("Deleted temp folder")

if __name__ == "__main__":
    delete_temp()