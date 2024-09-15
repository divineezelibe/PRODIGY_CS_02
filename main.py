"""
main.py - A command-line tool for encrypting and decrypting images using pixel manipulation.

This script allows you to encrypt or decrypt an image file by applying a simple mathematical operation
to the pixel values. You can use the `-i` option to specify the path to the image file and the `-k` option
to provide a key for the encryption or decryption process. Use the `--decrypt` flag to decrypt an image
that was previously encrypted.

Usage:
    python3 main.py -i <image_path> -k <key> [--decrypt]

Options:
    -h, --help          Show this help message and exit.
    -i <image_path>, --image <image_path>
                        Path to the image file that you want to encrypt or decrypt.
    -k <key>, --key <key>
                        Key for encryption or decryption. It should be an integer.
    --decrypt           Decrypt the image. If this flag is provided, the script will decrypt the
                        image specified by the -i option. Without this flag, the script will
                        encrypt the image.

Examples:
    Encrypt an image:
        python3 main.py -i example_image.jpg -k 100

        This command will encrypt the image `example_image.jpg` with a key of 100 and save the result
        as `encrypted_example_image.jpg`.

    Decrypt an image:
        python3 main.py -i example_image.jpg -k 100 --decrypt

        This command will decrypt the image `encrypted_example_image.jpg` using a key of 100 and
        save the result as `decrypted_example_image.jpg`.

Notes:
    - The encryption and decryption are performed using simple pixel value manipulation. The key
      is added to or subtracted from each pixel value, modulo 256 to keep the values in the valid
      range for image pixels.
    - Ensure that the image file you are working with is in a format supported by the Pillow library
      (e.g., JPEG, PNG).
    - For successful decryption, you must use the exact same key that was used for encryption.

Author:
    Divine Ezelibe

License:
    This script is provided as-is with no warranty. Use it at your own risk.

"""
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
