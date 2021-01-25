"""
Batch mp4 to mp3 Converter
Created by Caleb E.
date: Jan 2020

"""

from moviepy.editor import *

def find_mp4(mp4_folder_location, mp3_folder_location):

    for root, dirs, files in os.walk(mp4_folder_location):
        for filename in files:
            print(filename[:-4])
            # find mp4
            print(os.path.join(mp4_folder_location, filename))
            video = VideoFileClip(os.path.join(mp4_folder_location, filename))

            video.audio.write_audiofile(os.path.join(mp3_folder_location,filename[:-4]+".mp3"))


# Where the mp4 files are:
mp4_folder_location = "YOUR MP4 FOLDER HERE"

# Where you would like to covert the new mp3 files to
mp3_folder_location = "YOUR MP3 FOLDER HERE"


find_mp4(mp4_folder_location, mp3_folder_location)
