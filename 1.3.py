def isPermutation(stringO, stringC):
    if len(stringC) != len(stringO):
        return False
    if stringO == stringC:
        return True
    freq = {};
    for letter in stringO:
        if letter in freq.keys():
            freq[letter] += 1
        else:
            freq[letter] = 1
    for letter in stringC:
        if letter in freq.keys():
            if freq[letter] == 0:
                return False
            else:
                freq[letter] -= 1
        else:
            return False
    
    return True

if __name__ == "__main__":
    print(str(isPermutation("hola", "hola")))
    print(str(isPermutation("", "")))
    print(str(isPermutation(" ", " ")))
    print(str(isPermutation("abc", "cba")))
    print(str(isPermutation("aha", "aah")))
    print(str(isPermutation("abbcc", "bbcac")))
    print(str(isPermutation("abbcc", "bbcasc")))
    print(str(isPermutation("abbccs", "bbcasc")))
    print(str(isPermutation("abbccjkls", "bkbjcalsc")))
    print(str(isPermutation("abbccjkls", "bkbjalsc")))