from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import os
import time

# def decrypt_phrase():

#     # Load the private key from a file
#     with open('keys/private_key_5000.pem', 'rb') as f:
#         private_key = RSA.import_key(f.read())

#     # Check if the unlock file exists before loading it
#     if not os.path.exists('unlock_key.txt'):
#         print(' File not found: unlock_key.txt')
#         return

#     #Giving manual delay of 3 seconds 
#     print("\n Decrypting the key from unlock_key.txt ", end="", flush=True)
#     for i in range(3):
#         print(".", end="", flush=True)  # print a dot without a newline and flush the buffer
#         time.sleep(1)  # wait for 1 second
#     print()  # print a newline to move to the next line

#     # Load the encrypted message from a file
#     with open('unlock_key.txt', 'rb') as f:
#         encrypted_message = f.read()

#     # Decrypt the message using the private key
#     cipher = PKCS1_OAEP.new(private_key)
#     decrypted_message = cipher.decrypt(encrypted_message)

#     print(' Decrypted key:', decrypted_message.decode())

#     return (decrypted_message.decode())

def decrypt_phrase():

    # Load the private key from a file
    with open('keys/private_key_5000.pem', 'rb') as f:
        private_key = RSA.import_key(f.read())

    # Check if the unlock file exists before loading it
    if not os.path.exists('unlock_key.txt'):
        print(' \033[31mError: unlock_key.txt not found\033[0m')
        return
    else:
        #Giving manual delay of 3 seconds 
        print("\n Decrypting the key from unlock_key.txt ", end="", flush=True)
        for i in range(3):
            print(".", end="", flush=True)  # print a dot without a newline and flush the buffer
            time.sleep(1)  # wait for 1 second
        print()  # print a newline to move to the next line

        # Load the encrypted message from a file
        with open('unlock_key.txt', 'rb') as f:
            encrypted_message = f.read()

        # Decrypt the message using the private key
        cipher = PKCS1_OAEP.new(private_key)
        decrypted_message = cipher.decrypt(encrypted_message)

        unlock_key = decrypted_message.decode()

    return unlock_key
