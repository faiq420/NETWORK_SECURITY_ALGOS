from Encryption import Encryption
from Decryption import Decryption

if __name__ == "__main__":
    option = int(input("Enter the option 1 for Encryption or 2 for Decryption: "))
    text = input("Enter the text you want to encrypt or decrypt: ")
    ShiftKey = (input("Enter the Key: "))
    ciphertext=""
    if option == 1:
        ciphertext = Encryption(text, ShiftKey)
    elif option == 2:
        ciphertext = Decryption(text, ShiftKey)
    else:
        print("Invalid Option")
    print("Processed Text is :", ciphertext)