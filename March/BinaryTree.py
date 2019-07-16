class TreeNode:
    def __init__(self,val):
        self.value = val
        self.left = None
        self.right = None
        self.parent = None


class BinaryTreeImplement:
    def __init__(self,data):
        self.root = TreeNode(data)
        self.maxval = float("-infinity")
        self.bst_min = float("-infinity")
        self.bst_max = float("infinity")
        self.listpath = []

    def addnewnodeBinaryTreeBF(self, currentNode, newTreeNode):
        # print("currentNode",currentNode.value,newTreeNode.value)
        if currentNode:
            if currentNode.value > newTreeNode.value:
                if currentNode.left is None:
                    currentNode.left = newTreeNode
                    # print(currentNode.left.value)
                    return True
                else:
                    self.addnewnodeBinaryTreeBF(currentNode.left,newTreeNode)
            elif currentNode.value <= newTreeNode.value:
                if currentNode.right is None:
                    currentNode.right = newTreeNode
                    # print(currentNode.right.value)
                    return True
                else:
                    self.addnewnodeBinaryTreeBF(currentNode.right,newTreeNode)
        else:
            # print("root node is empty")
            return False

    def printinorderworecurrsion(self, root):
        current = root
        stacklist = []

        continuePrint = True
        # print("without recurrsion")
        while continuePrint:
            # print("inside while",self.current.value)
            if current is not None:
                stacklist.append(current)
                current = current.left

            else:
                if len(stacklist) > 0 :
                    newnode = stacklist.pop()
                    print(newnode.value,end=",")
                    current = newnode.right
                else:
                    continuePrint = False

    def addleftnode(self, treeNode):
        lastleft = self.root
        while lastleft is not None:
            #print(lastleft.val)
            previous = lastleft
            lastleft= lastleft.left
        previous.left= treeNode
    def addrightnode(self, treeNode):
        lastright = self.root
        while lastright is not None:
            previous = lastright
            lastright= lastright.right
        previous.right= treeNode
    def printinorder(self,rootNode):
        if rootNode:
            self.printinorder(rootNode.left)
            print(rootNode.value,end=",")
            self.printinorder(rootNode.right)
    def printpostorder(self,rootNode):
        if rootNode:
            self.printpostorder(rootNode.left)
            self.printpostorder(rootNode.right)
            print(rootNode.value)
    def printpreorder(self,rootNode):
        if rootNode:
            print(rootNode.value)
            self.printpreorder(rootNode.left)
            self.printpreorder(rootNode.right)
###################################################
    def printDFS(self,rootNode):
        heightoftree = self.calHeight(rootNode)
        #print("heightoftree",heightoftree)
        for level in range(1, heightoftree+1):
            self.printDFSwithLevel(rootNode,level)
            print(" ")
    def printDFSwithLevel(self,root, level):
        if root is None:
            return False
        if level == 1:
            print(root.value,end=",")
        elif level > 1:
            self.printDFSwithLevel(root.left, level - 1)
            self.printDFSwithLevel(root.right, level - 1)
    def calHeight(self, rootNode):
        if rootNode == None:
            return 0
        else:
            lheight = self.calHeight(rootNode.left)
            rheight = self.calHeight(rootNode.right)
        #print("lheight,rheight",lheight,rheight)
        return max(lheight, rheight)+1
