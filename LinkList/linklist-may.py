from Practice.LinkList.linklist import LinkList

import heapq

def nsortedarray():

    objLinkList1 = LinkList(15); objLinkList1.addNode(16); objLinkList1.addNode(24)
    objLinkList2 = LinkList(14); objLinkList2.addNode(22);objLinkList2.addNode(37)
    objLinkList3 =LinkList(18); objLinkList3.addNode(56); objLinkList3.addNode(57); objLinkList3.addNode(58)
    listarr = [objLinkList1,objLinkList2,objLinkList3]
    listheap = []
    heapq.heapify(listheap)
    for i in range(len(listarr)):
        heapq.heappush(listheap,(listarr[i].headNode.data,listarr[i]))

    firstelement = listheap.pop()
    newHeadNode = LinkList(firstelement[0])
    if firstelement[1].nextNode is not None:
        listheap.push(firstelement[1].nextNode.data,firstelement[1].nextNode)

    while len(listheap) > 0:
        newelement = listheap.pop()
        newHeadNode.addNode(newelement[0])
        if newelement[1].nextNode is not None:
            listheap.push(newelement[1].nextNode.data,newelement[1].nextNode)

    objLinkList1.printlinklist(objLinkList1.headNode)
    objLinkList2.printlinklist(objLinkList2.headNode)
    objLinkList3.printlinklist(objLinkList3.headNode)
    newHeadNode.printlinklist(newHeadNode.headNode)


nsortedarray()