from LinkedList import *

def loopStart(linkedList):
    fast = linkedList.head
    slow = linkedList.head
    while slow != None and fast != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    if slow == None or fast == None:
        return None
    slow = linkedList.head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow

if __name__ == "__main__":
    
    L1 = randomLinkedList(15, 0, 9)
    print(str(L1))
    print("Start of loop is the 5th element")
    start = L1.head.next.next.next.next
    L1.tail.next = start
    print("Starting node of loop")
    print(str(loopStart(L1)))