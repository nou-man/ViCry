from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def encrypt_phrase():
    # Load the public key from a file
    with open('keys/public_key_5000.pem', 'rb') as f:
        public_key = RSA.import_key(f.read())

    # Encrypt the phrase using the public key
    phrase = input("Enter the pass-phrase with minimum 5 words: ")

    # Condition set for minimum 5 words and each word must have 3 character
    if phrase.count(' ') >= 4 and sum(len(word) >= 3 for word in phrase.split()) >= 5:
        cipher = PKCS1_OAEP.new(public_key)
        encrypted_phrase = cipher.encrypt(phrase.encode())

        # Write the encrypted phrase to a file
        with open('unlock_key.txt', 'wb') as f:
            f.write(encrypted_phrase)

        print('Encrypted phrase saved to unlock_key.txt')
    else:
        print('Invalid sentence')
