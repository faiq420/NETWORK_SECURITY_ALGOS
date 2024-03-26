from tables import fetchByIndexForDecryption,predefined_matrix

def Decryption(array):
    inverseBytes=InverseSubBytes(array)
    inverseShift=InverseShiftRows(inverseBytes)
    multipliedArray=InverseMixColumn(inverseShift,predefined_matrix)
    convertedText=InverseAddRoundKey(multipliedArray)
    return convertedText

def InverseSubBytes(array):     #step 1
    newArray = []
    for i in array:
        innerArray = []
        for j in i:
            innerArray.append(fetchByIndexForDecryption(j))
        newArray.append(innerArray)
    return newArray

def InverseShiftRows(array2d):  # second step
    newArray = []
    for i in range(0, len(array2d)):
        first = array2d[i][i : len(array2d[i])]
        second = array2d[i][0:i]
        innerArray = first + second
        newArray.append(innerArray)
    return newArray

def hex_to_int(hex_str):
    return int(hex_str, 16)

def int_to_hex(int_val):
    return hex(int_val)[2:]

def InverseMixColumn(matrix1, matrix2):     # third step
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix.")

    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            cell_sum = 0
            for k in range(len(matrix2)):
                cell_sum += hex_to_int(matrix1[i][k]) * hex_to_int(matrix2[k][j])
            row.append(int_to_hex(cell_sum))
        result.append(row)
    return result

def InverseAddRoundKey(state):  # fourth step
    round_key = [
        ["AC", "19", "28", "57"],
        ["77", "FA", "D1", "5C"],
        ["66", "DC", "29", "00"],
        ["F3", "21", "41", "6A"],
    ]
    result = []
    for row1, row2 in zip(round_key, state):
        result_row = []
        for elem1, elem2 in zip(row1, row2):
            result_row.append("{:02x}".format(int(elem1, 16) ^ int(elem2, 16)))
        result.append(result_row)
    return result