# Implement queue using stacks:
# Queue FIFO Stack LIFO

class queueusingstack:
    def __init__ (self):
        self.insertstack = []
        self.getstack = []

    def insertdata(self, itemtoinsert):
        if itemtoinsert is not None:
            self.insertstack.append(itemtoinsert)

    def getdata(self):
        if len(self.getstack)==0 and len(self.insertstack) == 0:
            return False
        if len(self.getstack)==0 and len(self.insertstack) > 0:
            while len(self.insertstack)>0:
                self.getstack.append(self.insertstack.pop())
        return self.getstack.pop()

objqtostack = queueusingstack()
print(objqtostack.getdata())
objqtostack.insertdata(5)
objqtostack.insertdata(12)
objqtostack.insertdata(23)
objqtostack.insertdata(54)
objqtostack.insertdata(35)
objqtostack.insertdata(1)
objqtostack.insertdata(500)
print(objqtostack.getdata())
objqtostack.insertdata(34)
print(objqtostack.getdata())
print(objqtostack.getdata())
objqtostack.insertdata(37)
print(objqtostack.getdata())
print(objqtostack.getdata())
print(objqtostack.getdata())
print(objqtostack.getdata())
print(objqtostack.getdata())
print(objqtostack.getdata())
print(objqtostack.getdata())
