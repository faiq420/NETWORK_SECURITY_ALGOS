from Decryption import Decryption

if __name__ == "__main__":
    array = [
        ["87", "f2", "4d", "97"],
        ["ec", "6e", "4c", "90"],
        ["4a", "c3", "46", "e7"],
        ["8c", "d8", "95", "a6"],
    ]
    # array = [
    #     ["eb", "59", "8b", "1b"],
    #     ["40", "2e", "a1", "c3"],
    #     ["f2", "38", "13", "42"],
    #     ["1e", "84", "e7", "d6"],
    # ]
    result = Decryption(array)
    # print(f"Plain text: \n {array}")
    print(f"Ciphered text: \n {result}")
