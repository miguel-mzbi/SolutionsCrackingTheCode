from LinkedList import *

def isPalindrome(linkedList):
    n = 0
    temp = linkedList.head
    while temp != None:
        n += 1
        temp = temp.next
    isIt, dummy = isPalindromeRec(linkedList.head, n)
    return isIt

def isPalindromeRec(node, lenght):
    if lenght == 0:
        return False, None
    if lenght == 1:
        return True, node.next
    if lenght == 2:
        return node.value == node.next.value, node.next.next
    
    isIt, nodeR = isPalindromeRec(node.next, lenght-2)

    if isIt == False or node.value != nodeR.value:
        return False, nodeR.next
    else:
        return True, nodeR.next

if __name__ == "__main__":
    
    L1 = randomLinkedList(15, 0, 9)
    print(str(L1))
    print(str(isPalindrome(L1)))
    L2 = LinkedList()
    L2.addNode(1)
    L2.addNode(2)
    L2.addNode(3)
    L2.addNode(3)
    L2.addNode(2)
    L2.addNode(1)
    print(str(L2))
    print(str(isPalindrome(L2)))
    L3 = LinkedList()
    L3.addNode(1)
    L3.addNode(2)
    L3.addNode(3)
    L3.addNode(4)
    L3.addNode(3)
    L3.addNode(2)
    L3.addNode(1)
    print(str(L3))
    print(str(isPalindrome(L3)))
    L4 = randomLinkedList(1, 0, 9)
    print(str(L4))
    print(str(isPalindrome(L4)))
    L5 = randomLinkedList(0, 0, 9)
    print(str(L5))
    print(str(isPalindrome(L5)))