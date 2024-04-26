from Encryption import Encryption

if __name__ == "__main__":
    array = [
        ["EA", "04", "65", "85"],
        ["83", "45", "5D", "96"],
        ["5C", "33", "98", "B0"],
        ["F0", "2D", "AD", "C5"],
    ]
    print(f"Plain text: \n {array}")
    result=Encryption(array)
    print(f"Ciphered text: \n {result}")
