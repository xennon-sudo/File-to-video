import os

def merge_cunks(chunk_dir, output_file):
    """Merges files from the 'chunks' directory into the original file."""
    # Get a list of chunk files
    chunk_files = sorted([f for f in os.listdir(chunk_dir) if f.endswith('.bin')])

    with open(output_file, 'wb') as output_f:
        for chunk_file in chunk_files:
            chunk_path = os.path.join(chunk_dir, chunk_file)
            with open(chunk_path, 'rb') as chunk_f:
                output_f.write(chunk_f.read())

    print(f"Merged {len(chunk_files)} chunks into '{output_file}'")

if __name__ == "__main__":
    chunk_dir = "chunks"  # Directory containing the chunk files
    output_file = "merged_output.txt"  # Name of the merged output file

    print("Merging chunks...")
    merge_cunks(chunk_dir, output_file)
    print(f"Chunks merged into '{output_file}'")