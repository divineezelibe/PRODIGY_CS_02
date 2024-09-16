# PixCrypt

**PixCrypt** is a Python-based image encryption and decryption tool that combines pixel manipulation with full-image encryption. It allows users to securely encrypt their images and later decrypt them for viewing, making it ideal for protecting sensitive visual data. This project uses the AES encryption algorithm from the `cryptography` library.

## Project Structure

```bash
PixCrypt/
│
├── setup/                    # Setup files for different platforms
│   ├── unix/
│   │   └── setup.sh          # Unix setup script to install dependencies
│   ├── windows/
│   │   └── setup.bat         # Windows setup script to install dependencies
│   └── requirements.txt      # Python dependencies file
│
├── PixCrypt.py               # Main entry point for the program
├── decrypt_image.py          # Decryption logic for encrypted images
├── encrypt_image.py          # Encryption logic with pixel manipulation
├── AUTHORS                   # List of authors and contributors
├── LICENSE                   # License information (MIT)
└── README.md                 # This README file
```

## Features

- **Pixel Manipulation**: The encryption process manipulates pixels before performing full encryption, adding an extra layer of security.
- **AES Encryption**: Uses Advanced Encryption Standard (AES) with CBC mode for robust security.
- **Cross-platform Setup**: Automated setup for both Unix/Linux (`setup.sh`) and Windows (`setup.bat`) environments.
- **Metadata Preservation**: The encrypted file contains image metadata such as dimensions and mode, ensuring accurate restoration after decryption.

Sure, here's a shorter version:

---

## How It Works

PixCrypt encrypts and decrypts images to keep them secure.

### Encryption

1. **Open the Image**: Read the image and get its pixel data.
2. **Manipulate Pixels**: Slightly change the pixel data for added security.
3. **Encrypt**: Use a secret key to scramble the pixel data with AES encryption.
4. **Save**: Save the encrypted data along with extra info needed for decryption.

### Decryption

1. **Open Encrypted File**: Read the encrypted file and extract necessary info.
2. **Decrypt**: Use the secret key to unscramble the data.
3. **Restore Image**: Rebuild the image from the decrypted data and save it.

In essence, PixCrypt secures your images by manipulating the pixels and  encrypting them and can later decrypt them and then reverse the manipulations to restore the original image.

---

This should provide a clear and concise overview of how PixCrypt works!

## Prerequisites

Ensure that you have the following installed on your system:

- Python 3.8 or higher
- `pip` (Python package manager)

If you don't have Python installed, download and install it from [python.org](https://www.python.org/downloads/).

## Setup Instructions

### Automated Setup

#### Windows

1. Open a terminal (Command Prompt or PowerShell).
2. Run the following command to automatically set up dependencies:
   ```bash
   setup\windows\setup.bat
   ```

#### Unix/Linux

1. Open a terminal.
2. Run the following command to automatically install the required dependencies:
   ```bash
   bash setup/unix/setup.sh
   ```

The setup scripts will automatically install all required dependencies using `pip` and ensure your environment is ready for use.

### Manual Setup

If you prefer manual installation, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/divineezelibe/PRODIGY_CS_02.git
   cd PRODIGY_CS_02
   ```

2. Install dependencies:
   ```bash
   pip install -r setup/requirements.txt
   ```

## Usage

### Encrypt an Image

To encrypt an image, run the following command in your terminal:

```bash
python PixCrypt.py -i "<path_to_image>" -k <encryption_key>
```

- `<path_to_image>`: Path to the image you want to encrypt.
- `<encryption_key>`: Key used for encryption (AES).

Example:

```bash
python PixCrypt.py -i "C:\Users\Username\Pictures\image.png" -k 12345 --encrypt
```

### Decrypt an Image

To decrypt an encrypted image, use the following command:

```bash
python PixCrypt.py -i "<path_to_encrypted_image>" -k <encryption_key> --decrypt
```

- `<path_to_encrypted_image>`: Path to the encrypted image.
- `<encryption_key>`: Key used during encryption.

Example:

```bash
python PixCrypt.py -i "C:\Users\Username\Pictures\encrypted_image.picr" -k 12345 --decrypt
```

## Notes

1. **Key Length**: AES requires keys of 16, 24, or 32 bytes. Your key will automatically be padded to 16 bytes if shorter.
2. **File Format**: Encrypted files are saved in `.picr` format. Ensure you use the correct encryption key when decrypting.
3. **Image Modes**: Currently, only images with certain modes (like 'RGB') are supported. If you encounter an unsupported mode, you may need to convert the image before encrypting.

## Dependencies

PixCrypt relies on the following Python packages:

- `cryptography`: For encryption and decryption (AES with CBC mode).
- `Pillow`: For image processing.
- `numpy`: For efficient array handling.

## Authors

- Divine Ezelibe – [GitHub](https://github.com/divineezelibe) | [LinkedIn](https://linkedin.com/in/divine-ezelibe) | Email: divineezelibe.e@gmail.com

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

