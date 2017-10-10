
class QueueInStacks():
    def __init__(self, size = 100):
        self.enqueueStack = []
        self.dequeueStack = []
        self.size = size
        self.currentlyIn = 0 # 0 - enqueueStack, 1 - dequeueStack
    
    def __str__(self):
        string = []
        string.append("Queue: ")
        if self.currentlyIn == 0:
            string.append(" Front--> [ ")
            myStack = self.enqueueStack
        else:
            string.append("[ ")
            myStack = self.dequeueStack

        if len(myStack) == 0:
            string.append("None")
        else:
            for i in range(len(myStack)):
                string.append(str(myStack[i]))
                string.append(",")
            del(string[-1])

        if self.currentlyIn == 0:
            string.append(" ] ")
        else:
            string.append(" ] <--Front ")
        
        string = "".join(string)
        return string

    def isEmpty(self):
        if self.currentlyIn == 0:
            myStack = self.enqueueStack
        else:
            myStack = self.dequeueStack
        return len(myStack) == 0

    def isFull(self):
        if self.currentlyIn == 0:
            myStack = self.enqueueStack
        else:
            myStack = self.dequeueStack
        return len(myStack) == self.size

    def enqueue(self, item):
        if self.isFull():
            print("Queue is full.")
            return
        if self.currentlyIn == 1:
            while self.dequeueStack:
                self.enqueueStack.append(self.dequeueStack.pop())
            self.currentlyIn = 0
        self.enqueueStack.append(item)
        return

    def back(self):
        if self.isEmpty():
            print("Queue is empty.")
            return
        if self.currentlyIn == 1:
            while self.dequeueStack:
                self.enqueueStack.append(self.dequeueStack.pop())
            self.currentlyIn = 0
        return self.enqueueStack[len(self.enqueueStack)-1]

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty.")
            return
        if self.currentlyIn == 0:
            while self.enqueueStack:
                self.dequeueStack.append(self.enqueueStack.pop())
            self.currentlyIn = 1
        return self.dequeueStack.pop()

    def front(self):
        if self.isEmpty():
            print("Queue is empty.")
            return
        if self.currentlyIn == 0:
            while self.enqueueStack:
                self.dequeueStack.append(self.enqueueStack.pop())
            self.currentlyIn = 1
        return self.dequeueStack[len(self.dequeueStack)-1]

if __name__ == "__main__":
    queue = QueueInStacks(3)

    print(str(queue))

    print("\nFront when empty")
    print("F: " + str(queue.front()))
    print(str(queue))

    print("\nBack when empty")
    print("B: " + str(queue.back()))
    print(str(queue))

    print("\nInserts with front and back")
    queue.enqueue(1)
    print("F: " + str(queue.front()))
    print("B: " + str(queue.back()))
    print(str(queue))
    queue.enqueue(2)
    print("F: " + str(queue.front()))
    print("B: " + str(queue.back()))
    print(str(queue))
    queue.enqueue(3)
    print("F: " + str(queue.front()))
    print("B: " + str(queue.back()))
    print(str(queue))

    print("\nInserts when full")
    queue.enqueue(4)
    print("F: " + str(queue.front()))
    print("B: " + str(queue.back()))

    print("\nDequeues")
    print("B: " + str(queue.back()))
    print("F: " + str(queue.front()))
    print(str(queue))
    print(str(queue.dequeue()))
    print(str(queue))
    print(str(queue.dequeue()))
    print(str(queue))
    print(str(queue.dequeue()))
    print(str(queue))

    print("\nDequeue when empty")
    print("B: " + str(queue.back()))
    print("F: " + str(queue.front()))
    print(str(queue.dequeue()))
    print(str(queue))

    print("\Enqueues and dequeues")
    print("B: " + str(queue.back()))
    print("F: " + str(queue.front()))
    print(queue.enqueue(10))
    print(str(queue))
    print(queue.enqueue(20))
    print(str(queue))
    print(str(queue.dequeue()))
    print(str(queue))
    print(queue.enqueue(30))
    print(str(queue))
    print(queue.enqueue(40))
    print(str(queue))
    print(str(queue.dequeue()))
    print(str(queue))
