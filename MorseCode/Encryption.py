from Codes import codes

def Encryption(text):
    morse_code = ""
    for i in text.upper():
        if i in codes:
            morse_code += codes[i] + " "
        else:
            morse_code += i
    return morse_code.strip()