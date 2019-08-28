import heapq
# Definition for singly-linked list.
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
        while currNode is not None:
            print("Node :- ",currNode.data)
            currNode = currNode.nextNode



class Solution:
    def mergeKLists(self, lists,n):
        if not any(lists):
            raise ValueError("One of the list is empty")
        finallist = LinkList(0)
        heapmin = []
        heapq.heapify(heapmin)

        for headnodpos,items in enumerate(lists):
            #print("adf",type(items))
            if items is None:
                raise ValueError("headnode not found")
            heapq.heappush(heapmin, (items.data, headnodpos))
            #lists[i] = lists[i].nextNode
        #print(list(heapmin))

        for i in range(0,n):
            temptop = heapq.heappop(heapmin)
            temp = list(temptop)
            finallist.addNode(temp[0])
            finallist.printlinklist(finallist.headNode)
            #print("value from heap",temp[0])
            #print("value from heap",temp[1])
            #print("access the list", ite)
            if lists[temp[1]].nextNode is not None:
                #print("adssdfad",type(temp[1].nextNode))
                val = lists[temp[1]].nextNode.data
                print("val",val)
                nodes = temp[1]
                heapq.heappush(heapmin, (val,nodes))
                lists[temp[1]] = lists[temp[1]].nextNode
        return finallist

objsol = Solution()
linklist1 = LinkList(1)
linklist1.addNode(4)
linklist1.addNode(5)
linklist2 = LinkList(5)
linklist2.addNode(6)
linklist2.addNode(7)
linklist3 = LinkList(2)
linklist3.addNode(3)
linklist3.addNode(90)
#linklist1.printlinklist(linklist1.headNode)
#linklist2.printlinklist(linklist2.headNode)
#linklist3.printlinklist(linklist3.headNode)
inputdata = [linklist1.headNode,linklist2.headNode,linklist3.headNode]
newlist = objsol.mergeKLists(inputdata,9)
print("------------------------------------------")
newlist.printlinklist(newlist.headNode.nextNode)