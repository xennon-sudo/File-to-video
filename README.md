# File Encoder/Decoder 🔒🔓

This repository contains a set of Python scripts to encode and decode files by splitting them into chunks, rendering frames, and creating videos from the frames. The decoded files can be merged back into their original form.

## Features 🌟

- **Encode**: Splits a file into chunks, renders frames, and creates a video from the frames.
- **Decode**: Extracts frames from a video, recovers binary files, and merges the chunks back into the original file.
- **Logging**: Detailed logging for better debugging and tracking.

## Requirements 📦

- Python 3.6+
- `img_gen.py` module (custom module for image generation and decoding)
- `spliter.py` module (custom module for splitting and merging files)
- `merge.py` module (custom module for merging chunks)

## Installation 🛠️

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
   ```

2. Install the required Python packages:
   ```sh
   pip install -r requirements.txt
   ```

## Usage 🚀

### Encoding a File

To encode a file, use the `encode` function in `app.py`:

```python
from app import encode

encode('path/to/your/file.txt')
```

### Decoding a File

To decode a file, use the `decode` function in `app.py`:

```python
from app import decode

decode()
```

## File Structure 📁

- `app.py`: Main script containing `encode` and `decode` functions.
- `frame_creator.py`: Script to render frames from binary chunks.
- `img_gen.py`: Module for generating and decoding images.
- `merge.py`: Module for merging chunks back into the original file.
- `spliter.py`: Module for splitting files into chunks and merging chunks back into files.
- `requirements.txt`: List of required Python packages.

## Limitations 🚫

- The encoding and decoding processes are designed for binary files and may not work correctly with text files.
- The `img_gen.py` module is a custom module and must be implemented separately.
- The `spliter.py` module is a custom module and must be implemented separately.
- The `merge.py` module is a custom module and must be implemented separately.

## Contributing 🤝

Contributions are welcome! Please open an issue or submit a pull request.

## License 📜

This project is licensed under the MIT License. 



## Installation 🛠️

1. Clone the repository:
   ```sh
   git clone https://github.com/xennon-sudo/File-to-video.git
   cd File-to-video
   ```

2. Install the required Python packages:
   ```sh
   pip install -r requirements.txt
   ```

## Usage 🚀

Certainly! Below is a guide on how to use the `app.py` script for encoding and decoding files using video frames.

### Prerequisites
Ensure you have the necessary modules and dependencies installed. You can install any missing dependencies using `pip`:

```sh
pip install -r requirements.txt
```

### Usage

#### Encoding a File

To encode a file, you need to specify the `encode` action and provide the path to the file you want to encode.

```sh
python app.py encode --file path/to/your/file.txt
```

- `encode`: Specifies that you want to encode a file.
- `--file`: The path to the file you want to encode.

#### Decoding a File

To decode a file, you need to specify the `decode` action. The script will assume that the video frames are already extracted and stored in the appropriate directories.

```sh
python app.py decode
```

- `decode`: Specifies that you want to decode a file.

### Example

#### Encoding Example

Suppose you have a file named `example.txt` located in the current directory. You can encode this file using the following command:

```sh
python app.py encode --file example.txt
```

#### Decoding Example

To decode a previously encoded file, simply run:

```sh
python app.py decode
```

### Directory Structure

Ensure that the script has the necessary directories to store intermediate files:

- `./chunks`: Temporary directory to store file chunks during encoding.
- `./images`: Temporary directory to store rendered frames during encoding.
- `./extracted_frames`: Directory to store extracted frames during decoding.
- `./recovered`: Directory to store recovered binary files during decoding.

### Cleanup

After encoding or decoding, the script will clean up the temporary directories (`./chunks`, `./images`, and `./extracted_frames`). Ensure that these directories are not needed for other purposes before running the script.

### Notes

- Make sure the video frames and extracted frames are correctly placed in the specified directories for decoding to work properly.
- The script assumes that the necessary modules (`split_file`, `render_frame`, `create_video_from_images`, `extract_frames_from_video`, `recover_binary_files`, `merge_cunks`) are correctly implemented and available in the `modules` directory.

By following these instructions, you should be able to encode and decode files using the `app.py` script effectively.

## File Structure 📁

- `app.py`: Main script containing `encode` and `decode` functions.
- `frame_creator.py`: Script to render frames from binary chunks.
- `img_gen.py`: Module for generating and decoding images.
- `merge.py`: Module for merging chunks back into the original file.
- `spliter.py`: Module for splitting files into chunks and merging chunks back into files.
- `requirements.txt`: List of required Python packages.

## Limitations 🚫

- The encoding and decoding processes are designed for binary files and may not work correctly with text files.
- The `img_gen.py` module is a custom module and must be implemented separately.
- The `spliter.py` module is a custom module and must be implemented separately.
- The `merge.py` module is a custom module and must be implemented separately.

