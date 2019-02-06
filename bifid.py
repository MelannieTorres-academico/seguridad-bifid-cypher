import numpy as np
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
    tableau = np.chararray((5,5), unicode=True)
    for i in range(5):
        for j in range(5):
            tableau[i][j]=string_tableau[counter]
            counter += 1
    return tableau

def findPositionInTableau (letter, tableau):
    i = 0
    j = 0
    if(letter == ' '):
        return -1, -1
    while(letter != tableau[i][j]):
        i += 1
        if (i == 5):
            i=0
            j+=1
        if(j == 5):
            return -1, -1

    return i,j

def createArray(words, tableau):
    array1 = []
    array2 = []
    for word in words:
        word = word.replace(' ', '')
        for letter in word:
            i, j= findPositionInTableau(letter, tableau)
            if(i == -1):
                return array1, array2
            array1.append(i)
            array2.append(j)
    return array1,array2

def translateToString(indices_list, tableau):
    num_of_pairs = int(len(indices_list)/2)
    string=''
    for it in range(num_of_pairs):
        i=indices_list.pop(0)
        j=indices_list.pop(0)
        letter=tableau[i][j]
        string+=letter
    return string

def main():
    file_input = fileinput.input()

    #recieve key
    key = file_input[0]
    key = key.replace('\n', '')

    tableau = createTableau(key)

    words=file_input

    array1, array2 = createArray(words, tableau)
    indices_list = array1 + array2

    ct=translateToString(indices_list, tableau)
    print(ct)




if __name__ == "__main__":
    main()
