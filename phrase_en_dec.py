import phrase_encrypt
import phrase_decrypt

while(1):
    print("Phrase Encrypter and Decrypter")
    print("1. Encrypt Phrase")
    print("2. Decrypt Phrase")
    print("3. Exit")


    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        phrase_encrypt.encrypt_phrase()
    elif choice == "2":
        phrase_decrypt.decrypt_phrase()
    elif choice == "3":
        break
    else:
        print("Invalid choice")
