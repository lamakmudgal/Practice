class NewClass:
    def __init__(self,input):
        print("class1",input)

class anotherclass:
    def __init__(self,another):
        print("class2",another)
        self.head: NewClass= None
    def printhead(self):
        print(type(self.head))

obj1 =  anotherclass("kamal")
print(obj1.printhead)
obj2: NewClass = None
