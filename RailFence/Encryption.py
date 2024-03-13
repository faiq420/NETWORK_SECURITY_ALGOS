def Encryption(plainText, shiftKey):
    encrptedTxt=""
    array = [[] for _ in range(shiftKey)]
    for i, letter in enumerate(plainText):
        index = i % (2 * shiftKey - 2)
        j=index
        if index >= shiftKey:
            index = (2 * shiftKey - 2) - index
        array[index].append(letter)
    first_row_length = len(array[0])
    last_row_length = len(array[-1])
    difference = abs(first_row_length - last_row_length)
    if difference>0:
        for i in range(1,len(array)):
            array[i].append('@')
    for i in array:
        for j in i:
            encrptedTxt +=j
    return encrptedTxt 
