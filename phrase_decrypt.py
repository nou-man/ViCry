from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def decrypt_phrase():
    # Load the private key from a file
    with open('keys/private_key_5000.pem', 'rb') as f:
        private_key = RSA.import_key(f.read())

    # Load the encrypted message from a file
    with open('unlock_key.txt', 'rb') as f:
        encrypted_message = f.read()

    # Decrypt the message using the private key
    cipher = PKCS1_OAEP.new(private_key)
    decrypted_message = cipher.decrypt(encrypted_message)

    print('Decrypted message:', decrypted_message.decode())
