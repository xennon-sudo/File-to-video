from img_gen import gen_image, decode_img
import os
import re
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def render_frame():
    # 📁 Ensure the directories exist
    if not os.path.exists("./chunks"):
        logging.error("Error: 'chunks' directory does not exist. 🚫")
        return

    if not os.path.exists("./images"):
        os.makedirs("./images")
        logging.info("Created 'images' directory. 📁")

    # List all files in the directory
    file_list = os.listdir("./chunks")
    logging.info(f"Found {len(file_list)} files in 'chunks' directory. 📂")

    # Define a sorting key function that extracts the numeric part of the filename
    def sort_key(filename):
        match = re.match(r'(\d+)\.bin', filename)
        if match:
            return int(match.group(1))
        return float('inf')  # Ensure non-matching filenames are sorted last

    # Sort the file list using the custom key function
    file_list.sort(key=sort_key)
    logging.info("Sorted file list. 🔢")

    index = 0
    for f in file_list:
        if f.endswith('.bin'):
            try:
                # Construct the full path to the .bin file
                bin_file_path = os.path.join("./chunks", f)
                gen_image(bin_file_path, f"images/{index}.png")
                logging.info(f"Processed file {f} to images/{index}.png 🖼️")
                index += 1
            except Exception as e:
                logging.error(f"Error processing file {f}: {e} ❌")
        else:
            logging.warning(f"Skipping non-bin file: {f} 🚫")

if __name__ == "__main__":
    render_frame()