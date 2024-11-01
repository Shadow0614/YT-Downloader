import os
import shutil

def delete_temp():
    root_dir = os.path.dirname(os.path.abspath(__file__)) # Directory where this python file is located
    temp_folder_path = os.path.join(root_dir, 'temp') # Joins temp folder to the root directory path

    if os.path.exists(temp_folder_path) and os.path.isdir(temp_folder_path): # Checks if temp folder exists and is a directory
        shutil.rmtree(temp_folder_path) # Deletes temp folder and all its contents

if __name__ == "__main__":
    delete_temp()