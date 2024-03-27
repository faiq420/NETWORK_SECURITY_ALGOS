def Encryption(text,key):
    matrix = createMatrix(text, key)
    diagraph=createDiagraph(text)
    cipher=fetchEquivalentCharacters(matrix,diagraph)
    return cipher

def createMatrix(txt, key):
    txt = txt.lower()
    key = key.lower()
    alphabets = [chr(i) for i in range(ord("a"), ord("z") + 1)]
    booleanFlags = [True for i in range(ord("a"), ord("z") + 1)]
    count = row_index = column_index = 0
    matrix = []
    for r in range(1, 6):
        a = []
        for c in range(1, 6):
            a.append(c)
        matrix.append(a)
    for k in key:  # populating matrix with key
        element = alphabets.index(k)
        if booleanFlags[element] != False:  # if not already put in matrix
            matrix[row_index][column_index] = k
            count += 1
            booleanFlags[element] = False
            if column_index < 4:
                column_index += 1
            else:
                column_index = 0
                if row_index != 4:
                    row_index += 1
    for i in range(26):  # now populating matrix
        if booleanFlags[i] == True and alphabets[i] != "j":
            matrix[row_index][column_index] = alphabets[i]
            booleanFlags[i] = False
            if column_index < 4:
                column_index += 1
            else:  # column_index==4
                column_index = 0
                if row_index < 4:
                    row_index += 1
    return matrix

def createDiagraph(text):
    diagraphArray = []
    count = 0
    temp = te = ""
    for txt in text:
        if te != "":
            temp = te
            te = ""
        if temp == txt:
            temp = temp + "x"
            te = txt
        else:
            temp = temp + txt
        count += 1
        if len(temp) == 2 or count == len(text):
            diagraphArray.append(temp)
            temp = ""
    if len(diagraphArray[-1]) == 1:
        diagraphArray[-1] = diagraphArray[-1] + "z"
    return diagraphArray

def fetchEquivalentCharacters(matrix,diagraph):
    column1_index  = column2_index  = None
    index = 0
    encrypted_text = ""
    row1_index  = row2_index  = None
    for d in range(0, len(diagraph)):
        current_elements = list(diagraph[d])
        column1_index  = column2_index  = row1_index  = row2_index  = None
        for r in range(0, 5):
            if current_elements[index] in matrix[r] or current_elements[index] == "j":  # and r<1:
                if current_elements[index] == "j":  # covering j case
                    if "i" in matrix[r]:
                        column1_index  = matrix[r].index("i")
                        row1_index  = r
                else:
                    column1_index  = matrix[r].index(current_elements[index])
                    row1_index  = r
            index += 1
            if current_elements[index] in matrix[r] or current_elements[index] == "j":  # and r<1:
                if current_elements[index] == "j":
                    if "i" in matrix[r]:
                        column2_index  = matrix[r].index("i")
                        row2_index  = r
                else:
                    column2_index  = matrix[r].index(current_elements[index])
                    row2_index  = r
            index = 0
            if column1_index  == column2_index  and column1_index  != None and column2_index  != None:  # if cols are same
                if row1_index  < 4:
                    encrypted_text = encrypted_text + matrix[row1_index  + 1][column1_index ]
                else:
                    encrypted_text = encrypted_text + matrix[0][column1_index ]
                if row2_index  < 4:
                    encrypted_text = encrypted_text + matrix[row2_index  + 1][column2_index ]
                else:
                    encrypted_text = encrypted_text + matrix[0][column2_index ]
                break
            elif row1_index  == row2_index  and row1_index  != None:
                if column1_index  < 4:
                    encrypted_text = encrypted_text + matrix[row1_index ][column1_index  + 1]
                else:
                    encrypted_text = encrypted_text + matrix[row1_index ][0]
                if column2_index  < 4:
                    encrypted_text = encrypted_text + matrix[row2_index ][column2_index  + 1]
                else:
                    encrypted_text = encrypted_text + matrix[row2_index ][0]
                break
            elif row1_index  != None and row2_index  != None and column1_index  != None and column2_index  != None and column1_index  < column2_index :
                new_column_index= column2_index  - column1_index   # ->
                encrypted_text = encrypted_text + matrix[row1_index ][column1_index  + new_column_index]
                new_column_index= abs(column1_index  - column2_index )  # <-
                encrypted_text = encrypted_text + matrix[row2_index ][column2_index  - new_column_index]
                break

            else:  # if column1_index  is greater
                if column1_index  != None and column2_index  != None and row1_index  != None and row2_index  != None and column1_index  > column2_index :
                    new_column_index= column1_index  - column2_index 
                    encrypted_text = encrypted_text + matrix[row1_index ][column1_index  - new_column_index]
                    new_column_index= abs(column2_index  - column1_index )
                    encrypted_text = encrypted_text + matrix[row2_index ][column2_index  + new_column_index]
                    break

    return encrypted_text
