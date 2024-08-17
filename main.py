import os

# Get the name of the file from the user
filename = input("Enter the name of the file: ")

# Construct the path to the file based on the script's location
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename) + ".txt"

# Open the file and read the contents
with open(file_path, 'r') as file:
    # Loop through each line in the file
    for line in file:
        # Remove any whitespace from the beginning and end of the line
        line = line.strip()
        if line[0:19] == 'https://youtube.com':
            command = f'yt-dlp {line} --recode-video mp4 --paths {filename}/'
        # If the line is not empty
        else:
            # Extract the clip ID from the line
            clip_id = line.split('/')[-1].split('?')[0]
            # Construct the command to download the clip
            command = f"/Users/matthewgreene/TwitchDownloaderCLI clipdownload --id {clip_id} -o {filename}/{clip_id}.mp4"
            # Run the command in the terminal
        os.system(command)