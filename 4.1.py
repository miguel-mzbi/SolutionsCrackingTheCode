
class BinaryTree():
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None
        self.depth = -1
    
    def __str__(self):
        return "( " + str(self.value) + " ( " + str(self.left) + " | " + str(self.right) + ") )" 

def isBalanced(tree):
    if tree is None:
        return True
    else:
        #depthA(tree)
        if abs(depthA(tree.left) - depthA(tree.right)) > 1:
            print(depthA(tree.left))
            print(depthA(tree.right))
            return False
        return isBalanced(tree.left) and isBalanced(tree.right)

def depthA(tree):
    if tree is None:
        return 0
    else:
        if tree.depth == -1:
            tree.depth = 1 + max(depthA(tree.left), depthA(tree.right))
        return tree.depth

def isBalancedOpt(tree):
    if depthAOpt(tree) == -1:
        return False
    else:
        return True

def depthAOpt(tree):
    if tree is None:
        return 0
    else:
        leftD = depthAOpt(tree.left)
        if leftD == -1:
            return -1

        rightD = depthAOpt(tree.right)
        if rightD == -1:
            return -1

        heightDiff = abs(leftD - rightD)
        if heightDiff > 1:
            return -1
        else:
            tree.depth = max(leftD, rightD) +1
            return tree.depth

if __name__ == "__main__":
    head = BinaryTree(1)
    head.left = BinaryTree(2)
    head.left.left = BinaryTree(3)
    head.left.right = BinaryTree(4)
    head.right = BinaryTree(5)
    head.left.left.left = BinaryTree(6)
    print(isBalanced(head))
    print(isBalancedOpt(head))