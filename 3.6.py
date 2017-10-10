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

    def peek(self):
        if self.isEmpty():
            return
        return self.stack[len(self.stack)-1]

    def insert(self, item):
        if len(self.stack) == self.stackSize:
            return
        self.stack.append(item)
        return

    def pop(self):
        if self.isEmpty():
            return
        toReturn = self.stack.pop()
        return toReturn

def sortStack(stack):
    if stack.stackSize == 0:
        return stack
    helper = Stack(stack.stackSize)
    helper.insert(stack.pop())
    while not stack.isEmpty():
        item = stack.pop()
        while not helper.isEmpty() and helper.peek() < item:
            stack.insert(helper.pop())
        helper.insert(item)
    while not helper.isEmpty():
        stack.insert(helper.pop())
    return stack



if __name__ == "__main__":
    stack = Stack(10)
    stack.insert(10)
    stack.insert(9)
    stack.insert(8)
    stack.insert(7)
    stack.insert(6)
    stack.insert(5)
    stack.insert(4)
    stack.insert(3)
    stack.insert(2)
    stack.insert(1)
    print(str(stack))
    print("Sorting.")
    print(str(sortStack(stack)))

    