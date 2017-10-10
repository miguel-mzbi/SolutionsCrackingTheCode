from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, date):
        self.name = name
        self.date = date

    @abstractmethod
    def __str__(self):
        pass

    def isOlderThan(other):
        return self.date < other.date


class Dog(Animal):
    def __str__(self):
        return "( Dog: " + self.name + ", date: " + str(self.date) + " )"

class Cat(Animal):
    def __str__(self):
        return "( Cat: " + self.name + ", date: " + str(self.date) + " )"

class Queue():
    def __init__(self, queueSize = 100):
        self.queueSize = queueSize
        self.queue = []
    
    def __str__(self):
        string = []
        string.append("Queue [ ")
        if self.isEmpty():
            string.append("None")
        else:
            for i in range(0, len(self.queue)):
                string.append(str(self.queue[i]))
                string.append(",")
            del(string[-1])
        string.append(" ]")
        string = "".join(string)
        return string

    def isEmpty(self):
        return len(self.queue) == 0

    def isFull(self):
        return len(self.queue) == self.queueSize

    def front(self):
        if self.isEmpty():
            return
        return self.queue[0]

    def back(self):
        if self.isEmpty():
            return
        return self.queue[-1]

    def enqueue(self, item):
        if self.isFull():
            return
        self.queue.append(item)
        return

    def dequeue(self):
        if self.isEmpty():
            return
        return self.queue.pop(0)

class AnimalQueue():
    def __init__(self, queueSize = 100):
        self.queueSize = queueSize
        self.catQueue = Queue(self.queueSize)
        self.dogQueue = Queue(self.queueSize)
    
    def __str__(self):
        string = []
        string.append("Cat ")
        string.append(str(self.catQueue))
        string.append(", ")
        string.append("Dog ")
        string.append(str(self.dogQueue))
        string = "".join(string)
        return string

    def enqueue(self, item):
        if isinstance(item, Cat):
            self.catQueue.enqueue(item)
        else:
            self.dogQueue.enqueue(item)
    
    def dequeueAny(self):
        cat = self.catQueue.front()
        dog = self.dogQueue.front()
        if cat == None or dog.date < cat.date:
            return self.dogQueue.dequeue()
        else:
            return self.catQueue.dequeue()
    
    def dequeueCat(self):
        return self.catQueue.dequeue()

    def dequeueDog(self):
        return self.catQueue.dequeue()

if __name__ == "__main__":
    queue = AnimalQueue(3)
    print(str(queue))
    queue.enqueue(Cat("cat1", 1))
    queue.enqueue(Cat("cat2", 1))
    queue.enqueue(Cat("cat3", 10))
    print(str(queue))
    queue.enqueue(Dog("dog1", 1))
    queue.enqueue(Dog("dog2", 2))
    queue.enqueue(Dog("dog3", 10))
    print(str(queue))

    print(str(queue.dequeueAny()))
    print(str(queue))
    print(str(queue.dequeueCat()))
    print(str(queue))
    print(str(queue.dequeueAny()))
    print(str(queue))
    print(str(queue.dequeueDog()))
    print(str(queue))
    print(str(queue.dequeueAny()))
    print(str(queue))
    