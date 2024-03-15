import math

def Decryption(encryptedText,key):
    elementList=[]
    processedText=encryptedText.replace(" ","")
    rows=math.ceil(len(processedText)//len(key))
    array=[]
    plainText=""
    setOfUniqueChars=set([])
     #create entry(index) of every element in key
    for i,char in enumerate(key):
        elementList.append({"index":i,"element":char,"used":False})
    
    #sort elements in indexed list for order of arrangement
    sorted_list = sorted(elementList, key=lambda x: x['element'])

    #add plain text in matrix
    for i in range(0, len(processedText), len(key)):
        row = [] 
        for j in range(len(key)):
            if i + j < len(processedText):
                row.append(processedText[i + j])
            else:
                row.append('')
        array.append(row)

        #fetch unique characters in key
    for i in sorted_list:
        setOfUniqueChars.add(i["element"])

    sortedSet= sorted(setOfUniqueChars)

    #fetch from array a/c to index
    for i in sortedSet:
        filtered=list(filter(lambda x: x["element"] == i, sorted_list))
        for j in filtered:
            indexed=array[j["index"]]
            for k in indexed:
                plainText+=k
    print(plainText.replace("&",""))