###################################################
    def clone(self,root):
        if root == None:
            return None
        newNode = TreeNode(root.value)
        newNode.left = self.clone(root.left)
        newNode.right = self.clone(root.right)
        return newNode
    def mirrorimage(self,root):
        if root == None:
            return
        self.mirrorimage(root.left)
        self.mirrorimage(root.right)
        temp = root.left
        root.left = root.right
        root.right = temp
    #########################################
    def compare(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        elif root1 is None or root2 is None:
            return False
        elif root1.value != root2.value:
            return False
        return self.compare(root1.left,root2.left) and self.compare(root1.right,root2.right)
    def max(self,root): # validate if its a BST
        if root == None:
            return self.maxval
        if root.value > self.maxval:
            self.maxval = root.value
        self.max(root.left)
        self.max(root.right)
        return self.maxval
    def finddepth(self,root):
        if root == None:
            return 0
        q = []
        q.append([root,1])
        depth = 0
        count = 0
        while q:
            node, temp = q.pop()
            depth = temp
            #print(node.value)
            if node.left is not None and node.right is not None:
                count = count+1
               # print("count:-",count)
            if node.left is not None : q.append([node.left,depth+1])
            if node.right is not None: q.append([node.right,depth+1])
        return depth
    def findmaxdepth(self,root):
        if root is None:
            return 0

        # base case leaf node
        if root.left is None and root.right is None:
            return 1

        if not root.left:
            return self.finddepth(root.right) + 1
        if not root.right:
            self.finddepth(root.left) + 1

        return min(self.finddepth(root.right),self.finddepth(root.left))+1
    def printroottoleafpaths(self,root):
        if root is None:
            return

        self.listpath.append(root.value)
        self.printroottoleafpaths(root.left)
        print(self.listpath)
        k = self.listpath.pop()
        self.printroottoleafpaths(root.right)
        print(self.listpath)
        k = self.listpath.pop()
    def isbinsumtree(self,root):
        if root is None:
            return 0

        if root.left == None and root.right == None:
            return root.value

        if root.value != root.left.value + root.right.value:
            return -1

        left = self.isbinsumtree(root.left)
        if left == -1:
            return -1

        right = self.isbinsumtree(root.right)
        if right == -1:
            return -1


    def lca(self,root,elem1,elem2):
        if root is None or elem1 == None or elem2 == None:
            return 0

        if root.value == elem1 or root.value == elem2:
            print(root.value)
            return root

        left_lca = self.lca(root.left,elem1,elem2)
        right_lca = self.lca(root.right,elem1,elem2)

        if left_lca != 0 and right_lca != 0:
            return root

        if left_lca != 0:
            return left_lca

        if right_lca != 0:
            return right_lca





objBinaryTree = BinaryTreeImplement(11)
for i in [5,10,15,6,7,20,25,1,2,30,40]:
    objBinaryNode = TreeNode(i)
    objBinaryTree.addnewnodeBinaryTreeBF(objBinaryTree.root,objBinaryNode)

objBinaryTree2 = BinaryTreeImplement(11)
for i in [50,10,40,9,1,21,19,1,8,30,40]:
    objBinaryNode = TreeNode(i)
    objBinaryTree2.addnewnodeBinaryTreeBF(objBinaryTree2.root,objBinaryNode)


###################################################################
print("inorder")
objBinaryTree2.printinorder(objBinaryTree2.root)
#print("postorder")
#objBinaryTree.printpostorder(objBinaryTree.root)
#print("preorder")
#objBinaryTree.printpreorder(objBinaryTree.root)
#print("DFS")
#objBinaryTree.printDFS(objBinaryTree.root)
#print("without recurrsion")
#objBinaryTree.printinorderworecurrsion(objBinaryTree.root)
#clonetreeroot = objBinaryTree.clone(objBinaryTree.root)

#print("without recurrsion clone")
#objBinaryTree.printinorderworecurrsion(clonetreeroot)
#swaproot = objBinaryTree.mirrorimage(objBinaryTree.root)
#print("clonetree")
#objBinaryTree.printinorderworecurrsion(objBinaryTree.root)
#swaproot = objBinaryTree.mirrorimage(objBinaryTree.root)
#print("origtree")
#objBinaryTree.printinorderworecurrsion(objBinaryTree.root)
#print("compare")
#print(objBinaryTree.compare(objBinaryTree.root,objBinaryTree2.root))
#print(objBinaryTree.root)
##################################################################
print("Max Tree")
print(objBinaryTree.calHeight(objBinaryTree.root))

#print(objBinaryTree.max(objBinaryTree.root))
print("---------depth-------------")
print(objBinaryTree.finddepth(objBinaryTree.root))
print("---------depth recurssion-------------")
print(objBinaryTree.findmaxdepth(objBinaryTree.root))
#objBinaryTree.printroottoleafpaths(objBinaryTree.root)

objbt4 = BinaryTreeImplement(50)
treeNodeTemp = TreeNode(22)
objbt4.addleftnode(treeNodeTemp)
treeNodeTemp = TreeNode(28)
"""
objbt4.addrightnode(treeNodeTemp)
treeNodeTemp = TreeNode(24)
objbt4.addleftnode(treeNodeTemp)
treeNodeTemp = TreeNode(32)
objbt4.addrightnode(treeNodeTemp)
"""

#print(objbt4.isbinsumtree(objbt4.root))
#print(objbt4.lca(objbt4.root,22,28).value)