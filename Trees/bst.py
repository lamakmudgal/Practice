# Python program to check if a binary tree is bst or not
INT_MAX = 4294967296
INT_MIN = -4294967296


# A binary tree node
class Node:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Returns true if the given tree is a binary search tree
# (efficient version)
def isBST(node):
    return isBSTUtil(node, INT_MIN, INT_MAX)


# Return true if the given tree is a BST and its values
# >= min and <= max
def isBSTUtil(node, mini, maxi):
    # An empty tree is BST
    if node is None:
        return True

    # False if this node violates min/max constraint
    if node.data < mini or node.data > maxi:
        return False

    # Otherwise check the subtrees recursively
    # tightening the min or max constraint
    return (isBSTUtil(node.left, mini, node.data) and
            isBSTUtil(node.right, node.data, maxi))


def printBoundaryLeft(root):
    if root is None:
        return
    if root.left:
        print(root.data)
        printBoundaryLeft(root.left)
    elif root.right:
        print(root.data)
        printBoundaryLeft(root.right)

    """
    if (root):
        if (root.left):

            # to ensure top down order, print the node
            # before calling itself for left subtree
            print(root.data)
            printBoundaryLeft(root.left)
            print("return from left")

        elif (root.right):
            print("this",root.data)
            printBoundaryLeft(root.right)
            print("return from right",root.data)
   """
def printboundryright(root):
    if root:
        if root.right:
            printboundryright(root.right)
            print(root.data)
        elif root.left:
            printboundryright(root.left)
            print(root.data)

def printLeaves(root):
    if (root):
        printLeaves(root.left)

        # Print it if it is a leaf node
        if root.left is None and root.right is None:
            print(root.data),

        printLeaves(root.right)

                # Driver program to test above function
root = Node(40)
root.left = Node(30)
root.right = Node(45)
root.left.left = Node(29)
root.left.left.right = Node(32)
root.left.left.right.left = Node(333)
root.left.left.right.right = Node(444)
root.left.right = Node(31)
root.right.left = Node(44)
root.right.right = Node(46)
printBoundaryLeft(root)
printLeaves(root)
printboundryright(root.right)
if (isBST(root)):
    print("Is BST")
else:
    print("Not a BST")