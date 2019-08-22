def reverseastack(stack1):
    if len(stack1)<1:
        return None
    return reverseastackhelper(stack1)

def reverseastackhelper(stack1):
    if len(stack1)<1:
        print("stack1 is empty")
        return None
    k = stack1.pop()
    print("k", k)
    reverseastackhelper(stack1)
    insertatbottom(stack1, k)
    return stack1

def insertatbottom(stack, item):
    if len(stack)<1:
        stack.append(item)
    else:
        temp = stack.pop()
        print("temp",temp)
        insertatbottom(stack,temp)
        stack.append(temp)

def reversestack2(stack1):
    def reversestack2help(stack1,tempstack=[]):
        if len(stack1)>0:
            tempstack.append(stack1.pop())
            reversestack2help(stack1,tempstack)
        return tempstack
    return reversestack2help(stack1)


stack1 = [1,2,3,4,5]
#print(reverseastack(stack1))
#print(stack1)

def findspan(arr):
    n = len(arr)-1
    span = [1]*(n+1)
    for k in range(n,-1,-1):
        spanval = 1
        j = k-1
        while j>=0:
            print("k",k,"j",j)
            if arr[k]>=arr[j]:
                spanval = spanval +1
                j = j-1
            else:
                span[k] = spanval
                print(span)
                break
    print(span)
def findspanfrombegin(arr):
    span = [None]*len(arr)

    for i in range(0,len(arr)):
        j = 1

        while j <=i and arr[i] > arr[i-j]:
            j = j +1
        span[i] = j
    print(span)


def calculateSpan(price, S):
    n = len(price)
    # Create a stack and push index of fist element to it
    st = []
    st.append(0)

    # Span value of first element is always 1
    S[0] = 1

    # Calculate span values for rest of the elements
    for i in range(1, n):
        # Pop elements from stack whlie stack is not
        # empty and top of stack is smaller than price[i]
        while (len(st) > 0 and price[st[-1]] <= price[i]):
            st.pop()

        # If stack becomes empty, then price[i] is greater
        # than all elements on left of it, i.e. price[0],
        # price[1], ..price[i-1]. Else the price[i] is
        # greater than elements after top of stack

        if len(st) <= 0:
            S[i] = i + 1
        else:
            S[i] = (i - st[-1])
        # Push this element to stack
        st.append(i)

def replacewithnextmax(arr):
    maxval = arr[-1]
    n = len(arr)
    #newarr= [None]*n
    arr[n-1] = -1
    for i in range(n-2,-1,-1):
        temp = arr[i]
        arr[i] = maxval
        if temp > maxval:
            maxval = temp
            print("new max val is:- ",maxval)

    print(arr)


arr = [6,3,4,5,2]
span = [None]*5
#calculateSpan(arr,span)
#print(span)
arr = [16,17,4,3,5,2]
replacewithnextmax(arr)
