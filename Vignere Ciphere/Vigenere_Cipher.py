from Vignere_Table import PrintVignereTable

def Encryption(plainText, keyStream):
    result = ""
    for i in range(len(plainText)):
        key = i % (len(keyStream))
        if plainText[i].isalpha():
            if plainText[i].islower():
                result += chr((ord(plainText[i]) + ord(keyStream[key])) % 26 + 97)
            else:
                result += chr((ord(plainText[i]) + ord(keyStream[key])) % 26 + 65)
        else:
            result += plainText[i]
    return result

def Decryption(plainText, keyStream):
    result = ""
    for i in range(len(plainText)):
        key = i % (len(keyStream))
        if plainText[i].isalpha():
            if plainText[i].islower():
                result += chr((ord(plainText[i]) - ord(keyStream[key])) % 26 + 97)
            else:
                result += chr((ord(plainText[i]) - ord(keyStream[key])) % 26 + 65)
        else:
            result += plainText[i]
    return result


if __name__ == "__main__":
    PrintVignereTable()
    option = int(input("Enter the option 1 for Encryption or 2 for Decryption: "))
    plaintext = input("Enter the text you want to encrypt or decrypt: ")
    key = input("Enter the lock stream: ")
    if option == 1:
        ciphertext = Encryption(plaintext, key)
    elif option == 2:
        ciphertext = Decryption(plaintext, key)
    else:
        print("Invalid Option")
    print("Cipher Text is :", ciphertext)
