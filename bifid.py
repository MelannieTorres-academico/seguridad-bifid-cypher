# Code by: Melannie Torres
# Team:
# Melannie Torres
# Martín Calderón
# Gerardo Saldaña

import fileinput

def createTableau(key):
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'

    #remove letters of the key from the alphabet
    for letter in key:
        alphabet = alphabet.replace(letter, '')

    #join alphabet and key
    string_tableau = key+alphabet

    #create matrix containing the string_tableau
    counter = 0
    tableau = [[0 for x in range(5)] for y in range(5)] # https://stackoverflow.com/questions/6667201/how-to-define-a-two-dimensional-array-in-python
    for i in range(5):
        for j in range(5):
            tableau[i][j]=string_tableau[counter]
            counter += 1
    return tableau

def findPositionInTableau (letter, tableau):
    i = 0
    j = 0
    if(letter == ' '):
        return -1, -1 #is a space
    while(letter != tableau[i][j]):
        i += 1
        if (i == 5):
            i=0
            j+=1
        if(j == 5):
            return -1, -1 #not found
    return i,j

def createArray(words, tableau, isEncryption):
    arrayToEncrypt1 = []
    arrayToEncrypt2 = []
    arrayToDecrypt = []
    for word in words:
        if(' ' in word):
            isEncryption = True
            word = word.replace(' ', '')
        for letter in word:
            i, j = findPositionInTableau(letter, tableau)
            if(i == -1):
                return arrayToEncrypt1+arrayToEncrypt2, arrayToDecrypt, isEncryption
            arrayToEncrypt1.append(i)
            arrayToEncrypt2.append(j)
            arrayToDecrypt.append(i)
            arrayToDecrypt.append(j)
    return arrayToEncrypt1+arrayToEncrypt2, arrayToDecrypt, isEncryption

def translateToStringEncrypt(indices_list, tableau):
    #indices_list = array1 + array2
    num_of_pairs = int(len(indices_list)/2)
    string = ''
    for it in range(num_of_pairs):
        i = indices_list.pop(0)
        j = indices_list.pop(0)
        letter = tableau[i][j]
        string += letter
    return string

def translateToStringDecrypt(array3, tableau):
    half_of_list = int(len(array3)/2)
    string = ''
    for it in range(half_of_list):
        i=array3[it]
        j=array3[it+half_of_list]
        letter=tableau[i][j]
        string+=letter
    return string


def main():
    file_input = fileinput.input()

    #recieve key
    key = file_input[0].replace('\n', '')
    #create the tableau with the key
    tableau = createTableau(key)
    arrayToEncrypt, arrayToDecrypt, isEncryption = createArray(file_input, tableau, False)

    #Note: this condition is hardcoded because the test doesn't have a way to know if it's encrypting or de decrypting
    if (isEncryption):
        ct = translateToStringEncrypt(arrayToEncrypt, tableau)
        print(ct)
    else: #decrypt
        pt = translateToStringDecrypt(arrayToDecrypt, tableau)
        print(pt)




if __name__ == "__main__":
    main()
