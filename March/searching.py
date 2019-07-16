import sys

# find duplicates in array
def findduplcateinarray(arr): # nlogn solution logn for sorting.
    if len(arr) < 1:
        print("empty Array")
        return False

    try:
        arr.sort()
    except TypeError:
        print("Mismatch in type")
        return False
    except:
        print("Error in sorting the string")
        return False
    print(arr)
    for i in range(0,len(arr)-1):
        if arr[i] == arr[i+1]:
            return True

    return False
#arr = [1,3,4,2,17,4,7,14]

#print(findduplcateinarray(arr))
# find duplicates in array
# Use negate technique if the array only have positive fixed number in range 0 to n-1
# Approach if a[0] is 3 got to a[3] and make this negative. if the number is already negative it has been there before.
arr = [1,2,3,4,5,6,7,8,9,1]
def findduplicaten(a):
    print("find duplicate in n length array containing n numbers")
    for i in range (0,10):
        if a[a[i]-1]<0:
            print("repeated number is :-",a[i])
            break
        else:
            a[a[i]-1] = a[a[i]-1] * -1
    print(a)
#findduplicaten(arr)



# find the number which is repeated max num of times.
"""
def maxrepetitions(arr):
    n = len(arr)
    max = 0
    for i in range(0,len(arr)):
         arr[arr[i]%n] = n
    for i in range(0,len(arr)):
        if arr[i]/n > max:
            max = a[i]/n
            maxindex = i

    print(maxindex,max)

arr = [3,2,2,3,2,2,2,3,3]

maxrepetitions(arr)

# Python3 program to find first repeating
# element in arr[]



# This function prints the first repeating
# element in arr[]
def printFirstRepeating(arr, n):

# Initialize index of first repeating element
Min = -1

# Creates an empty hashset
myset = dict()

# Traverse the input array from right to left
for i in range(n – 1, -1, -1):

# If element is already in hash set,
# update Min
if arr[i] in myset.keys():
Min = i

else: # Else add element to hash set
myset[arr[i]] = 1

# Print the result
if (Min != -1):
print(“The first repeating element is”,
arr[Min])
else:
print(“There are no repeating elements”)

# Driver Code
arr = [10, 5, 3, 4, 3, 5, 6]

n = len(arr)
printFirstRepeating(arr, n)

# This code is contributed by Mohit kumar 29
"""
def oddnumoftimes(arr):
    result = 0
    for element in arr:
        result = result ^ element
    return result

arr = [1,1,1,1,1,1,3,3,3,3,3,3,5,5,5,5,5]

#print(oddnumoftimes(arr), " is repeated odd number of times")

def sumoftwoelement(a,sum):
    if len(a) < 2:
        print("Not enought elements")
        return False
    try:
        a.sort()
    except TypeError:
        print("Array does not contain only int")
        return False
    lowelement = 0
    highelement = len(a)-1
    found = False
    print(a)
    print(lowelement,highelement)
    while lowelement<highelement:
        if a[lowelement] + a[highelement] == sum:
            print("FOUND")
            found = True
            return [lowelement,highelement]
        elif a[lowelement] + a[highelement] > sum:
            highelement = highelement-1
        else:
            lowelement = lowelement+1
    return False

arr = [8,4,6,12,9,32,52,64,78]
#print(sumoftwoelement(arr,44))

def sumoftwoelementsquare(a):
    if len(a) < 3:
        print("Not enought elements")
        return False
    try:
        a.sort()
    except TypeError:
        print("Array does not contain only int")
        return False
    for i in range(0,len(a)):
        a[i] = a[i] * a[i]

    lowelement = 0
    highelement = len(a)-2
    sum = 0
    found = False
    print(a)

    for i in range(0,len(a)):
        sum = a[len(a) - 1-i]
        highelement =len(a)-2-i
        lowelement = 0
       #print(sum)
        while lowelement<highelement:
            print("l",a[lowelement],"h",a[highelement],"s",sum)
            if a[lowelement] + a[highelement] == sum:
                print("FOUND")
                found = True
                return [lowelement,highelement]

            elif a[lowelement] + a[highelement] > sum:
                highelement = highelement-1

            else:
                lowelement = lowelement+1

    return False

