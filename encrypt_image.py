from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from PIL import Image
import numpy as np
import os
import struct

def encrypt_image(image_path, key):
    # Ensure the key is 16 bytes long (AES requires a key of length 16, 24, or 32 bytes)
    key = str(key).ljust(16, ' ').encode('utf-8')[:16]
    
    # Read the image and convert it to a byte array
    img = Image.open(image_path)
    img_array = np.array(img)
    img_bytes = img_array.tobytes()
    
    img_mode = img.mode
    img_size = img.size  # (width, height)

    # Set up AES encryption with CBC mode and a random IV
    iv = os.urandom(16)  # Generate a random IV (Initialization Vector)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Pad the byte array to be a multiple of AES block size (16 bytes)
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(img_bytes) + padder.finalize()

    # Encrypt the padded data
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    # Save the encrypted data to a file, along with the IV and image metadata
    directory, filename = os.path.split(image_path)
    filename_without_ext, _ = os.path.splitext(filename)
    new_filename = f"encrypted_{filename_without_ext}.picr"
    new_file_path = os.path.join(directory, new_filename)
    
    with open(new_file_path, 'wb') as f:
        # Write the IV (16 bytes)
        f.write(iv)
        # Write the image mode (as a fixed 10-byte string)
        f.write(img_mode.ljust(10).encode('utf-8'))
        # Write the image dimensions (width and height as 4-byte integers)
        f.write(struct.pack('>II', img_size[0], img_size[1]))
        # Write the encrypted image data
        f.write(encrypted_data)

    print(f"Image encrypted and saved as {new_file_path}")
