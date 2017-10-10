
class ThreeStacksOneArray():
    def __init__(self, stackSize = 100, numberStacks = 3):
        self.stackSize = stackSize
        self.numberStacks = numberStacks
        self.array = [None] * self.stackSize*self.numberStacks
        self.size = [-1] * self.numberStacks
        self.totalSize = self.stackSize*self.numberStacks
    
    def __str__(self):
        string = []
        string.append("Stacks [ (")
        for l in range(self.numberStacks):
            if self.size[l] == -1:
                string.append("None")
            else:
                for i in range(l*self.stackSize, l*self.stackSize + self.size[l]+1, 1):
                    string.append(str(self.array[i]))
                    string.append(",")
                del(string[-1])
            if l != self.numberStacks-1:
                string.append(") (")
        string.append(") ]")
        string = "".join(string)
        return string

    def peek(self, stackNum):
        if self.isEmpty:
            print("Stack number " + str(stackNum) + " is empty.")
            return
        return self.array[self.topIndex(stackNum)]

    def insert(self, stackNum, item):
        if stackNum >= self.numberStacks:
            print("Stack number " + str(stackNum) + " doesn't exist. There aren't enough stacks.")
            return
        if self.size[stackNum] == self.stackSize-1:
            print("Stack number " + str(stackNum) + " is full.")
            return
        self.size[stackNum] += 1
        self.array[self.topIndex(stackNum)] = item
        return

    def pop(self, stackNum):
        if self.size[stackNum] == -1:
            print("Stack number " + str(stackNum) + " is empty.")
            return
        toReturn = self.array[self.topIndex(stackNum)]
        self.size[stackNum] -= 1
        return toReturn

    def topIndex(self, stackNum):
        if self.isEmpty(stackNum):
            return -1
        return self.stackSize * stackNum + self.size[stackNum]

    def isEmpty(self, stackNum):
        return self.size[stackNum] == -1

if __name__ == "__main__":
    stacks = ThreeStacksOneArray(5,3)

    print("Inserts")
    stacks.insert(0, 1)
    print(stacks.peek(0))

    stacks.insert(1, 9)
    print(stacks.peek(1))
    stacks.insert(1, 8)
    print(stacks.peek(1))

    stacks.insert(2, 14)
    print(stacks.peek(2)) 
    stacks.insert(2, 13)
    print(stacks.peek(2)) 
    stacks.insert(2, 12)
    print(stacks.peek(2))

    print(str(stacks))

    print("\nPops")
    print(stacks.pop(0))
    print(str(stacks))

    print(stacks.pop(1))
    print(str(stacks))

    print(stacks.pop(2))
    print(str(stacks))
    print(stacks.pop(2))
    print(str(stacks))

    print("\nPop empty")
    print(stacks.pop(0))
    print(str(stacks))

    print("\nInserts to fill")
    stacks.insert(2, 11)
    print(str(stacks))
    stacks.insert(2, 11)
    print(str(stacks))
    stacks.insert(2, 11)
    print(str(stacks))
    stacks.insert(2, 11)
    print(str(stacks))
    stacks.insert(2, 11)
    print(str(stacks))

    print("\nInsert inexistent")
    stacks.insert(10, 10)
    print(str(stacks))