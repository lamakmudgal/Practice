
class LinkListNode:
    def __init__(self,data):
        self.data = data
        self.nextNode = None
        self.downNode = None

class LinkList(LinkListNode):
    def __init__(self,data):
        self.headNode = LinkListNode(data)

    def addNode(self,data):
        currNode = self.headNode
        while currNode.nextNode is not None:
            currNode = currNode.nextNode
        newNode = LinkListNode(data)
        currNode.nextNode = newNode

    def printlinklist(self,headNode):
        currNode = headNode
        count = 1
        while currNode is not None and count !=3:
            print("Node :- ",currNode.data)
            if currNode.data == 38:
                count = count + 1
            currNode = currNode.nextNode

    def findintersectingpointhash(self,headnode1,headnode2):
        #self.printlinklist(headnode1)
        #self.printlinklist(headnode2)
        hashlist = []
        while headnode1:
            hashlist.append(headnode1)
            headnode1 = headnode1.nextNode
        #print(hashlist)
        while headnode2:
            if headnode2 in hashlist:
                #print(headnode2.data)
                return headnode2
            headnode2 = headnode2.nextNode
        return None

    def findintersectingpointstack(self,headnode1,headnode2):
        stack1 = []
        stack2 = []
        while headnode1 or headnode2:
            if headnode1 is not None:
                stack1.append(headnode1)
                headnode1 = headnode1.nextNode
            if headnode2 is not None:
                stack2.append(headnode2)
                headnode2 = headnode2.nextNode
        print(len(stack1))
        print(len(stack2))
        while stack1.pop() == stack2.pop():
            pass
        print(stack2.pop().nextNode.data)

    def findintersectionlength(self,h1,h2,l1,l2):
        if l1>l2:
            bigger = h1
            smaller = h2
            diff = l1-l2
        else:
            bigger = h2
            smaller = h1
            diff = l2-l1

        for i in range(0,diff):
            bigger = bigger.nextNode

        while bigger and smaller:
            if bigger == smaller:
                print(bigger.data)
                return bigger
            bigger = bigger.nextNode
            smaller = smaller.nextNode

    def findnthnodefromend(self,rootNode,n):
        if rootNode is None:
            return  -1
        nthnode = rootNode
        nodeptr = rootNode
        count = 0
        #print(rootNode.data)
        while nodeptr and nthnode  :
            #print(nodeptr.data)
            if count < n:
                nodeptr = nodeptr.nextNode
                count = count+1
            else:
                nodeptr = nodeptr.nextNode
                nthnode = nthnode.nextNode

        print("nth node is ",nthnode.data)

l1 = LinkList(2)
l1.addNode(4) , l1.addNode(5),l1.addNode(150)
l2 = LinkList(3)
l2.addNode(8) , l2.addNode(15), l2.addNode(18) , l2.addNode(20) , l2.addNode(28) , l2.addNode(35)
l1.headNode.nextNode.nextNode.nextNode.nextNode = l2.headNode.nextNode.nextNode.nextNode
#l1.printlinklist(l1.headNode)
#l2.printlinklist(l2.headNode)

#print(l1.findintersectingpointhash(l1.headNode,l2.headNode))
#l1.findintersectingpointstack(l1.headNode,l2.headNode)
#l1.findintersectionlength(l1.headNode,l2.headNode,8,7)
l3= LinkList(3)
l3.addNode(8) , l3.addNode(15), l3.addNode(18) , l3.addNode(20) , l3.addNode(28) , l3.addNode(35), l3.addNode(90)
l3.findnthnodefromend(l3.headNode,5)

