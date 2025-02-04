

def file_to_binary(filepath):
    """
    Reads a file in binary mode and converts its content into a binary (0s and 1s) string.
    
    Args:
        filepath (str): The path to the file.
    
    Returns:
        str: A string representation of the file's binary content.
    """
    try:
        with open(filepath, 'rb') as file:
            binary_data = file.read()
            # Convert bytes to binary string
            binary_string = ''.join(format(byte, '08b') for byte in binary_data)
        return binary_string
    except FileNotFoundError:
        print("Error: File not found.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

