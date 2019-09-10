import queue
class Node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Tree():
    def __init__(self,data):
        self.root = Node(data)
        self.maxval = -1
        self.path = [""]
        self.paths = [[]]

    def addleftnode(self, treeNode):
        lastleft = self.root
        newNode = Node(treeNode)
        while lastleft is not None:
            # print(lastleft.val)
            previous = lastleft
            lastleft = lastleft.left
        previous.left = newNode

    def addrightnode(self, treeNode):
        lastright = self.root
        newNode = Node(treeNode)
        while lastright is not None:
            previous = lastright
            lastright = lastright.right
        previous.right = newNode

    def printinorder(self, rootNode):
        if rootNode:
            self.printinorder(rootNode.left)
            print(rootNode.data, end=",")
            self.printinorder(rootNode.right)

    def printpostorder(self, rootNode):
        if rootNode:
            self.printpostorder(rootNode.left)
            self.printpostorder(rootNode.right)
            print(rootNode.data)

    def printpreorder(self, rootNode):
        if rootNode:
            print(rootNode.data)
            self.printpreorder(rootNode.left)
            self.printpreorder(rootNode.right)

    def height(self,rootNode):
        #print(rootNode.data)
        if rootNode is None:
            return 0
        return max(self.height(rootNode.left), self.height(rootNode.right))+1

    def findheightiter(self,root):
        if root is None:
            return
        tq = queue.Queue()
        tq.put(root)
        tq.put(None)
        count = 0
        while not tq.empty():
            elem = tq.get()
            if elem is None:
                count += 1
                if not tq.empty():
                    tq.put(None)
            else:
                print(elem.data)
                if elem.left is not None:
                    tq.put(elem.left)
                if elem.right is not None:
                    tq.put(elem.right)
        return count


    def findmax(self,rootNode):
        if rootNode is None:
            return self.maxval
        self.maxval = max(rootNode.data,self.maxval)
        self.findmax(rootNode.left)
        self.findmax(rootNode.right)
        return self.maxval

    def findelem(self,root,elem,res):
        if root is None:
            return
        print(root.data)
        if root.data == elem:
            print("found")
            res = 1
            return res
        else:
            res = self.findelem(root.left,elem,res)
            if res == 1:
                return res
            return self.findelem(root.right,elem,res)

    def addelemlevel(self,root,data):
        if root is None:
            return
        newNode = Node(data)
        treeQ = queue.Queue()
        treeQ.put(root)
        while not treeQ.empty():
            elem = treeQ.get()
            if elem.left is None:
                print("added in left of ",elem.data)
                elem.left = newNode
                #return 1
            else:
                treeQ.put(elem.left)
            if elem.right is None:
                print("added in right of ", elem.data)
                elem.right = newNode
                #return 1
            else:
                treeQ.put(elem.right)

    def findpaths(self,root,path,paths):
        print("path",path)
        if root is None:
            paths.append(path)
            return
        path.append(root.data)
        self.findpaths(root.left,path+[root.data],paths)
        self.findpaths(root.right,path+[root.data],paths)

treeObj = Tree(1)
treeObj.addleftnode(2)
treeObj.addleftnode(12)
treeObj.addleftnode(20)
treeObj.addleftnode(29)
treeObj.addrightnode(30)
treeObj.addrightnode(30)
treeObj.addrightnode(35)
print(treeObj.height(treeObj.root))
#print(treeObj.findmax(treeObj.root))
#print(treeObj.findelem(treeObj.root,12,0))
#print(treeObj.addelemlevel(treeObj.root,3))
#print(treeObj.printpreorder(treeObj.root))
#print("count is:-",treeObj.findheightiter(treeObj.root))
paths = []
#treeObj.findpaths(treeObj.root,[],paths)
#print(paths)
