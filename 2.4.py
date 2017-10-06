from LinkedList import *

def partition(linkedList, value):
    greater = None
    greaterFirst = None
    lesser = None
    lesserFirst = None
    temp = linkedList.head
    while temp != None:
        if temp.value >= value:
            if greaterFirst == None:
                greater = temp
                greaterFirst = greater
            else:
                greater.next = temp
                greater = greater.next
        else:
            if lesserFirst == None:
                lesser = temp
                lesserFirst = lesser
            else:
                lesser.next = temp
                lesser = lesser.next
        temp = temp.next
    greater.next = None
    lesser.next = greaterFirst
    linkedList.head = lesserFirst
    return linkedList

if __name__ == "__main__":
    
    L1 = randomLinkedList(9, 3, 7)
    print(str(L1))
    print("Partition around 5")
    print(str(partition(L1, 5)))
    print()
    L2 = randomLinkedList(15, 3, 12)
    print(str(L2))
    print("Partition around 7")
    print(str(partition(L2, 7)))