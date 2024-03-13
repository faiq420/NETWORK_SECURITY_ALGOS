def createTemplateMatrix(encrptedTxt, key):
    rail = [['-' for i in range(len(encrptedTxt))]
                for j in range(key)]
    move_to_next_row = None
    row, col = 0, 0
    for i in range(len(encrptedTxt)):
        if row == 0:
            move_to_next_row = True
        if row == key - 1:
            move_to_next_row = False
        rail[row][col] = '*'
        col += 1
        if move_to_next_row:
            row += 1
        else:
            row -= 1
    return rail

def fillLetters(rail,encrptedTxt, key):
    index = 0
    for i in range(key):
        for j in range(len(encrptedTxt)):
            if (rail[i][j] == '*'):
                rail[i][j] = encrptedTxt[index]
                index += 1
    return rail

def fetchText(rail,encrptedTxt, key):
    result = []
    row, col = 0, 0
    for i in range(len(encrptedTxt)):
        if row == 0:
            move_to_next_row = True
        if row == key-1:
            move_to_next_row = False
        if (rail[row][col] != '*'):
            result.append(rail[row][col])
            col += 1
        if move_to_next_row:
            row += 1
        else:
            row -= 1
    return("".join(result))

def Decryption(encrptedTxt, key):
    rail=createTemplateMatrix(encrptedTxt, key)
    rail=fillLetters(rail,encrptedTxt, key)
    text=fetchText(rail,encrptedTxt, key)
    return text