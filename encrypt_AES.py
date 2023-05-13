import phrase_encrypt
from Crypto.Cipher import AES
import os
import time

def encrypt_video():
        
    # Set the encryption key and block size
    key = phrase_encrypt.encrypt_phrase().encode('utf-8')
    # key = pass_phrase.encode('utf-8')
    # key = b'Sixteen byte key'
    block_size = 16

    # Set the input and output directories
    input_dir = './source_video/'
    output_dir = './encrypted_video/'

    # Check if the source video directory exists and is not empty
    if not os.path.exists(input_dir):
        print("\n \033[31mError: Source video folder not found!\033[0m")
        return
    elif not os.listdir(input_dir):
        print(" \033[31mError: Source video directory is empty!\033[0m")
        return

    # Check if the output directory exists, create it if it doesn't
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    #Giving manual delay of 3 seconds before encrypting video 
    print("\n\033[33m Encrypting Video\033[0m ", end="", flush=True)
    for i in range(3):
        print("\033[33m.\033[0m", end="", flush=True)  # print a dot without a newline and flush the buffer
        time.sleep(1)  # wait for 1 second
    print()  # print a newline to move to the next line
    print()  # print a newline to move to the next line

    # Iterate over the input directory and encrypt each file
    for filename in os.listdir(input_dir):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)

        # Open the input video file and read the contents
        with open(input_path, 'rb') as f:
            plaintext = f.read()

        # Add padding to the plaintext if necessary
        pad_len = block_size - len(plaintext) % block_size
        plaintext += pad_len * bytes([pad_len])

        # Generate a random initialization vector
        iv = os.urandom(block_size)

        # Create the AES cipher object with CBC mode
        cipher = AES.new(key, AES.MODE_CBC, iv)

        # Encrypt the plaintext with the cipher object
        ciphertext = iv + cipher.encrypt(plaintext)

        # Write the encrypted video to the output file
        with open(output_path, 'wb') as f:
            f.write(ciphertext)
        
        time.sleep(1)
        # print("\nEncryption of Video was Successful !")
        print('\033[32m Encryption of Video was Successful !\033[0m')
        time.sleep(1)
        print(" Encrypted Video moved to folder \033[32m'encrypted_video'\033[0m ..")
        time.sleep(2)