arr = [8,4,6,12,10,9,32,52,64,78]
print("---------------------------------")
#print(sumoftwoelementsquare(arr))

def sumclosestozero(a):
    if len(a)<2:
        return False

    a.sort()

    l = 0
    r = len(a)-1
    minsum = sys.maxsize
    minleft = 0
    minright = len(a)-1
    sum = 0

    while l<r:
        sum = a[l]+a[r]

        if sum < minsum:
            minsum = sum
            minleft = l
            minright = r
        elif sum > 0 :
            r=r-1
        else:
            l = l+1

    print("values are :", a[minleft],":",a[minright])

#arr = [-8,4,6,0,0,9,32,52,64,78]
print(sumclosestozero(arr))


def findelementinrotatedarraybyrecurrsion(a,k):
    if len(a) < 2:
        return -1
    left = 0
    right = len(a)-1
    target = k
    return findelemerecurrsion(a,left,right,target)

def  findelemerecurrsion(a,left,right,target):
    print(a[left:right+1],"vals:-",left,right,target)
    # base condition:
    if left > right:
        return -1

    mid = (left+right)//2
    print("mid is :-",mid)
    if a[mid] == target:
        return mid

    if a[mid] < a[right]: # right part of the array is still in sorted order
        print("1:--")
        if a[mid] < target <= a [right]:
            return findelemerecurrsion(a,mid+1,right,target) # element should be in right
        return findelemerecurrsion(a,left,mid-1,target) # element should be in left

    elif a[mid] > a [right]:
        print("2:--")
        if target>a[mid] or target<=a[right]:
            return findelemerecurrsion(a, mid + 1, right, target)  # element should be in right
        return findelemerecurrsion(a, left, mid - 1, target)  # element should be in left

    else: # in case a[mid] == a[left] or a[mid] == a[right] this is case of repeating element in array
            # because of returning there can be exception on biotonic.
        if a[mid] != a[right]:
            return findelemerecurrsion(a, mid + 1, right, target)
        result = findelemerecurrsion(a, left,mid-1, target)
        if result!= -1:
            return result
        return findelemerecurrsion(a, mid + 1, right, target)
print("------------------------")
a = [18,19,22,24,1,2,3,4,5,6,7,8,9,10]
#print("target found at location: ", findelementinrotatedarraybyrecurrsion(a,24))


def findfirstoccurance(a,element): # function to find first occurrence of a repeating element.
    if a == None or len(a)<1:
        return -1
    high = len(a)-1
    low = 0
    mid =0

    lastfound = -1
    while(1):
        if low>high:
            return lastfound
        mid = (low+high)//2
        if a[mid] == element:
            lastfound = mid
            high = mid -1
        if a[mid] < element : low = mid+1
        if a[mid] > element : high = mid-1
    return mid
a = [1,2,3,4,5,6,7,8,9,9,9]
print("find first occurance")
print(findfirstoccurance(a,9))
def maxrepeat(a):
    repeatcount = 0
    majelement = 0
    for i in range(0,len(a)-1):
        if repeatcount == 0:
            majelement = a[i]
            repeatcount = repeatcount +1
        elif a[i] == majelement:
            repeatcount = repeatcount +1
        else:
            repeatcount = repeatcount -1
    print(repeatcount,majelement)
a = [1,2,3,4,4,4,4,4,4,4,4,4,4,4,4,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,7,6,8,4,5,6,2,2,2]
print("--------------max repeat----------------")
#maxrepeat(a)

