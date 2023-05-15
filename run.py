import encrypt_AES
import decrypt_AES
from termcolor import cprint 
from pyfiglet import figlet_format
import os

def main():
    while(1):
        print()
        cprint(figlet_format('MENU', font='digital'),'blue', attrs=['bold'])
        print("1> Encrypt Videos")
        print("2> Decrypt Videos")
        print("3> Exit")
        print("")
        choice = input("Choice:- ")
        
        if choice == '1':
            encrypt_AES.encrypt_video()
        elif choice == '2':
            decrypt_AES.decrypt_video()
        elif choice == '3':
            break
        else:
            print("Redefine your choice !!!")
      
    
if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    cprint(figlet_format('V ! Cry', font='slant'),'yellow', attrs=['bold'])
    cprint(figlet_format('AES Video Encryption Decryption', font='digital'),'green', attrs=['bold'])
    main()
