from PIL import Image
import numpy as np
import os

def decrypt_image(image_path, key):
    try:
        # Open the encrypted image and convert it to a numpy array
        img = Image.open(image_path)
        img_array = np.array(img)
        
        # Convert the array to a larger type to avoid overflow during subtraction
        img_array = img_array.astype(np.int32)
        
        # Perform decryption (subtraction of key) and ensure values are within the uint8 range
        decrypted_array = (img_array - key) % 256
        
        # Convert the decrypted array back to uint8
        decrypted_array = decrypted_array.astype(np.uint8)
        
        # Create an Image object from the decrypted array
        decrypted_img = Image.fromarray(decrypted_array)
        
        # Extract the directory, filename, and extension from the original image path
        directory, filename = os.path.split(image_path)
        filename_without_ext, file_extension = os.path.splitext(filename)
        
        # Create the new filename for the decrypted image
        new_filename = f"decrypted_{filename_without_ext}{file_extension}"
        
        # Ensure that the directory path is absolute and valid
        if not os.path.isdir(directory):
            raise FileNotFoundError(f"The directory {directory} does not exist.")
        
        new_image_path = os.path.join(directory, new_filename)
        
        # Save the decrypted image
        decrypted_img.save(new_image_path)
        print(f"Image decrypted and saved as {new_image_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
# decrypt_image("C:/Users/Divine Ezelibe/Pictures/svg/encrypted_DSC_0323.JPG", 50)
