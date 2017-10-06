def uniqueChar(string):
    if len(string) > 256:
        return False
    if len(string) == 0 or len(string) == 1:
        return True
    for i in range(0, len(string)-1):
        charComp = string[i]
        for j in range(i+1, len(string)):
            if charComp == string[j]:
                return False
    return True

def uniqueCharFast(string):
    if len(string) > 256:
        return False
    booleanList = [False for _ in range(256)]
    for i in range(0, len(string)):
        charComp = ord(string[i])
        if booleanList[charComp] == True:
            return False
        booleanList[charComp] = True
    return True

if __name__ == "__main__":
    print(str(uniqueChar("hola")))
    print(str(uniqueChar("")))
    print(str(uniqueChar(" ")))
    print(str(uniqueChar("aa")))
    print(str(uniqueChar("aha")))
    print(str(uniqueChar("holaaaa")))
    print("~~~~~~~~~")
    print(str(uniqueCharFast("hola")))
    print(str(uniqueCharFast("")))
    print(str(uniqueCharFast(" ")))
    print(str(uniqueCharFast("aa")))
    print(str(uniqueCharFast("aha")))
    print(str(uniqueCharFast("holaaaa")))