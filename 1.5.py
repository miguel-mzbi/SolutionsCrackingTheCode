def compress(string):
    if len(string) == 0 or len(string) == 1:
        return string
    
    count = []
    currentCount = 0
    currentLetter = string[0]
    returnString = []
    for letter in string:
        if currentLetter == letter:
            currentCount += 1
        elif letter != currentLetter:
            returnString.append(currentLetter + str(currentCount))
            currentLetter = letter
            currentCount = 1
    returnString.append(currentLetter + str(currentCount))
    returnString = "".join(returnString)

    if len(string) < len(returnString):
        return string
    else:
        return returnString

if __name__ == "__main__":
    print(str(compress("hola")))
    print(str(compress("")))
    print(str(compress(" ")))
    print(str(compress("aa")))
    print(str(compress("aaa")))
    print(str(compress("holaaaa")))
    print(str(compress("holaaaaaaaaaaaaaaaaaaaaaaaa")))
    print(str(compress("hooolaaaaaaaaaaaaaaaaaaaaaaaa")))
