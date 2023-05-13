from Crypto.Cipher import AES
import os

# Set the encryption key and block size
key = b'Sixteen byte key'
block_size = 16

# Open the input video file and read the contents
with open('./source_video/video_test.mp4', 'rb') as f:
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
with open('./encrypted_video/encrypted_video.mp4', 'wb') as f:
    f.write(ciphertext)
