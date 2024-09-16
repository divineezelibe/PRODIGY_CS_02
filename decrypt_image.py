from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from PIL import Image
import numpy as np
import os
import struct

def reverse_pixel_manipulation(manipulated_array):
    # Reverse the pixel manipulation (inverting the colors again)
    original_array = 255 - manipulated_array  # Invert pixel colors back
    return original_array

def decrypt_image(encrypted_image_path, key):
    # Ensure the key is 16 bytes long (AES requires a key of length 16, 24, or 32 bytes)
    key = str(key).ljust(16, ' ').encode('utf-8')[:16]

    # Open the encrypted file and read its contents
    with open(encrypted_image_path, 'rb') as f:
        # Read the IV (first 16 bytes)
        iv = f.read(16)
        # Read the image mode (next 10 bytes)
        img_mode = f.read(10).decode('utf-8').strip()
        # Read the image dimensions (next 8 bytes for width and height)
        img_width, img_height = struct.unpack('>II', f.read(8))
        # Read the remaining encrypted image data
        encrypted_data = f.read()

    # Set up AES decryption with the same key, IV, and CBC mode
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    # Decrypt the encrypted data
    decrypted_padded_data = decryptor.update(encrypted_data) + decryptor.finalize()

    # Unpad the decrypted data
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    decrypted_data = unpadder.update(decrypted_padded_data) + unpadder.finalize()

    # Convert the decrypted byte data back into an image array
    decrypted_array = np.frombuffer(decrypted_data, dtype=np.uint8)
    decrypted_array = decrypted_array.reshape((img_height, img_width, len(img_mode)))

    # Reverse the pixel manipulation (e.g., invert the colors back to the original)
    original_array = reverse_pixel_manipulation(decrypted_array)

    # Convert the array back to an image
    original_image = Image.fromarray(original_array, mode=img_mode)

    # Save the decrypted image
    directory, filename = os.path.split(encrypted_image_path)
    filename_without_ext, _ = os.path.splitext(filename)
    new_filename = f"decrypted_{filename_without_ext}.png"  # Save as PNG or any format you prefer
    new_file_path = os.path.join(directory, new_filename)
    original_image.save(new_file_path)

    #print(f"Your image is decrypted and saved as {new_file_path}")
