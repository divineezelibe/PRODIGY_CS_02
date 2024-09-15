import argparse
from encrypt import encrypt_image
from decrypt import decrypt_image

def main():
    parser = argparse.ArgumentParser(description="Encrypt or decrypt an image.")
    parser.add_argument('-i', '--image', required=True, help="Path to the image file")
    parser.add_argument('-k', '--key', type=int, required=True, help="Key for encryption/decryption")
    parser.add_argument('--decrypt', action='store_true', help="Decrypt the image")

    args = parser.parse_args()
    image_path = args.image
    key = args.key

    if args.decrypt:
        decrypt_image("encrypted_" + image_path, key)
    else:
        encrypt_image(image_path, key)

if __name__ == "__main__":
    main()
