from Encryption import Encryption

if __name__ == "__main__":
    text = "instruments"
    key = "monarchy"
    result = Encryption(text.lower(), key.lower())
    print("Plain Text is :-",text)
    print("Encrypted Text is :-",result)
