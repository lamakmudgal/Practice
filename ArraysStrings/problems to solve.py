# 1. Adding one to number represented as array of digits
def addonetoarray(arr):
    n = len(arr)

    # Find carry:
    lastdigit = arr[-1]
    lastdigit = lastdigit +1
    carry = lastdigit//10
    arr[-1] = lastdigit%10

    for i in range (n-2,0,-1):
        if carry ==1:
            val = arr[i] + 1
            carry = val//10
            arr[i] = arr[i]%10


    if carry == 1:
        arr.insert(0,1)
    print(arr)

arr = [9,9,9,8]
#addonetoarray(arr)

def watertrap(arr):
    waterunit = 0
    n = len(arr)

    leftarr = [0]*n
    rightarr = [0] * n
    leftarr[0] = arr[0]
    for i in range (1,len(leftarr)):
        leftarr[i] = max(leftarr[i-1],arr[i])

    print(leftarr)
    rightarr[-1] = arr[-1]
    for i in range (n-2,-1,-1):
        rightarr[i] = max(rightarr[i+1],arr[i])

    print(rightarr)

    for i in range (0,n-1):
        waterunit = waterunit + min (leftarr[i],rightarr[i])-arr[i]

    print(waterunit)


arr = [0,1,0,2,1,0,1,3,2,1,2,1]
#watertrap(arr)


def findWater(arr, n):
    # initialize output
    result = 0

    # maximum element on left and right
    left_max = 0
    right_max = 0

    # indices to traverse the array
    lo = 0
    hi = n - 1

    while (lo <= hi):
        print(result)

        if (arr[lo] < arr[hi]):

            if (arr[lo] > left_max):

                # update max in left
                left_max = arr[lo]
            else:

                # water on curr element = max - curr
                result += left_max - arr[lo]
            lo += 1

        else:

            if (arr[hi] > right_max):
                # update right maximum
                right_max = arr[hi]
            else:
                result += right_max - arr[hi]
            hi -= 1

    return result


# Driver program

arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
n = len(arr)

#print("Maximum water that can be accumulated is ", findWater(arr, n))
"""
4.	Given a string, find the length of the longest substring T that contains at most k distinct characters.
Example 1:
Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.
"""

def findlongestsubstring(string, k):
    for i in range(0,len(string)-(k-1)):
        temp = set(string[i:i+k])
        print(temp)
        if len(temp) < k:
            j = 0
            print(string[i + k])
            while len(temp)<k and i+k+j < len(string):
                temp.add(string[i+k+j])
                print(temp)
                j = j +1
            print(len(temp),i,i+k+j-1)

findlongestsubstring("kamallamal",3)


