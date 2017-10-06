def replace(string):
    if len(string) == 0:
        return string
    if len(string) == 1:
        if string[0] != " ":
            return string

    indexes = []
    for i, letter in enumerate(string):
        if letter == " ":
            indexes.append(i)

    if len(indexes) == 0:
        return string
    
    for k in range(len(indexes)-1, -1, -1):
        string.append('2')
        string.append('0')
        string[indexes[k]] = '%'
        for j in range(len(string)-1, indexes[k]+2, -1):
            string[j] = string[j-2]
        string[indexes[k]+1] = '2'
        string[indexes[k]+2] = '0'
    return string

def replaceFast(string):
    if len(string) == 0:
        return string
    if len(string) == 1:
        if string[0] != ' ':
            return string

    spaceCount = 0
    for letter in string:
        if letter == ' ':
            spaceCount += 1

    if spaceCount == 0:
        return string
    
    pLen = len(string)
    newLen = len(string)+2*spaceCount
    for j in range(2*spaceCount):
        string.append('')
    for k in range(pLen-1, -1, -1):
        if string[k] == ' ':
            string[newLen-1] = '0'
            string[newLen-2] = '2'
            string[newLen-3] = '%'
            newLen -= 3
        else:
            string[newLen-1] = string[k]
            newLen -= 1
    return string

if __name__ == "__main__":
    string = ['H','o','l','a',' ','M','i','g','u','e','l',' ',' ','a','b',' ']
    print(replace(string))
    string = ['H','o','l','a',' ']
    print(replace(string))
    string = []
    print(replace(string))
    string = ['H']
    print(replace(string))
    string = [' ']
    print(replace(string))
    string = ['']
    print(replace(string))
    string = [' ',' ',' ',' ',' ']
    print(replace(string))
    print("~~~~~~~~~~~~~~~~~~~~~~")
    string = ['H','o','l','a',' ','M','i','g','u','e','l',' ',' ','a','b',' ']
    print(replaceFast(string))
    string = ['H','o','l','a',' ']
    print(replaceFast(string))
    string = []
    print(replaceFast(string))
    string = ['H']
    print(replaceFast(string))
    string = [' ']
    print(replaceFast(string))
    string = ['']
    print(replaceFast(string))
    string = [' ',' ',' ',' ',' ']
    print(replaceFast(string))
