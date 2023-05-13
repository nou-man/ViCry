from Crypto.Cipher import AES
import phrase_decrypt
import os
import time

def decrypt_video():
    # Set the encryption key and block size
    pass_phrase = phrase_decrypt.decrypt_phrase()
    if not pass_phrase:
        # print("\n\033[31mError: Key is empty!\033[0m")
        return
    key = pass_phrase.encode('utf-8')
    block_size = 16

    # Set the input and output directories
    input_dir = './encrypted_video/'
    output_dir = './decrypted_video/'

    # Check if the encrypted video directory exists and create it if it doesn't
    if not os.path.exists(input_dir):
        print("\n\033[31mError: encrypted_video directory not found!\033[0m")
        return
    elif not os.listdir(input_dir):
        print("\n\033[31mError: encrypted_video directory is empty!\033[0m")
        return

    # Check if the decrypted video directory exists and create it if it doesn't
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    # Giving manual delay of 3 seconds
    print("\n\n \033[33mVideo decryption in progress \033[0m ", end="", flush=True)
    for i in range(3):
        print("\033[33m. \033[0m", end="", flush=True)  # print a dot without a newline and flush the buffer
        time.sleep(1)  # wait for 1 second
    print()  # print a newline to move to the next line

    # Iterate over the input directory and decrypt each file
    for filename in os.listdir(input_dir):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)

        # Open the encrypted video file and read the contents
        with open(input_path, 'rb') as f:
            ciphertext = f.read()

        # Get the initialization vector from the beginning of the ciphertext
        iv = ciphertext[:block_size]

        # Create the AES cipher object with CBC mode
        cipher = AES.new(key, AES.MODE_CBC, iv)

        # Decrypt the ciphertext with the cipher object
        plaintext = cipher.decrypt(ciphertext[block_size:])

        # Remove padding from the plaintext
        pad_len = plaintext[-1]
        plaintext = plaintext[:-pad_len]

        # Write the decrypted video to the output file
        with open(output_path, 'wb') as f:
            f.write(plaintext)

        time.sleep(1)
        print('\n\033[32m Video decryption successful !\033[0m')
        time.sleep(2)
