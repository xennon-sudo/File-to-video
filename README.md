# File Encoder/Decoder 🔒🔓

This repository provides Python scripts to encode and decode files by converting them into video frames. This method allows files to be stored as videos, offering an alternative form of storage.

## Features 🌟

- **Encoding**: Splits files into chunks, converts them into frames, and compiles a video from those frames.
- **Decoding**: Extracts frames from a video, reconstructs the binary data, and merges it back into the original file.
- **Logging**: Provides detailed logging for debugging and tracking progress.

## Requirements 📦

- Python 3.6+
- Required modules:
  - `img_gen.py` (handles image generation and decoding)
  - `spliter.py` (handles file splitting and merging)
  - `merge.py` (handles merging file chunks)

## Installation 🛠️

1. Clone the repository:
   ```sh
   git clone https://github.com/xennon-sudo/File-to-video.git
   cd File-to-video
   ```
2. Install required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage 🚀

### Encoding a File

To encode a file into a video:
```sh
python app.py encode --file path/to/your/file.txt
```
- `encode`: Specifies the encoding process.
- `--file`: Path to the file you want to encode.

### Decoding a File

To decode a video back into the original file:
```sh
python app.py decode
```
- `decode`: Specifies the decoding process.

### Example Usage

#### Encoding Example
To encode a file named `example.txt`:
```sh
python app.py encode --file example.txt
```

#### Decoding Example
To decode a previously encoded file:
```sh
python app.py decode
```

### Directory Structure 📁

- `./chunks/` - Stores file chunks during encoding.
- `./images/` - Stores rendered frames during encoding.
- `./extracted_frames/` - Stores extracted frames during decoding.
- `./recovered/` - Stores recovered binary files after decoding.

### Cleanup 🧹

After encoding or decoding, temporary directories (`./chunks`, `./images`, `./extracted_frames`) are cleaned up automatically. Ensure these directories are not needed before running the script.

### Notes 📌

- Ensure the video frames and extracted frames are placed in the correct directories for decoding to work properly.
- The script depends on custom modules (`img_gen.py`, `spliter.py`, `merge.py`), which must be properly implemented.

## File Structure 📁

- `app.py` - Main script containing encoding and decoding functions.
- `frame_creator.py` - Handles rendering frames from binary chunks.
- `img_gen.py` - Handles image generation and decoding.
- `merge.py` - Merges chunks back into the original file.
- `spliter.py` - Splits files into chunks and merges them back.
- `requirements.txt` - List of required Python packages.

## Limitations 🚫

- The encoding and decoding process is optimized for binary files; text files may require additional processing.
- The custom modules (`img_gen.py`, `spliter.py`, `merge.py`) must be implemented separately.

## Contributing 🤝

Contributions are welcome! Feel free to open an issue or submit a pull request.

## License 📜

This project is licensed under the MIT License.
