# from Crypto.Cipher import AES
# import os

# # Set the encryption key and block size
# key = b'Sixteen byte key'
# block_size = 16

# # Open the input video file and read the contents
# with open('./source_video/video_test.mp4', 'rb') as f:
#     plaintext = f.read()

# # Add padding to the plaintext if necessary
# pad_len = block_size - len(plaintext) % block_size
# plaintext += pad_len * bytes([pad_len])

# # Generate a random initialization vector
# iv = os.urandom(block_size)

# # Create the AES cipher object with CBC mode
# cipher = AES.new(key, AES.MODE_CBC, iv)

# # Encrypt the plaintext with the cipher object
# ciphertext = iv + cipher.encrypt(plaintext)

# # Write the encrypted video to the output file
# with open('./encrypted_video/encrypted_video.mp4', 'wb') as f:
#     f.write(ciphertext)


from Crypto.Cipher import AES
import os

def encrypt_video():
    
    # Set the encryption key and block size
    pass_phrase = input('Enter the video encryption key: ')
    key = pass_phrase.encode('utf-8')
    # key = b'Sixteen byte key'
    block_size = 16

    # Set the input and output directories
    input_dir = './source_video/'
    output_dir = './encrypted_video/'

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
