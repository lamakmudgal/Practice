from collections import deque
import heapq
# A Deque (Double ended queue) based
# method for printing maximum element
# of all subarrays of size k
def printMaxdeque(arr, n, k):
    """ Create a Double Ended Queue, Qi that
    will store indexes of array elements.
    The queue will store indexes of useful
    elements in every window and it will
    maintain decreasing order of values from
    front to rear in Qi, i.e., arr[Qi.front[]]
    to arr[Qi.rear()] are sorted in decreasing
    order"""
    Qi = deque()

    # Process first k (or first window) elements of array
    for i in range(k):

        # For every element, the previous smaller elements are useless
        # so remove them from Qi
        while Qi and arr[i] >= arr[Qi[-1]]:
            Qi.pop()

            # Add new element at rear of queue
        Qi.append(i)
        print(Qi)

        # Process rest of the elements, i.e.
    # from arr[k] to arr[n-1]
    for i in range(k, n):
        print(Qi)
        # The element at the front of the
        # queue is the largest element of
        # previous window, so print it
        print(str(arr[Qi[0]]) + " ", end="")

        # Remove the elements which are
        # out of this window
        while Qi and Qi[0] <= i - k:
            # remove from front of deque
            Qi.popleft()

            # Remove all elements smaller than
        # the currently being added element
        # (Remove useless elements)
        while Qi and arr[i] >= arr[Qi[-1]]:
            Qi.pop()

            # Add current element at the rear of Qi
        Qi.append(i)

        # Print the maximum element of last window
    print(str(arr[Qi[0]]))
def printmaxheap(arr,n,k):
    if n*k == 0:
        return
    i =0
    j = k-1
    mxheap = arr[i:j+1]
    heapq._heapify_max(mxheap)
    print(mxheap[0])
    last = arr[i]
    j = j+1
    i +=1
    new = arr[j]
    while j<n:
        print("heap",mxheap)
        mxheap[mxheap.index(last)] = new
        heapq._heapify_max(mxheap)
        print(mxheap[0])
        last = arr[i]
        i+=1
        j+=1
        if j<n:
            new = arr[j]

# Python3 implementation of the approach

# Function to print the maximum for
# every k size sub-array
def print_max(a, n, k):  #using Stack
    # max_upto array stores the index
    # upto which the maximum element is a[i]
    # i.e. max(a[i], a[i + 1], ... a[max_upto[i]]) = a[i]

    max_upto = [0 for i in range(n)]

    # Update max_upto array similar to
    # finding next greater element
    s = []
    s.append(0)

    for i in range(1, n):
        while (len(s) > 0 and a[s[-1]] < a[i]):
            max_upto[s[-1]] = i - 1
            del s[-1]

        s.append(i)
    print("max_upto:-",max_upto)
    while (len(s) > 0):
        max_upto[s[-1]] = n - 1
        del s[-1]

    j = 0
    for i in range(n - k + 1):

        # j < i is to check whether the
        # jth element is outside the window
        while (j < i or max_upto[j] < i + k - 1):
            j += 1
        print(a[j], end=" ")
    print()




# Driver programm to test above fumctions
if __name__ == "__main__":
    arr = [12, 1, 78, 90, 57, 89, 56]
    k = 3
    printMaxdeque(arr, len(arr), k)