
class StackWithMin():
    def __init__(self, stackSize = 100):
        self.stackSize = stackSize
        self.stack = []
        self.minStack = []
    
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

    def peek(self):
        if self.isEmpty():
            return
        return self.stack[len(self.stack)-1]

    def peekMin(self):
        if self.isEmpty():
            return
        return self.minStack[len(self.minStack)-1]

    def insert(self, item):
        if len(self.stack) == self.stackSize:
            print("Stack is full.")
            return
        self.stack.append(item)
        if len(self.minStack) == 0 or item <= self.peekMin():
            self.minStack.append(item)
        return

    def pop(self):
        if self.isEmpty():
            return
        toReturn = self.stack.pop()
        if toReturn == self.peekMin():
            self.minStack.pop()
        return toReturn

    def isEmpty(self):
        if len(self.stack) == 0:
            print("Stack is empty.")
            return True
        return False

if __name__ == "__main__":
    stack = StackWithMin(5)

    print("Inserts")
    stack.insert(5)
    print(stack.peek())
    print("M: "+str(stack.peekMin()))
    stack.insert(4)
    print(stack.peek())
    print("M: "+str(stack.peekMin()))
    stack.insert(3)
    print(stack.peek())
    print("M: "+str(stack.peekMin()))
    stack.insert(2)
    print(stack.peek()) 
    print("M: "+str(stack.peekMin()))
    stack.insert(1)
    print(stack.peek())
    print("M: "+str(stack.peekMin()))
    print(str(stack))

    print("\nInserts to fill")
    stack.insert(5)
    print(stack.peek())
    print("M: "+str(stack.peekMin()))
    print(str(stack))

    print("\nPops")
    print(stack.pop())
    print("M: "+str(stack.peekMin()))
    print(str(stack))
    print(stack.pop())
    print("M: "+str(stack.peekMin()))
    print(str(stack))
    print(stack.pop())
    print("M: "+str(stack.peekMin()))
    print(str(stack))
    print(stack.pop())
    print("M: "+str(stack.peekMin()))
    print(str(stack))
    print(stack.pop())
    print("M: "+str(stack.peekMin()))
    print(str(stack))

    print("\nPop empty")
    print(stack.pop())
    print("M: "+str(stack.peekMin()))
    print(str(stack))