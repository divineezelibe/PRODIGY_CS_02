from PIL import Image
import numpy as np

def encrypt_image(image_path, key):
    img = Image.open(image_path)
    img_array = np.array(img)
    
    encrypted_array = (img_array + key) % 256
    
    encrypted_img = Image.fromarray(encrypted_array.astype(np.uint8))
    encrypted_img.save("encrypted_" + image_path)
    print(f"Image encrypted and saved as encrypted_{image_path}")
