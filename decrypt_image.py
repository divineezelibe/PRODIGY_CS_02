from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from PIL import Image
import numpy as np
import struct  # Ensure this line is included to handle binary data packing/unpacking

def decrypt_image(encrypted_image_path, key):
    # Ensure the key is 16 bytes long (AES requires a key of length 16, 24, or 32 bytes)
    key = str(key).ljust(16, ' ').encode('utf-8')[:16]

    # Read the encrypted file
    with open(encrypted_image_path, 'rb') as f:
        iv = f.read(16)  # The first 16 bytes are the IV
        img_mode = f.read(10).strip().decode('utf-8')  # Read the next 10 bytes for the image mode
        img_width, img_height = struct.unpack('>II', f.read(8))  # Read the next 8 bytes for image dimensions (width, height)
        encrypted_data = f.read()  # The rest is the encrypted image data

    # Set up AES decryption with CBC mode
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    # Decrypt the data
    decrypted_padded_data = decryptor.update(encrypted_data) + decryptor.finalize()

    # Remove padding
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    decrypted_data = unpadder.update(decrypted_padded_data) + unpadder.finalize()

    # Reshape the decrypted byte data into the correct format
    decrypted_array = np.frombuffer(decrypted_data, dtype=np.uint8)
    
    if img_mode == 'RGB':
        decrypted_array = decrypted_array.reshape((img_height, img_width, 3))  # for RGB images
    elif img_mode == 'L':
        decrypted_array = decrypted_array.reshape((img_height, img_width))  # for grayscale images
    else:
        raise ValueError(f"Unsupported image mode: {img_mode}")

    # Convert the array back to an image and save it
    decrypted_img = Image.fromarray(decrypted_array, img_mode)
    decrypted_img_path = encrypted_image_path.replace("encrypted_", "decrypted_").replace('.picr', '.png')
    decrypted_img.save(decrypted_img_path)

    print(f"Image decrypted and saved as {decrypted_img_path}")
