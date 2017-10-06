from LinkedList import *

def deleteDup(linkedList):
    if linkedList.head != None:
        temp = linkedList.head
        app = {temp.value: True}
        while temp.next != None:
            if temp.next.value not in app.keys():
                app[temp.next.value] = True
                temp = temp.next
            else:
                if temp.next.next == None:
                    linkedList.tail = temp
                temp.next = temp.next.next
    return linkedList

def deleteDupNoBuff(linkedList):
    curr = linkedList.head
    while curr != None and curr.next != None:
        comp = curr
        while comp.next != None:
            if comp.next.value == curr.value:
                if comp.next.next == None:
                    linkedList.tail = comp
                comp.next = comp.next.next
            else:
                comp = comp.next
        curr = curr.next
    return linkedList

if __name__ == "__main__":
    
    L1 = randomLinkedList(9, 3, 7)
    print(str(L1))
    print(str(deleteDup(L1)))
    print()
    L2 = randomLinkedList(9, 3, 7)
    print(str(L2))
    print(str(deleteDupNoBuff(L2)))