import timeit
def something(x,y):
    if x == 0:
        return y
    else:
        return something(x-1,y+x)

print(something(5,4))


def log2n(n):
    if n == 1:
        return 0
    else:
        return 1+ log2n(n//2)

print(log2n(20))

def convertintorbin(n):
    if n ==0:
        return
    convertintorbin(n//2)
    print(n%2,end="")

convertintorbin(21)
print("pyramid")
def printstarpyramid(n):
    i = 0
    if n >1:
        printstarpyramid(n-1)
    for i in range (0,n):
        print("*",end=" ")
    print("")
printstarpyramid(10)

def printrecursive(n):
    if n>0:
        printrecursive(n-1)
        print(n,end=",")
        printrecursive(n-1)

printrecursive(4)
print("")
print("-----------------------")
def findmaxinarr(arr,n):
    if n == 1:
        return arr[0]
    currmax = findmaxinarr(arr,n-1)
    if currmax>arr[n-1]:
        return currmax
    else:
        return arr[n-1]

arr = [-11,-2,-3,-4,-5]
arrlen = len(arr)
print(findmaxinarr(arr,arrlen))
print("-------------------------------------------------")
def multtwo(a,b):
    print("a",a,"b",b)
    if b ==0: return 0
    if b%2 == 0: return multtwo(a+a,b//2)
    return multtwo(a+a,b//2)+a
print(multtwo(2,5))
print("-------------------")

def power(a,b):
    return 1 if b == 0 else power(a,b-1)*a
print(power(2,5))
print("-------------------------------------------------------")
def countthree(count):
    print(count)
    if count<3:
        countthree(countthree(countthree(count+1)))
    return count
countthree(1)
print("------------------------------------------------")
def fun(n):
    if n<=1:
        return 1
    if n%2 == 0 :
        return fun(n//2)
    return fun(n//2) + fun((n//2)+1)
print(fun(11))