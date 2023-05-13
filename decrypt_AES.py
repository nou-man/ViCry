# from Crypto.Cipher import AES

# # Set the encryption key and block size
# key = b'Sixteen byte key'
# block_size = 16

# # Open the encrypted video file and read the contents
# with open('./encrypted_video/encrypted_video.mp4', 'rb') as f:
#     ciphertext = f.read()

# # Get the initialization vector from the beginning of the ciphertext
# iv = ciphertext[:block_size]

# # Create the AES cipher object with CBC mode
# cipher = AES.new(key, AES.MODE_CBC, iv)

# # Decrypt the ciphertext with the cipher object
# plaintext = cipher.decrypt(ciphertext[block_size:])

# # Remove padding from the plaintext
# pad_len = plaintext[-1]
# plaintext = plaintext[:-pad_len]

# # Write the decrypted video to the output file
# with open('./decrypted_video/decrypted_video.mp4', 'wb') as f:
#     f.write(plaintext)


from Crypto.Cipher import AES
import os

def decrypt_video():
    # Set the encryption key and block size
    # key = b'Sixteen byte key'
    pass_phrase = input('Enter the video decryption key: ')
    key = pass_phrase.encode('utf-8')
    block_size = 16

    # Set the input and output directories
    input_dir = './encrypted_video/'
    output_dir = './decrypted_video/'

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
