from Encryption import Encryption
from Decryption import Decryption


if __name__ == "__main__":
    option = int(input("Enter the option 1 for Encryption or 2 for Decryption: "))
    Text = input("Enter text to convert:- ")
    processedText=""
    if option == 1:
        processedText = Encryption(Text)
    elif option == 2:
        processedText = Decryption(Text)
    else:
        print("Invalid Option")
    print("Processed Text is :", processedText)
