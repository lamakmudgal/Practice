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

    def reverselinklist(self,headNode):
        if headNode is None: # Error Statement
            print("was I here")
            return 0
        if headNode.nextNode is None: # Breaking Statement
            print("in if loop",headNode.data)
            return headNode
        newHeadNode1 = self.reverselinklist(headNode.nextNode)
        headNode.nextNode.nextNode = headNode
        headNode.nextNode = None
        return newHeadNode1

    def popanode(self):
        print(self.headNode.data," is being popped")
        self.headNode = self.headNode.nextNode
        print("New head node", self.headNode.data)

    def pushatindex(self,newNode,index):
        if newNode is None:
            return ValueError
        count = 0
        currNode = self.headNode
        while currNode is not None:
            if count == index:
                newNode.nextNode = currNode.nextNode
                currNode.nextNode = newNode
                return self.headNode
            currNode = currNode.nextNode
            count +=1
        print("Index greater than list")
        return self.headNode

    def sortedInsert(self,newNode):
        if newNode is None:
            return ValueError
        currNode = self.headNode
        if newNode.data <= self.headNode.data:
            newNode.nextNode =  self.headNode
            self.headNode = newNode
            return True
        else:
            while currNode.nextNode is not None:
                if currNode.data < newNode.data <= currNode.nextNode.data: # time to add Node
                    newNode.nextNode = currNode.nextNode
                    currNode.nextNode = newNode
                    return True
                else:
                    currNode = currNode.nextNode
            currNode.nextNode = newNode
            return True
    def flatalist(self):
        currNode = self.headNode
        while currNode is not None:
            print("hor",currNode.data)
            if currNode.downNode is not None:
                print("down",currNode.downNode.data)
                tempNode = currNode.downNode
                oldcurrNode = currNode
                currNode.downNode = None
                while currNode.nextNode is not None:
                    currNode = currNode.nextNode
                currNode.nextNode = tempNode
                currNode = oldcurrNode

            currNode = currNode.nextNode
    def makeacyclic(self):
        print("Creating cyclic")
        currNode = self.headNode
        tempNode = None
        while currNode.nextNode is not None:
            #if currNode.data == 33:
            #    tempNode = currNode
            currNode = currNode.nextNode
        #print(currNode.data)
        currNode.nextNode = self.headNode.nextNode.nextNode.nextNode

    def findcycleinalisthash(self):
        storage_hash = {}
        currNode = self.headNode
        cyclefound = False
        count = 0
        if currNode is None:
            return AttributeError("head node is none")
        while cyclefound or currNode.nextNode is not None:
            print("next val",currNode.data)
            if currNode in storage_hash:
                cyclefound = True
                print("Node",currNode.data)
                #print("cycle found at index", count , "and:-",listofpointers.index(currNode))
                print(storage_hash[currNode])
                return currNode
            else:
                print("adding this to hash",currNode.data)
                storage_hash[currNode] = currNode.data
            count = count+1
            currNode = currNode.nextNode
        print("length of list", count)
        if cyclefound == False:
            print("No cycle found")
        return None

    def findcycleinalistfastpointer(self):
        slowpointer = self.headNode
        fastpointer = self.headNode
        cyclefound = False
        while slowpointer and fastpointer and fastpointer.nextNode:
            slowpointer = slowpointer.nextNode
            fastpointer = fastpointer.nextNode.nextNod  e
            print("slow",slowpointer.data,fastpointer.data)
            if slowpointer == fastpointer:
                print("Cycle in the list 1",slowpointer.data,fastpointer.data)
                cyclefound = True
                break
                #return slowpointer.data

        if slowpointer == fastpointer:
            print("lets find the start")
            slowpointer = self.headNode
            while slowpointer!= fastpointer :
                print(slowpointer.data)
                slowpointer =slowpointer.nextNode
                fastpointer =fastpointer.nextNode

        print("Cycle in the list",fastpointer.data)
        #return None
        return slowpointer.data
    def findstartofcycle(self):
        if None == self.headNode or None == self.headNode.nextNode:
            return None
        slow = self.headNode.nextNode
        fast = slow.nextNode
        while slow != fast:
            print("first")
            slow = slow.nextNode
            try:
                fast = fast.nextNode.nextNode
            except AttributeError:
                return None
        slow = self.headNode
        while slow!= fast:
            print("second")
            slow = slow.nextNode
            fast = fast.nextNode

        return slow.data

#objLinkList = LinkList(15) ; objLinkList.addNode(16) ; objLinkList.addNode(24) ; objLinkList.addNode(38) ;objLinkList.addNode(37)
#objLinkList.addNode(56) ; objLinkList.addNode(57) ; objLinkList.addNode(58) ; objLinkList.addNode(59) ; objLinkList.addNode(60)
#objLinkList.addNode(39) ; objLinkList.addNode(40) ; objLinkList.addNode(42)

#objLinkList.printlinklist(objLinkList.headNode)

"""
objLinkList2 = LinkList(17)
objLinkList2.addNode(18)
objLinkList2.addNode(24)
objLinkList2.addNode(37)
objLinkList2.addNode(41)
objLinkList2.addNode(44)
objLinkList2.addNode(488)
objLinkList2.printlinklist(objLinkList2.headNode)

objLinkList3 = LinkList(35)
objLinkList3.addNode(40)
objLinkList3.addNode(41)
objLinkList3.addNode(42)
objLinkList3.addNode(67)
objLinkList3.addNode(89)
objLinkList3.addNode(889)
objLinkList3.printlinklist(objLinkList3.headNode)
"""
#objLinkList.printlinklist(objLinkList.headNode)
#newHeadNode = objLinkList.reverselinklist(objLinkList.headNode)
# print("-------------------------")
#print(newHeadNode.data)
#print(newHeadNode.data)
#objLinkList.printlinklist(newHeadNode)
#objLinkList.popanode()
#nodetoadd = LinkListNode(33)
#nodetoadd2 = LinkListNode(10)
#objLinkList.printlinklist(objLinkList.pushatindex(nodetoadd,2))
#print("----------")
# print(objLinkList.sortedInsert(nodetoadd2))
# objLinkList.printlinklist(objLinkList.headNode)
# objLinkList.headNode.nextNode.nextNode.downNode = LinkListNode(12)
# objLinkList.headNode.nextNode.nextNode.downNode.downNode = LinkListNode(13)
# objLinkList.headNode.nextNode.nextNode.downNode.downNode.downNode = LinkListNode(14)
# objLinkList.headNode.nextNode.nextNode.downNode.downNode.nextNode = LinkListNode(15)
# objLinkList.flatalist()
#print("--------2----------")
#objLinkList.printlinklist(objLinkList.headNode)
#objLinkList.makeacyclic()
#objLinkList.printlinklist(objLinkList.headNode)
#print("--------3----------")
#print(objLinkList.findcycleinalisthash())
#print("--------4----------")
#print(objLinkList.findcycleinalistfastpointer())
#print("--------4----------")
#print(objLinkList.findstartofcycle())