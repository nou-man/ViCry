from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import time
import secrets

def encrypt_phrase():
    # Load the public key from a file
    with open('keys/public_key_5000.pem', 'rb') as f:
        public_key = RSA.import_key(f.read())

    #Giving manual delay of 3 seconds 
    print("\n\n\033[33m Generating key \033[0m ", end="", flush=True)
    for i in range(3):
        print("\033[33m. \033[0m", end="", flush=True)  # print a dot without a newline and flush the buffer
        time.sleep(1)  # wait for 1 second
    print()  # print a newline to move to the next line
    
    print('\n \033[32mKey Generation was Successful !!!\033[0m\n')
    
    # Generate a 16-byte string of random bytes
    rand_bytes = secrets.token_bytes(16)

    # Print the byte string in hexadecimal format
    print(" The Key generated is: ",rand_bytes.hex())

    # Encrypt the phrase using the public key
    phrase = rand_bytes.hex()

    # Condition set for minimum 5 words and each word must have 3 character
    # if phrase.count(' ') >= 4 and sum(len(word) >= 3 for word in phrase.split()) >= 5:
    if phrase != None:
        cipher = PKCS1_OAEP.new(public_key)
        encrypted_phrase = cipher.encrypt(phrase.encode())

        # Write the encrypted phrase to a file
        with open('unlock_key.txt', 'wb') as f:
            f.write(encrypted_phrase)

        print(' Encrypted phrase saved to unlock_key.txt')
        
        return phrase
    else:
        print(' Key generation failed, Please Retry')

    
