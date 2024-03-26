from tables import fetchByIndexForEncryption, predefined_matrix


def sub_bytes(array2d):  # first step
    newArray = []
    for i in array2d:
        innerArray = []
        for j in i:
            innerArray.append(fetchByIndexForEncryption(j))
        newArray.append(innerArray)
    return newArray


def shift_rows(array2d):  # second step
    newArray = []
    for i in range(0, len(array2d)):
        first = array2d[i][i : len(array2d[i])]
        second = array2d[i][0:i]
        innerArray = first + second
        newArray.append(innerArray)
    return newArray


def gf_multiply(a, b):
    # Perform Galois Field (GF) multiplication of two bytes a and b.
    result = 0
    while b:
        if b & 1:
            result ^= a
        a <<= 1
        if (
            a & 0x100
        ):  # If a exceeds 255, reduce modulo irreducible polynomial (x^8 + x^4 + x^3 + x + 1)
            a ^= 0x11B
        b >>= 1
    return result


def mix_column(array2d):  # third step
    array2_hex = [["{:02x}".format(num) for num in row] for row in predefined_matrix]
    new_state = [["00"] * 4 for _ in range(4)]
    # Perform matrix multiplication
    for i in range(4):
        for j in range(4):
            result = 0
            for k in range(4):
                result ^= gf_multiply(int(array2_hex[i][k]), int(array2d[k][j], 16))
            new_state[i][j] = "{:02x}".format(result)
    return new_state


def add_round_key(state):  # fourth step
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


def Encryption(array):
    substitted_array = sub_bytes(array)
    print(substitted_array,"substitted_array")
    shifted_array = shift_rows(substitted_array)
    print(shifted_array,"shifted_array")
    mixed_column = mix_column(shifted_array)
    print(mixed_column,"mixed_column")
    cipher = add_round_key(mixed_column)
    return cipher