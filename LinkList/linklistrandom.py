class LinkListNode:
    def __init__(self,data):
        self.data = data
        self.nextNode = None
        self.random = None

class LinkList(LinkListNode):
    def __init__(self,data):
        self.headNode = LinkListNode(data)

    def addNode(self,data):
        currNode = self.headNode
        while currNode.nextNode is not None:
            currNode = currNode.nextNode
        newNode = LinkListNode(data)
        currNode.nextNode = newNode

    def printlist(self):
        currNode = self.headNode
        while currNode.nextNode is not None:
            print(currNode.data,end="->")
            if currNode.random is not None:
                print("->","[",currNode.random.data,"]")
            currNode = currNode.nextNode
    def printlistnorand(self):
        currNode = self.headNode
        while currNode.nextNode is not None:
            print(currNode.data,end="->")
            currNode = currNode.nextNode
    def assignrand(self):
        currNode = self.headNode
        while currNode.nextNode is not None:
            if currNode.nextNode.nextNode is not None:
                currNode.random = currNode.nextNode.nextNode
            currNode = currNode.nextNode

    def copylist(self):
        org_head = self.headNode
        curr = org_head
        while curr.nextNode is not None:
            newNode =LinkListNode(curr.data)
            newNode.nextNode = curr.nextNode
            curr.nextNode = newNode
            if curr.nextNode.nextNode is not None:
                curr = curr.nextNode.nextNode
        self.printlistnorand()
        curr = org_head
        while curr.nextNode is not None and curr.random is not None:
            curr.nextNode.random = curr.random.nextNode
            curr = curr.nextNode.nextNode
        curr = org_head
        newhead = org_head.nextNode
        newhead.data = 123
        while curr.nextNode is not None:
            tmp = curr.nextNode
            if curr.nextNode.nextNode is not None:
                curr.nextNode = curr.nextNode.nextNode
            curr = tmp
        self.headNode = newhead
        print("newlist")
        self.printlist()
        return newhead

objLinkList = LinkList(1)
arr = [2,3,4,5,6,7,8]
for item in arr:
    objLinkList.addNode(item)
objLinkList.assignrand()
#objLinkList.printlist()
objLinkList.copylist()