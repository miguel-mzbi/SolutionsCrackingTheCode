from LinkedList import *

def delete(node):
    if node.next != None:
        node.value = node.next.value
        node.next = node.next.next
    elif node.next == None:
        node.value = None
        node = None

if __name__ == "__main__":
    
    L1 = randomLinkedList(9, 3, 7)
    k = L1.head.next.next
    print(str(L1))
    print("Deleting 3rd node.")
    delete(k)
    print(str(L1))
    print()
    L2 = randomLinkedList(5, 3, 7)
    k = L2.head.next.next.next.next
    print(str(L2))
    print("Deleting 5th node.")
    delete(k)
    print(str(L2))