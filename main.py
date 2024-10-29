import pytubefix as pt


# Filters the video based on the provided link, quality, and file type
def filter_video(vid_link, quality, file_type) -> pt.query.StreamQuery: # Should return a StreamQuery object, similar to a list
    try:
        vid = pt.YouTube(vid_link)

    except TypeError:
        print("Error: YouTube link is invalid")
        return None
    
    except Exception as e:
        print(f"Error: {e}")
        return None

    if file_type == "": # If file type was not specified by user, set file type to mp4
        file_type = "mp4"

    if quality == "":
        quality = vid.streams.get_highest_resolution(progressive = False).resolution # If quality was not specified by user, set quality to highest resolution available
        filtered_streams = vid.streams.filter(res = quality, file_extension = file_type)

    else:
        filtered_streams = vid.streams.filter(res = quality, file_extension = file_type)
    
    # If type of vid is correct, filter streams with the specified quality and file type, and return filtered streams
    return filtered_streams




# Main function to take user input for video link, quality, and file type
# Variables are global to be accessible in the filter_video function call below. -> GLOBAL VARIABLES ARE NOT NECESSARY IF LINES 67-71 ARE INSIDE OF MAIN FUNCTION
def main():
    # Prompts user for a YouTube video link
    # Video link is set to the variable 'vid_link'
    # global vid_link
    while True:
        vid_link = input("Enter YouTube video link: ")

        if "youtube.com/watch?" in vid_link or "youtu.be/" in vid_link:
            break

        print("\nInvalid YouTube link. Please enter a valid link.")


    # Prompts user for desired video quality
    # Video quality is set to the variable 'q'
    # global q
    while True:
        q = input("Enter desired video quality, if known (Ex: 720p, 1080p, 1440p, etc). Press enter to skip: ")

        if q in ["144p", "240p", "360p", "720p", "1080p", "1440p", "2160p"]:
            break

        elif q == "": # Break if user doesn't want to specify a quality
            break

        print("\nInvalid video quality. Please enter a valid quality. Press enter to skip.")


    # Prompts user for desired file type
    # File type is set to the variable 'file_type'
    # global file_type
    while True:
        file_type = input("Enter desired file type, if known (Ex: mp4, m4a, webm). Press enter to skip: ")

        if file_type in ["mp4", "m4a", "webm"]:
            break

        elif file_type == "": # Break if user doesn't want to specify a file type
            break

        print("\nInvalid file type. Please enter a valid file type. Press enter to skip.")
        print(f"Selected file type: {file_type}")

    
    hello = filter_video(vid_link, q, file_type)
    video = hello.get_highest_resolution(progressive = False)

    video.download()




if __name__ == "__main__":
    main()