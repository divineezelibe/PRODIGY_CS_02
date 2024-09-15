from PIL import Image
import numpy as np

def decrypt_image(encrypted_image_path, key):
    img = Image.open(encrypted_image_path)
    img_array = np.array(img)
    
    decrypted_array = (img_array - key) % 256
    
    decrypted_img = Image.fromarray(decrypted_array.astype(np.uint8))
    decrypted_img.save("decrypted_" + encrypted_image_path)
    print(f"Image decrypted and saved as decrypted_{encrypted_image_path}")
