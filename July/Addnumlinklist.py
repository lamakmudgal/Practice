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


