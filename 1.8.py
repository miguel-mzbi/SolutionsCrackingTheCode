def isRotate(s1, s2):
    if len(s1) == len(s2) and len(s1) > 0:
        s1s1 = s1+s1
        if s2 in s1s1:
            return True
    return False

if __name__ == "__main__":
    
    print(str(isRotate("hola", "laho")))
    print(str(isRotate("hola", "lahho")))
    print(str(isRotate("h", "l")))
    print(str(isRotate("h", "h")))
    print(str(isRotate("", "laho")))
    print(str(isRotate("", "")))