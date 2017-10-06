from random import randint

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __str__(self):
        if self.head != None:
            temp = self.head
            string = [str(temp)]
            while temp.next != None:
                temp = temp.next
                string.append(str(temp))
            return "LinkedList [ " + "->".join(string) + " ]"
        return "LinkedList []"

    def addNode(self, value):
        node = Node(value)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
    
    def removeNode(self, valueR):
        temp = self.head
        if temp.value == valueR:
            self.head = self.head.next
        while temp.next != None:
            if temp.next.value == valueR:
                if temp.next.next == None:
                    self.tail = temp
                temp.next = temp.next.next
                break
            else:
                temp = temp.next

def randomLinkedList(length, min, max):
    linkedlist = LinkedList()
    for i in range(length):
        value = randint(min, max)
        linkedlist.addNode(value)
    return linkedlist