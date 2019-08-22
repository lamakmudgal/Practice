from collections import deque
"""
def checksymbolbalace(inputstring):
    if inputstring == "":
        return True
    symbolstack = deque()
    balanced = True
    for chars in inputstring:
        #print(symbolstack)
        if chars in ["(", "[", "{"]:
            symbolstack.append(chars)
        if chars in [")","}","]"]:
            print(chars)
            if len(symbolstack) == 0:
                print("empty",len(symbolstack),symbolstack,chars)
                balanced = False
            elif not oppsymbol(chars,symbolstack.pop()):
                print("Non Matching")
                balanced = False
    if len(symbolstack) >0:
        balanced = False
    return balanced
def oppsymbol(char1,char2):
    #print(char1,char2)
    if char1 == ")" and char2 =="(":
        return True
    if char1 == "}" and char2 == "{":
        return True
    if char1 == "]" and char2 == "[":
        return True
    else:
        return False


inputstring = "((A+B)+(C-D))"
#print(checksymbolbalace(inputstring))
inputstring = "(A+B+(C-D)"
#print(checksymbolbalace(inputstring))
"""
class stackoperations:
    def __init__(self):
        self.minvalstack = []
        self.storagestack = []

    def createminvalstack(self,arr):
        if len(arr) < 1:
            return ValueError("empty input")

        for items in arr:
            if len(self.minvalstack) == 0:
                self.minvalstack.append(items)
            elif self.minvalstack[-1] >= items:
                self.minvalstack.append(items)

            self.storagestack.append(items)
    def getminval(self):
        print(self.minvalstack)
        print(self.storagestack)
        return self.minvalstack.pop()


objstack = stackoperations()
objstack.createminvalstack([50,15,1,22,1,6,18,9,6,5])
print(objstack.getminval())