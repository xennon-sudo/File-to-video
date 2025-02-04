import numpy as np
import cv2
import os
from tqdm import tqdm
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def decode_img(image_path, output_file_path):
    """
    Decode an image using the size header to remove padding.
    """
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"The image at {image_path} does not exist.")

    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"Could not read the image at {image_path}.")

    height, width, _ = img.shape
    binary_str = []

    # Extract binary string from image
    for y in tqdm(range(height), desc="Decoding image"):
        for x in range(width):
            b, g, r = img[y, x]
            r_bit = '0' if r == 0 else '1'
            g_bit = '0' if g == 0 else '1'
            b_bit = '0' if b == 0 else '1'
            binary_str.extend([r_bit, g_bit, b_bit])

    binary_str = ''.join(binary_str)

    # Split into bytes
    byte_array = bytearray()
    for i in range(0, len(binary_str), 8):
        byte_bits = binary_str[i:i+8]
        byte = int(byte_bits, 2)
        byte_array.append(byte)

    # Extract size from the first 4 bytes (header)
    original_size = int.from_bytes(byte_array[:4], byteorder='big')
    decoded_data = byte_array[4:4+original_size]  # Truncate to original size

    # Write to file
    with open(output_file_path, 'wb') as f:
        f.write(decoded_data)

    logging.info(f"INFO! Decoded data written to {output_file_path}")

def gen_image(file_path, output_path, width=1280, height=720):
    """
    Convert a file to a binary string (with size header) and encode it into an image.
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file at {file_path} does not exist.")

    with open(file_path, 'rb') as f:
        binary_data = f.read()

    # Add 4-byte header containing the original data size (big-endian)
    original_size = len(binary_data)
    size_header = original_size.to_bytes(4, byteorder='big')
    binary_data = size_header + binary_data  # Prepend header to data

    # Convert to binary string
    binary_str = ''.join(format(byte, '08b') for byte in binary_data)

    # Calculate required length and pad with zeros
    required_length = width * height * 3
    if len(binary_str) > required_length:
        raise ValueError(f"Data too large for image: {len(binary_str)} > {required_length}")
    binary_str = binary_str.ljust(required_length, '0')

    # Create and populate image
    image = np.zeros((height, width, 3), dtype=np.uint8)
    for y in tqdm(range(height), desc="Generating image"):
        for x in range(width):
            index = (y * width + x) * 3
            r = int(binary_str[index], 2) * 255
            g = int(binary_str[index + 1], 2) * 255
            b = int(binary_str[index + 2], 2) * 255
            image[y, x] = [b, g, r]

    cv2.imwrite(output_path, image)
    logging.info(f"INFO:👍  Image generated and saved to {output_path}")

if __name__ == "__main__":
    # Example usage
    input_file = 'x.png'
    output_image = 'output.png'
    decoded_file = 'decoded.txt'

    gen_image(input_file, output_image)
    decode_img(output_image, decoded_file)