from LinkedList import *

def kth(linkedList, k):
    if linkedList.head != None:
        myTail = linkedList.head
        for _ in range(k-1):
            if myTail.next != None:
                myTail = myTail.next
            else:
                return "LL isn't long enough"
        myHead = linkedList.head
        while myTail.next != None:
            myTail = myTail.next
            myHead = myHead.next
        return myHead

if __name__ == "__main__":
    
    L1 = randomLinkedList(9, 3, 7)
    k=4
    print(str(L1))
    print("Looking for "+str(k)+"th element: "+str(kth(L1,k)))
    print()
    L2 = randomLinkedList(4, 3, 7)
    k=6
    print(str(L2))
    print("Looking for "+str(k)+"th element: "+str(kth(L2,k)))