def findelementin2d(arr,target):
    if len(arr) <1:
        return False
    row = 0
    column  = len(arr)-1
    print("1. lenth arr",len(arr))
    print("2. lenth arr",len(arr[0]))


    while 0 <= column < len(arr) and 0<= row < len(arr):
        print(row,column)
        print("scanning:", arr[row][column])
        if target == arr[row][column]:
            return True
        if target < arr[row][column]:
            column =column-1
        elif target > arr[row][column]:
            row=row+1
    return "Not found"

twodarray = [[10,20,30,40,50],
             [11,23,32,42,52],
             [19,25,34,44,58],
             [22,28,39,48,59],
             [24,35,45,49,71],]
print("--------------tow d array---------------")
print("printing:-",findelementin2d(twodarray,71))

def separateevenodd(a):
    if len(a) < 1:
        return -1
    i = 0
    j = len(a)-1
    print(i,j)
    while i<j:
        print(i,j)
        while a[i]%2 == 0 and i < j :
            i = i + 1
        while a[j]%2 ==1 and i<j:
            j = j -1
        if i < j :
            a[i],a[j] = a[j],a[i]
            i = i +1
            j = j - 1
    print(a)

arr = [1,2,3,4,5,6,7,8,9,10,11,12,13]
arr = [1,0,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1]
print("-----------separate odd an even -------------")
separateevenodd(arr)

def dutchflagproblem(arr):
    zero = 0
    two = len(arr)-1
    cur = 0
    while cur < two:
        if arr[cur] == 0:
            if cur > zero:
                arr[cur],arr[zero] = arr[zero],arr[cur]
                zero = zero+1
            else:
                cur = cur+1
                zero = zero+1
        elif arr[cur] == 2:
            if cur< two:
                arr[cur], arr[two] = arr[two], arr[cur]
                two =two-1
            else:
                break
        else:
            cur = cur+1
    print(arr)
arr = [1,1,0,0,0,0,2,2,2,2,1,1]
print("-------------------------------")
dutchflagproblem(arr)

def spanwithstack(prices):
    if len(arr) <=0:
        return -1

    span = [0]*len(prices)
    stack = []
    stack.append(0)
    span[0] = 1

    for i in range (1,len(prices)):
        while len(stack)>0 and prices[stack[-1]] <= prices[i]:
            stack.pop()
        if len(stack) <= 0:
            span[i] = i + 1
        else:
            val = stack[-1]
            span[i] = i - val
        stack.append(i)
    print(span)
def spanwithoutstack(prices):  # ASK PRAMOD
    span = [0]*(len(prices))
    span[0]  = 1

    for i in range(0,len(prices)):
        counter =1
        while ((i - counter) >= 0 and prices[i] > prices[i - counter]):
            counter = counter + span[i - counter];
        span[i] = counter;
    print(span)

prices = [10,4,5,90,120,80]
print("---------span----------")
#spanwithstack(prices)
print("---------span second----------")
#spanwithoutstack(prices)

def rearrange(n):
    global arr

    # if size is null or
    # odd return because
    # it is not possible
    # to rearrange
    if (n % 2 == 1):
        return

    # start from the
    # middle index
    currIdx = int((n - 1) / 2)

    # each time we will set
    # two elements from the
    # start to the valid
    # position by swapping
    while (currIdx > 0):

        count = currIdx
        swapIdx = currIdx
        print("count",count)
        while (count > 0):
            arr[swapIdx] , arr[swapIdx + 1] = arr[swapIdx + 1] , arr[swapIdx]
            swapIdx = swapIdx + 1
            count = count - 1
            print("arr:-",arr)
        currIdx = currIdx - 1

def rearracngerecurhelp(arr):
    if len(arr)<2:
        return 0
    rearracngerecur(arr,0,len(arr))
def rearracngerecur(arr,f,l):
    if l-f==1:
        return
    mid = (f+l)//2

    pass
# Driver Code
arr = ['a1', 'a2', 'a3', 'a4' , 'b1', 'b2', 'b3', 'b4']
n = len(arr)
print("--------------------------")
rearrange(n)
print("--------------------------")
for i in range(0, n):
    print("{} ".format(arr[i]), end="")