import os
from img_gen import decode_img

def recover_binary_files(directory="extracted_frames", recovered_directory="recovered"):
    """
    Recover binary files from PNG images in the specified directory.

    Parameters:
    directory (str): The directory containing the extracted frames.
    recovered_directory (str): The directory to save the recovered binary files.
    """
    # Ensure the recovered directory exists
    if not os.path.exists(recovered_directory):
        os.makedirs(recovered_directory)

    # Get a list of all PNG files in the directory
    png_files = sorted([f for f in os.listdir(directory) if f.endswith('.png')])

    # Initialize a counter
    counter = 0

    # Iterate through the sorted list of PNG files
    for png_file in png_files:
        # Construct the full path to the PNG file
        png_path = os.path.join(directory, png_file)

        # Construct the output binary file name using the counter
        bin_file = os.path.join(recovered_directory, f"{counter}.bin")

        # Decode the image
        decode_img(png_path, bin_file)

        # Increment the counter
        counter += 1

# Example usage
if __name__ == "__main__":
    recover_binary_files()