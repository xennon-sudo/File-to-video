import os

def split_file(input_file, chunk_size_mb=0.329, output_dir="chunks"):
    """Splits a file into 2.6MB chunks and saves them in the 'chunks' directory."""
    chunk_size_bytes = int(chunk_size_mb * 1024 * 1024)  # Convert MB to Bytes

    # Create chunks directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    chunk_files = []
    with open(input_file, 'rb') as f:
        chunk_index = 0
        while True:
            chunk = f.read(chunk_size_bytes)
            if not chunk:
                break
            chunk_file = os.path.join(output_dir, f'{chunk_index}.bin')
            with open(chunk_file, 'wb') as chunk_f:
                chunk_f.write(chunk)
            chunk_files.append(chunk_file)
            chunk_index += 1

    return chunk_files

if __name__ == "__main__":
    input_file = "input.txt"  # Ensure this file exists
    output_dir = "chunks"

    print("Splitting file...")
    chunk_files = split_file(input_file, output_dir=output_dir)
    print(f"File split into {len(chunk_files)} chunks, saved in '{output_dir}/'")