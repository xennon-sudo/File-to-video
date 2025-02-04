# Importing necessary modules to prepare the app 📦
from modules.split import split_file  # 🎰 FOR SLICING APP
from modules.frame_creator import render_frame
from modules.video import create_video_from_images, extract_frames_from_video
from modules.frame_decoder import recover_binary_files
import shutil
from modules.merge import merge_cunks
import argparse
import os       
# 🔵 TEXT INPUTS
# Removed the input() function as we will use argparse for command-line arguments

# 🌝 Defining Encode functions
def encode(file_path):
    """
    Encodes a file by splitting it into chunks, rendering frames, and creating a video from the frames.
    """
    split_file(input_file=file_path)
    render_frame()
    create_video_from_images()
    shutil.rmtree("./chunks")
    shutil.rmtree("./images")

def decode():
    """
    Decodes a video by extracting frames, recovering binary files, and merging the chunks back into the original file.
    """
    extract_frames_from_video()
    recover_binary_files()
    merge_cunks("./recovered", "x.txt")
    shutil.rmtree("./extracted_frames")
    os.mkdir("./extracted_frames")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Encode or decode a file using video frames.")
    parser.add_argument('action', choices=['encode', 'decode'], help="Action to perform: 'encode' or 'decode'")
    parser.add_argument('--file', help="Path to the file to encode")

    args = parser.parse_args()

    if args.action == 'encode':
        if not args.file:
            parser.error("The --file argument is required for encoding.")
        encode(args.file)
    elif args.action == 'decode':
        decode()