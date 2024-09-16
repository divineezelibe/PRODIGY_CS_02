import argparse
from encrypt_image import encrypt_image
from decrypt_image import decrypt_image

def print_intro():
    print("""
    ************************************************
    *                                             *
    *                                           *
    *    Thank you for trying PixCrypt!       * 
    *                                           *
    *                                             *
    ************************************************
    """)

def print_success_message(operation, image_path):
    print(f"""                            
      {operation.capitalize()} Successful!       
                                             
      Your image has been {operation}d and saved 
      successfully.                              
                                                 
      File: {image_path}                         
    
    ***********************************************
    """)

def main():
    print_intro()
    
    parser = argparse.ArgumentParser(description="Encrypt or decrypt an image.")
    parser.add_argument('-i', '--image', required=True, help="Path to the image file")
    parser.add_argument('-k', '--key', type=int, required=True, help="Key for encryption/decryption")
    parser.add_argument('--decrypt', action='store_true', help="Decrypt the image")

    args = parser.parse_args()
    image_path = args.image
    key = args.key

    if args.decrypt:
        decrypt_image(image_path, key)
        print_success_message("decrypt", image_path)
    else:
        encrypt_image(image_path, key)
        print_success_message("encrypt", image_path)

if __name__ == "__main__":
    main()
