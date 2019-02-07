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
        return -1, -1
    while(letter != tableau[i][j]):
        i += 1
        if (i == 5):
            i=0
            j+=1
        if(j == 5):
            return -1, -1

    return i,j

def createArray(words, tableau, flag):
    array1 = []
    array2 = []
    array3 = []
    for word in words:
        if(' ' in word):
            flag = True
        word = word.replace(' ', '')
        for letter in word:
            i, j= findPositionInTableau(letter, tableau)
            if(i == -1):
                return array1, array2, array3, flag
            array1.append(i)
            array2.append(j)
            array3.append(i)
            array3.append(j)
    return array1, array2, array3, flag

def translateToStringEncrypt(array1, array2, tableau):
    indices_list = array1 + array2
    num_of_pairs = int(len(indices_list)/2)
    string=''
    for it in range(num_of_pairs):
        i=indices_list.pop(0)
        j=indices_list.pop(0)
        letter=tableau[i][j]
        string+=letter
    return string

def translateToStringDecrypt(array3, tableau):
    string=''
    half_of_list = int(len(array3)/2)

    for it in range(half_of_list):
        i=array3[it]
        j=array3[it+half_of_list]
        letter=tableau[i][j]
        string+=letter
    return string



def main():
    file_input = fileinput.input()
    flag = False

    #recieve key
    key = file_input[0]
    key = key.replace('\n', '')

    tableau = createTableau(key)

    words = file_input


    array1, array2, array3, flag = createArray(words, tableau, flag)

    if (flag):
        ct = translateToStringEncrypt(array1, array2, tableau)
        print(ct)
    else:
        pt = translateToStringDecrypt(array3, tableau)
        print(pt)




if __name__ == "__main__":
    main()
