class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkList(Node):
    def __init__(self,data):
        self.root = Node(data)

    def getlength(self,rootnode):
        count = 0
        while rootnode is not None:
            count+=1
            rootnode = rootnode.next
        return count


    def addlinklist(self,root1,root2,sumroot):
        count1 = self.getlength(root1)
        count2 = self.getlength(root2)

        val = self.addtwonum(root1,root2,sumroot)
        if val == 1: # carry over need to add one more node in front of list
            newHeadnode = Node(val)
            newHeadnode.next = sumroot
            return newHeadnode
        else:
            return sumroot




    def addtwonum(self,root1,root2,sumroot):
        print("add two num called")

        if root1 is None or root2 is None:
            print("base case")
            return 0

        if root1.next is not None or root2.next is not None:
            newNode = Node(0)
            sumroot.next = newNode

        sumval = root1.data + root2.data + self.addtwonum(root1.next,root2.next,sumroot.next)

        if sumval >=10:
            sumroot.data = sumval%10
            return 1
        else:
            sumroot.data = sumval
            return 0

    def printlinklist(self,root):
        while root is not None:
            print(root.data,end=",")
            root = root.next
    # opposite order
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None and l2 is None:
            return
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        carryover = 0
        l3 = l1
        res = l3
        while l1 is not None and l2 is not None:
            tempsum = l1.val + l2.val + carryover

            if tempsum >= 10:
                carryover = 1
                l3.val = tempsum % 10
            else:
                carryover = 0
                l3.val = tempsum
            l1 = l1.next
            l2 = l2.next
            if l1 is not None or l2 is not None or carryover == 1:
                l3.next = ListNode(0)
                l3 = l3.next
        if l1 is not None:
            print("l1 is not none")
            if carryover != 1:
                print("ji", l1.val)
                l3.val = l1.val
            else:
                print("in else")
                while l1 is not None:
                    tempsum = l1.val + carryover
                    if tempsum >= 10:
                        carryover = 1
                        l3.val = tempsum % 10
                    else:
                        carryover = 0
                        l3.val = tempsum
                    l1 = l1.next
                    if l1 is not None or carryover == 1:
                        l3.next = ListNode(0)
                        l3 = l3.next
                print("carryover", carryover, l3.val)
                if carryover != 1:
                    l3.val = 1  # as carryover was one and l2 ended

        if l2 is not None:
            print("l2 is not none")
            if carryover != 1:
                l3.val = l2.val
            else:
                while l2 is not None:
                    tempsum = l2.val + carryover
                    if tempsum >= 10:
                        carryover = 1
                        l3.val = tempsum % 10
                    else:
                        carryover = 0
                        l3.val = tempsum
                    l2 = l2.next
                    if l2 is not None or carryover == 1:
                        l3.next = ListNode(0)
                        l3 = l3.next
                if carryover != 1:
                    l3.val = 1  # as carryover was one and l2 ended
        if carryover != 0:
            l3.val = 1

        return res

root1 = LinkList(5)
#print(root1.data)
node = Node(2)
root1.root.next = node
print(root1.root.next.data)
node = Node(3)
root1.root.next.next = node
root2 = LinkList(8)
node = Node(1)
root2.root.next = node
node = Node(8)
root2.root.next.next = node
sumroot = LinkList(0)
obj = LinkList(0)
sumroot.root = obj.addlinklist(root1.root,root2.root,sumroot.root)
obj.printlinklist(sumroot.root)


