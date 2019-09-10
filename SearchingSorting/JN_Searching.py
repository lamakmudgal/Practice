#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Seaching Chapter 
# Problem 1 ,2,3:
# Find duplicate elements in Array 
# Approach:  Hashing, Brute force
def find_duplicate(arr):
    len_arr = len(arr)
    if len_arr<2:
        return
    arr.sort()
    for i in range(0,len_arr-1):
        if arr[i] == arr[i+1]:
            return True
    return False


arr = [5, 4, 3, 6, 6, 78, 9, 0, 22, 33, 44, 55, 44]
arr1 = [44,33,22,11,55,66,77,88,99]
print(find_duplicate(arr))
print(find_duplicate(arr1))


# In[ ]:


# Searching Chapter 
# Problem 4
# Find duplicate in array in o(n) if the element of array are in between 1 to n-1
def find_duplicated_negate(arr):
    if len(arr)<2:
        return
    for i in range (0,len(arr)):
        print(arr,i)
        if arr[abs(arr[i])]< 0:
            print(arr,i)
            return True
        else:
            arr[arr[i]] = -arr[arr[i]] 
    return False
arr = [3,2,1,4,5,0]
print(find_duplicated_negate(arr))


# In[ ]:


# Searching chapter problem 5 ,6,7,8
# find an element which appers maximum number of times
# Approach:
    # Hashing or Counting sort Time o(n) and spce o(n)
    # Brute Force two loops and counter. o(n2) and o(1)
    # sort and count
    # Restrictive set. Add array length and divide
def find_frequency(arr):
    if len(arr)<2:
        return
    for i in range(0,len(arr)):
        val = arr[i]%len(arr)
        arr[val] = arr[val]+len(arr)
    print(arr)
    maxcount = 0
    pos = 0
    for i in range(0,len(arr)):
        if arr[i]//len(arr) > maxcount:
            maxcount = arr[i]//len(arr)
            pos = i
    print(maxcount,pos)
    
arr = [3,2,2,3,2,2,2,3,3,2]
find_frequency(arr)
    


# In[ ]:


# Searching problem question 9,10,11
# first repeating number 3,2,1,2,2,3 the ans in this input is 3 though 2 has been repeated by three is the first
# 
def findfirstrepetition(arr):
    if len(arr)<2:
        return
    dict_repeat = {}
    minval =len(arr)
    for i in range(len(arr)-1,-1,-1):
        if arr[i] in dict_repeat:
            minval = i
            print(minval)
        else: 
            #print(arr[i])
            dict_repeat[arr[i]] = 1
    print("result",arr[minval])
arr = [4,5,3,2,1,2,1,2,3]
findfirstrepetition(arr)           


# In[ ]:


# Problem 13,14,15,16,17
# Find the missing number
# Approch
# Brute force , (N*N=1)/2 Summation technique , Hashing, sort and loop.
# In case very large integer values the summation technique will go out of range so XOR
def findmissingnum_XOR(arr):
    if len(arr)<1:
        return
    x1= arr[0]
    for i in range(1,len(arr)):
        x1= x1^arr[i]
        print("x1",x1)
    x2 = 1
    for i in range(2,len(arr)+2):
        x2 = x2^i
        print("x2",x2)
    
    return x1^x2

arr = [1,3,4,2,7,5]
print(findmissingnum_XOR(arr))


# In[ ]:


# problem 18,19,20,21
# find number repeating odd number of times

def oddrepeat(arr):
    if len(arr)<1:
        return
    result = arr[0]
    for i in range(1,len(arr)):
        result = result ^ arr[i]
    
    return result
arr = [1,2,3,4,5]
print(oddrepeat(arr))      


# In[ ]:


# Problem 22 and 24 To be dicussed with promod.


# In[ ]:


# problem 23
# find sum and multiplication and solve quadratic equation. 
# problem over flow


# In[ ]:


# Problem 25 ,26,27,28
def find_sum(arr,k):
    if len(arr)<2:
        print("return")
        return
    arr.sort()
    start = 0
    end = len(arr)-1
    k1 = 0
    while start<end: #or k1==10:
        print(start,end,"values")
        sum1 = arr[start] + arr[end]
        if sum1 == k :
            print("result",arr[start],arr[end])
            return True
        elif sum1<k:
            start +=1
        elif sum1>k:
            end -=1
        #k1 +=1
arr = [1,4,45,6,10,-8]        
print(find_sum(arr,11))


# In[ ]:


# Problem 29
# a2+b2=c2
def findsquaresum(arr):
    for i in range(0,len(arr)):
        arr[i] = arr[i]*arr[i]
    print(arr)
    for i in range(len(arr)-1,-1,-1):
        print(arr[:i],arr[i])
        if find_sum(arr[:i], arr[i]) == True:
            return True
arr = [1,2,3,4,5]
findsquaresum(arr)


# In[ ]:


# Problem 30,31,36 Nearest to zero
#import sys 
def close_zero(arr):
    if len(arr)<2:
        return
    arr.sort()
    minsum = float("inf")
    left = arr[0]
    right = arr[-1]
    l = 0
    r = len(arr)-1
    while l<r:
        curr_sum = arr[l] + arr [r]
        if abs(curr_sum) < abs (minsum):
            minsum = curr_sum
            left = arr[l]
            right= arr[r]
        if curr_sum>0:
            r -= 1
        else:
            l+=1
    print("result:", minsum,left,right)
arr = [1,60,10,-9,70,-80,85,-2,2]
print(close_zero(arr))


# In[ ]:


# Question 32 ,33,34,35 A+B+C = k
# Extention to problem 25. So we can call the function we created in question 25. 
def find_sum(arr,k):
    if len(arr)<2:
        print("return")
        return
    arr.sort()
    start = 0
    end = len(arr)-1
    k1 = 0
    while start<end: #or k1==10:
        print(start,end,"values")
        sum1 = arr[start] + arr[end]
        if sum1 == k :
            print("result",arr[start],arr[end])
            return True
        elif sum1<k:
            start +=1
        elif sum1>k:
            end -=1
        #k1 +=1
def threenumsum(arr,k):
    arr.sort()
    for i in range(0,len(arr)-2):
        if find_sum(arr[i+1:],k-arr[i]) is True:
            return True
    return False
arr = [1,6,45,4,10,18]
threenumsum(arr,320)

