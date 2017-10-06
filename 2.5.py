from LinkedList import *

def sumR(linkedList1, linkedList2):
    result = LinkedList()
    digit1 = linkedList1.head
    digit2 = linkedList2.head
    carry = 0
    while digit1 != None or digit2 != None:
        if digit1 == None:
            result.addNode(digit2.value+carry)
            digit2 = digit2.next
        elif digit2 == None:
            result.addNode(digit1.value+carry)
            digit1 = digit1.next
        else:
            result.addNode((digit1.value+digit2.value+carry)%10)
            carry = int((digit1.value+digit2.value+carry)/10)
            digit1 = digit1.next
            digit2 = digit2.next
    return result

def sumFor(linkedList1, linkedList2):
    
    len1 = 0
    len2 = 0
    temp = linkedList1.head
    while temp != None:
        len1 +=1
        temp = temp.next
    temp = linkedList2.head
    while temp != None:
        len2 +=1
        temp = temp.next
    if len1>len2:
        for _ in range(len1-len2):
            t = Node(0)
            t.next = linkedList2.head
            linkedList2.head = t
    elif len1<len2:
        for _ in range(len2-len1):
            t = Node(0)
            t.next = linkedList1.head
            linkedList1.head = t
    print("~~~~~~~~~~~~~~~~~")
    print(str(linkedList1))
    print(str(linkedList2))
    result = LinkedList()
    digit1 = linkedList1.head
    digit2 = linkedList2.head
    carry, nodeR = sumForRec(digit1, digit2)
    if carry > 0:
        temp = Node(carry)
        temp.next = nodeR
        nodeR = temp
    result.head = nodeR  
    print("Result")  
    return result

def sumForRec(digit1, digit2):
    if digit1 == None and digit2 == None:
        return 0,None
    else:
        carryRec, nodeRec = sumForRec(digit1.next, digit2.next)
        carry = int((digit1.value+digit2.value+carryRec)/10)
        node = Node((digit1.value+digit2.value+carryRec)%10)
        node.next = nodeRec
        return carry, node
        

if __name__ == "__main__":
    print("Reversed")
    L1 = randomLinkedList(10, 0, 9)
    L2 = randomLinkedList(15, 0, 9)
    print(str(L1))
    print(str(L2))
    print("Result")
    print(str(sumR(L1, L2)))
    print("\nForward")
    L1 = randomLinkedList(10, 0, 9)
    L2 = randomLinkedList(15, 0, 9)
    print(str(L1))
    print(str(L2))
    print(str(sumFor(L1, L2)))