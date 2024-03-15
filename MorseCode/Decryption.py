from Codes import codes

def Decryption(morse):
    plainText = ""
    characters=morse.split("|")
    for i in characters:
        txt=get_key_by_value(codes,i)
        if(txt==None):
            plainText+=i
        else:
            plainText+=txt
   
    return plainText

def get_key_by_value(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key
    return None