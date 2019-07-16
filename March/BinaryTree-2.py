class TreeNode:
    def __init__(self,val):
        self.value = val
        self.left = None
        self.right = None
        self.parent = None

class BinaryTreeImplement:
    def __init__(self,data):
        self.root = TreeNode(data)
        self.maxval = float("-Infinity")

    def addleftnode(self, treeNode):
        lastleft = self.root
        while lastleft is not None:
            #print(lastleft.val)
            previous = lastleft
            lastleft = lastleft.left
        previous.left= treeNode
    def addrightnode(self, treeNode):
        lastright = self.root
        while lastright is not None:
            previous = lastright
            lastright = lastright.right
        previous.right= treeNode

    def addnewnodeBinaryTreeBF(self, currentNode, newTreeNode):
        # print("currentNode",currentNode.value,newTreeNode.value)
        if currentNode:
            if currentNode.value > newTreeNode.value:
                if currentNode.left == None:
                    currentNode.left = newTreeNode
                    # print(currentNode.left.value)
                    return True
                else:
                    self.addnewnodeBinaryTreeBF(currentNode.left, newTreeNode)
            elif currentNode.value <= newTreeNode.value:
                if currentNode.right == None:
                    currentNode.right = newTreeNode
                    # print(currentNode.right.value)
                    return True
                else:
                    self.addnewnodeBinaryTreeBF(currentNode.right, newTreeNode)
        else:
            # print("root node is empty")
            return False

    def printinorder(self, rootNode):
        if rootNode:
            self.printinorder(rootNode.left)
            print(rootNode.value, end=",")
            self.printinorder(rootNode.right)

    def printpostorder(self, rootNode):
        if rootNode:
            self.printpostorder(rootNode.left)
            self.printpostorder(rootNode.right)
            print(rootNode.value)

    def printpreorder(self, rootNode):
        if rootNode:
            print(rootNode.value)
            self.printpreorder(rootNode.left)
            self.printpreorder(rootNode.right)


    def maxintree(self,rootNode):
        #global self.maxval
        if rootNode is None:
            return self.maxval

        if rootNode.value > self.maxval:
            self.maxval = rootNode.value

        self.maxintree(rootNode.left)
        self.maxintree(rootNode.right)

        return self.maxval

objBinaryTree = BinaryTreeImplement(11)
for i in [5,10,15,6,70,20,25,1,2,30,40]:
    objBinaryNode = TreeNode(i)
    objBinaryTree.addnewnodeBinaryTreeBF(objBinaryTree.root,objBinaryNode)
objBinaryTree.printinorder(objBinaryTree.root)
print("---------------------")
print(objBinaryTree.maxintree(objBinaryTree.root))