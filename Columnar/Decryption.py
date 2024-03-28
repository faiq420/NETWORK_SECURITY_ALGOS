import math

def Decryption(encryptedText,key):
    processedText = encryptedText.replace(" ", "")
    rows = math.ceil(len(processedText) / len(key))
    array = [[""] * len(key) for _ in range(rows)]
    decryptedText = ""

    elementList = [{"index": i, "element": char, "used": False} for i, char in enumerate(key)]

    sorted_list = sorted(elementList, key=lambda x: x['element'])
    # Fill the array with encrypted text by the key
    index = 0
    for char in sorted(key):
        filtered = list(filter(lambda x: x["element"] == char, sorted_list))
        for elem in filtered:
            for k in range(rows):
                if index < len(processedText):
                    array[k][elem["index"]] = processedText[index]
                    index += 1

    for row in array:
        decryptedText += ''.join(row)

    return decryptedText.replace("&", "")