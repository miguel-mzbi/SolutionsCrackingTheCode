
class Stack():
    def __init__(self, stackSize = 100):
        self.stackSize = stackSize
        self.stack = []
    
    def __str__(self):
        string = []
        string.append("Stack [ ")
        if self.isEmpty():
            string.append("None")
        else:
            for i in range(0, len(self.stack)):
                string.append(str(self.stack[i]))
                string.append(",")
            del(string[-1])
        string.append(" ]")
        string = "".join(string)
        return string

    def isEmpty(self):
        return len(self.stack) == 0

    def isFull(self):
        return len(self.stack) == self.stackSize

    def peek(self):
        if self.isEmpty():
            return
        return self.stack[len(self.stack)-1]

    def insert(self, item):
        if self.isFull():
            return
        self.stack.append(item)
        return

    def pop(self):
        if self.isEmpty():
            return
        toReturn = self.stack.pop()
        return toReturn

    def getBottom(self):
        if self.isEmpty():
            return
        toReturn = self.stack.pop(0)
        return toReturn

class StackOfPlates():
    def __init__(self, stackSize = 100, numberOfStacks = 100):
        self.stackSize = stackSize
        self.numberOfStacks = numberOfStacks
        self.stacks = [Stack(self.stackSize)]
    
    def __str__(self):
        string = []
        string.append("Stacks [ ")
        for i in range(0, len(self.stacks)):
            string.append(str(self.stacks[i]))
            string.append(", ")
        del(string[-1])
        string.append(" ]")
        string = "".join(string)
        return string

    def isEmpty(self):
        if len(self.stacks) == 1 and self.stacks[0].isEmpty():
            print("Stack is completely empty.")
            return True
        return False

    def isFull(self):
        if len(self.stacks) == self.numberOfStacks and self.stacks[self.numberOfStacks-1].isFull():
            print("Stack is completely full.")
            return True
        return False

    def getLastStack(self):
        return self.stacks[len(self.stacks)-1]

    def peek(self):
        if self.isEmpty():
            return
        return self.getLastStack().peek()

    def insert(self, item):
        if self.isFull():
            return
        last = self.getLastStack()
        if last.isFull():
            self.stacks.append(Stack(self.stackSize))
            last = self.getLastStack() 
        last.insert(item)
        return

    def pop(self):
        if self.isEmpty():
            return
        toReturn = self.getLastStack().pop()
        if self.getLastStack().isEmpty() and len(self.stacks) > 1:
            self.stacks.pop()
        return toReturn

    def popS(self, stackNum):
        if self.isEmpty():
            return
        toReturn = self.stacks[stackNum].pop()
        if self.stacks[stackNum+1] != None and not self.stacks[stackNum+1].isEmpty():
            self.replace(stackNum)
        if self.getLastStack().isEmpty() and len(self.stacks) > 1:
            self.stacks.pop()
        return toReturn
    
    def replace(self, stackNum):
        if stackNum +1 < self.numberOfStacks:
            bottom = self.stacks[stackNum+1].getBottom()
            self.stacks[stackNum].insert(bottom)
            if self.stacks[stackNum+1].isEmpty():
                self.stacks.pop()
            else:
                self.replace(stackNum+1)

        

    

if __name__ == "__main__":
    stackP = StackOfPlates(3, 2)

    print("Inserts")
    stackP.insert(5)
    print(stackP.peek())
    stackP.insert(4)
    print(stackP.peek())
    stackP.insert(3)
    print(stackP.peek())
    stackP.insert(2)
    print(stackP.peek()) 
    stackP.insert(1)
    print(stackP.peek())
    stackP.insert(0)
    print(stackP.peek())
    print(str(stackP))

    print("\nInserts to fill")
    stackP.insert(-1)
    print(stackP.peek())
    print(str(stackP))

    print("\nPops")
    print(stackP.pop())
    print(str(stackP))
    print(stackP.pop())
    print(str(stackP))
    print(stackP.pop())
    print(str(stackP))
    print(stackP.pop())
    print(str(stackP))
    print(stackP.pop())
    print(str(stackP))
    print(stackP.pop())
    print(str(stackP))

    print("\nPop empty")
    print(stackP.pop())
    print(str(stackP))

    print("\nInserts and pops")
    stackP.insert(5)
    print(str(stackP))
    stackP.insert(4)
    print(str(stackP))
    stackP.insert(3)
    print(str(stackP))
    stackP.insert(2)
    print(str(stackP))
    print(stackP.pop())
    print(str(stackP))
    print(stackP.pop())
    print(str(stackP))
    stackP.insert(10)
    print(str(stackP))
    stackP.insert(9)
    print(str(stackP))
    stackP.insert(8)
    print(str(stackP))

    print("\nSpecial pop")
    print(stackP.popS(0))
    print(str(stackP))
    print(stackP.popS(0))
    print(str(stackP))