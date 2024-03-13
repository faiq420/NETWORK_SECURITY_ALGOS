from Encryption import Encryption
from Decryption import Decryption


if __name__ == "__main__":
    option = int(input("Enter the option 1 for Encryption or 2 for Decryption: "))
    plaintext = input("Enter the text you want to encrypt or decrypt: ")
    ShiftKey = int(input("Enter the Shift Key: "))
    # option=2
    # ShiftKey=3
    # ShiftKeyDec=4
    # plaintext="defendtheeastwall"
    # encTxt="TEKOOHRACIRMNREATANFTETYTGHH"
    ciphertext=""
    if option == 1:
        ciphertext = Encryption(plaintext, ShiftKey)
    elif option == 2:
        ciphertext = Decryption(plaintext, ShiftKey)
    else:
        print("Invalid Option")
    print("Processed Text is :", ciphertext)
