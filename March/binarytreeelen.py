# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class TreeClass:
    def __init__(self,data):
        self.root = TreeNode(data)

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
        #print(lastright.val)

    def printinorder(self,rootNode):
        if rootNode:
            self.printinorder(rootNode.left)
            print(rootNode.val)
            self.printinorder(rootNode.right)

    def printpostorder(self,rootNode):
        if rootNode:
            self.printpostorder(rootNode.left)
            self.printpostorder(rootNode.right)
            print(rootNode.val)

    def printpreorder(self,rootNode):
        if rootNode:
            print(rootNode.val)
            self.printpreorder(rootNode.left)
            self.printpreorder(rootNode.right)

    #def longestunivaluepath(self,root):
    def dfs(self, root):
        print("Start again")
        if not root:
            return 0,0
        elif not root.left and not root.right:
            print("here")
            return 1, 1
        print("Count:-", root.val)
        l_here, l_max = self.dfs(root.left)
        print("left", l_here, l_max)
        r_here, r_max = self.dfs(root.right)
        print("right", r_here, r_max)
        max_here = 1
        print("calculating max_here")
        if root.left and root.left.val == root.val:
            print("calculating max_left")
            max_here =  1+l_here
        if root.right and root.right.val == root.val:
            print("calculating max_right")
            max_here = max(max_here, 1 +r_here)

        if root.left and root.right and root.left.val == root.val and root.right.val == root.val:
            print("calculating left and right with root")
            return  max_here, max(l_here+r_here+1,l_max,r_max)
        print("calculating left and right not with root")
        return max_here,max(l_max,r_max,max_here)

    #if not root:
    #    return 0
    #return dfs(root)[1]-1

objtreeclass = TreeClass(5)
#newrightnode = TreeNode(5)
objtreeclass.root.left = TreeNode(4)
objtreeclass.root.left.left = TreeNode(1)
objtreeclass.root.left.right = TreeNode(1)
objtreeclass.root.right = TreeNode(5)
objtreeclass.root.right.right = TreeNode(5)
#objtreeclass.root.right.left = TreeNode(2)
#newleftnode = TreeNode(3)
#objtreeclass.addleftnode(TreeNode(12))
#objtreeclass.addrightnode(TreeNode(15))
#objtreeclass.printinorder(objtreeclass.root)
#objtreeclass.printpostorder(objtreeclass.root)
#objtreeclass.printpreorder(objtreeclass.root)

print(objtreeclass.dfs(objtreeclass.root))
