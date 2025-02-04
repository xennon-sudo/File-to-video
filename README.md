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

