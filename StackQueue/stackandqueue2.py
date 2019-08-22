# implement stack using queue
# STACK lifo queue fifo

class queue:
    def __init__(self):
        self.queue = []

    def isempty(self):
        return self.queue == []

    def enqueue(self,x):
        if x is not None:
            self.queue.append(x)
    def dequeu(self):
        if self.queue:
            a = self.queue[0]
            self.queue.remove(a)
            return a
        else:
            raise IndexError("queue is empty")
    def size(self):
        return len(self.queue)

class stack:
    def __init__(self):
        self.q1 = queue()
        self.q2 = queue()

    def push(self,data):
        if data is None:
            raise ValueError("Empty data to push")
        if self.q1.size() == 0:
            self.q2.enqueue(data)
        elif self.q2.size() == 0:
            self.q1.enqueue(data)

    def pop(self):
        if self.q1.size() == 0 and self.q2.size()==0:
            raise IndexError("Empty list")
        if self.q1.size() == 0:
            while self.q2.size() > 1 :
                self.q1.enqueue(self.q2.dequeu())
            return self.q2.dequeu()
        elif self.q2.size() == 0:
            while self.q1.size() > 1 :
                self.q2.enqueue(self.q1.dequeu())
            return self.q1.dequeu()

    def isempty(self):
        if self.q1.size() == 0 and self.q2.size()== 0:
            print("empty")
            return True
        else:
            print("not empty")
            return False




objstack  = stack()

objstack.push(5)
objstack.push(22)
objstack.push(33)
objstack.push(12)
objstack.push(7)
objstack.push(32)
objstack.push(0)
objstack.push(9)
#print(objstack.pop())
#print(objstack.pop())
objstack.push(33333)
#print(objstack.pop())
#print(objstack.pop())


