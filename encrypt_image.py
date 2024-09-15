from PIL import Image
import numpy as np
import os

def encrypt_image(image_path, key):
    # Open the image and convert it to a numpy array
    img = Image.open(image_path)
    img_array = np.array(img)
    
    # Convert the array to a larger type to avoid overflow during addition
    img_array = img_array.astype(np.int32)
    
    # Perform encryption (addition of key) and ensure values are within the uint8 range
    encrypted_array = (img_array + key) % 256
    
    # Convert the encrypted array back to uint8
    encrypted_array = encrypted_array.astype(np.uint8)
    
    # Create an Image object from the encrypted array
    encrypted_img = Image.fromarray(encrypted_array)
    
    # Extract the filename and directory from the original image path
    directory, filename = os.path.split(image_path)
    filename_without_ext, file_extension = os.path.splitext(filename)
    
    # Create the new filename for the encrypted image
    new_filename = f"encrypted_{filename_without_ext}{file_extension}"
    new_image_path = os.path.join(directory, new_filename)
    
    # Save the encrypted image
    encrypted_img.save(new_image_path)
    print(f"Image encrypted and saved as {new_image_path}")

# Example usage:
# encrypt_image("C:/Users/Divine Ezelibe/Pictures/svg/DSC_0323.JPG", 50)
