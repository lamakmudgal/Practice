#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def findrepeatingchars(strk):
    l = []
    temp = []

    for i in range(0, len(strk)):
        if strk[i] in l:
            temp.append(strk[i])
        else:
            l.append(strk[i])
    return temp
    
strk="kamal"
findrepeatingchars(strk)


# In[ ]:





# In[ ]:


def partition(arr,start,end,pivot):
    curr = start
    ge_pivot = start
    print(end)
    # Move the pivot ot end
    arr[pivot],arr[end] = arr[end],arr[pivot]
    for curr in range (start,end):
        if arr[curr]<= arr[end]: # Less than equal to pivot
            #swap
            arr[curr], arr[ge_pivot] = arr [ge_pivot] , arr[curr]
            ge_pivot +=1
    arr[end] , arr[ge_pivot] = arr[ge_pivot] , arr[end]
    return arr
arr = [8,12,6,19,11,8,12,3,2]
print(partition(arr,0,len(arr)-1,3))


# In[ ]:


def mergesort(arr,start,end):
    if start>= end:
        return
    mid = start + end//2
    print("mid",mid)
    mergesort(arr,start,mid)
    mergesort(arr,mid+1,end)
    merge(arr,start,mid,end)
    return arr
def merge(arr,start,mid,end):
    left = mid-start+1
    right = end-mid
    leftarr = arr[start:mid]
    
    rightarr = arr[mid:end]
    print("Left array is :",leftarr,"Right Arr is :", rightarr)
    i , j, k = 0,0,0
    while i == left or j ==right :
        if leftarr[i] <= rightarr[k]:
            arr[k] = leftarr[i]
            k += 1
            i += 1
        else: 
            arr[k] = rightarr[j]
            k +=1
            j+=1
        ad
    if i<left:
        arr = arr+leftarr[i:]
    if j<right:
        arr = arr+rightarr[j:] 
    print("Merged arr is ",arr)
        

arr = [2,3,15,20,5,6,12,25]
#print(mergesort(arr,0,8))


# In[ ]:


arr = [2,3,15,20,5,6,12,25]
print(arr[0:4])
print(arr[4:8])


# In[ ]:


import random
def countingsort(A,k):
    B = [0 for item in A]
    C = [0 for item in range(k+1)]
    print(C)
    for i in range(0,k+1):
        C[i] = 0 
    for j in range(0,len(A)):
        C[A[j]]+=1
        print(C)
    for i in range(1,k+1):
        C[i] += C[i-1]
        print("new",C)
    for j in range(len(A)-1,0-1,-1):
        tmp = A[j]
        tmp2 = C[tmp]-1
        B[tmp2] = tmp
        C[tmp]-=1
        print("B:",B)
        print("C:",C)
    return B

arr = [2,3,6,1]
countingsort(arr,7)


# In[ ]:


# given an arr arr[0...n-1] of na numbers find any repetitive numbers. No extra space. 
def findrepetition(arr): # Problem with 0
    if len(arr)<1:
        return None
    if len(arr)<2:
        return "No repetition"
    
    for i in range(0,len(arr)):
        if arr[abs(arr[i])]<0:
            return "Repetition"
        else:
            arr[arr[i]] =  arr[arr[i]]*(-1)
            print(arr)
arr = [0,1,0,3]    
print(findrepetition(arr))


# In[ ]:


# given an arr arr[0...n-1] of na numbers find any repetitive numbers. No extra space. 
def findrepetition(arr): # Problem with 0
    arr.sort()
    for i in range(0,len(arr)-1):
        if arr[i] == arr[i+1]:
            return "repeat"
    return "No Repeat"
arr = [33,2,10,20,22,32]    
print(findrepetition(arr))


# In[ ]:


def partition(arr,start,end):
    med = start+end//2
    print(med)
    arr[med],arr[end-1] = arr[end-1],arr[med]
    for i in range(start,end-2):
       # print(arr[end-2])
        if arr[i] <= arr[end-1]:
            arr[i],arr[start] =arr[start], arr[i]
            start +=1
    arr[end-1],arr[start] = arr[start],arr[end-1]
    print(arr,start)
    return arr
arr = [3,12,23,1,2,2,0,24,200,400,20]
print(partition(arr,0,11))


# In[ ]:


def bubblesort(arr):
    swapdone = True
    while swapdone == True:
        swapdone = False
        for i in range(0,len(arr)-1):
            if arr[i]>arr[i+1]:
                #print("B$ Swap",arr[i],arr[i+1])
                arr[i],arr[i+1] = arr[i+1],arr[i]
                print("Swap done",arr[i],arr[i+1])
                #print(arr)
                swapdone = True
    return arr

print(bubblesort([4,1,1,1]))


# In[ ]:


def selectionsort(arr):
    for i in range(0,len(arr)):
        min = arr[i]
        for j in range(i,len(arr)):
            if min > arr[j]:
                min,arr[j] = arr[j] , min
        min,arr[i] = arr[i],min
        print(arr)
    return arr

print(selectionsort([5,8,2,3,1,9]))


# In[ ]:


def insertionsort(arr):
    if len(arr)<2:
        return
    
    for i in range(1,len(arr)):
        k = i
        temp = arr[i]
        for j in range(k,-1,-1):
            if arr[j] > temp:
               # print(arr[j],temp)
                arr[j] , arr[j+1] = arr[j+1],arr[j]
               # print(arr[j],temp)
        print(arr)

        
print(insertionsort([8,8,8,8,5,1,4,3,2]))


# In[ ]:


# Sorting Chapter problem 1 and 2 Page 306:
def checkduplicates(arr): # with sorting so o(nlogn) + o(n) = nlogn
    arr.sort()
    for i in range(0,len(arr)-1):
        if arr[i] == arr[i+1]:
            return True
    return False
arr = [1,4,5,3,2,0,9]
print(checkduplicates(arr))
# other ways of doing it:
# Hash without sort but storage is needed.
# Counting arr if the input is from a limited number of integers like 1-n etc. Restricted data set.

def checkduplicates_hash(arr):
    dictofvalues = {}
    for item in arr:
        if item in dictofvalues:
            return True
        else:
            dictofvalues[item] = 1
    print(dictofvalues)
    return False
    
print(checkduplicates_hash(arr))


# In[ ]:


# sorting problem 3 and 4 and 5 Counting votes:
# Solution 1: Use dict like problem2
# sort and count with for loop.

def countvote(arr):
    arr.sort()
    maxvote = winner = candidate = 0
    votes = 1
    for i in range(1,len(arr)):
        
        if arr[i] == arr [i-1]:
            candidate = arr[i]
            votes +=1
        else:
            if votes > maxvote:
                   maxvote = votes
                   winner = candidate
            votes = 1
    print("winner is with votes",winner,maxvote)
arr = [2,3,4,5,6,2,7,8,8,8,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0]
print(countvote(arr))


# In[ ]:


mudgal = "Mudgal"
print("Kamal {0}".format(mudgal))


# In[ ]:


# Sorting problem 6 , 7 , 8:
# sorting an array with limited of integer. Hence Counting sort
# an array has n integer from range [1-n2] sort the array in o(n) time.

def sorting1_nsquare(arr):
    countingarr = [0]*(len(arr)*len(arr))
    for i in arr:
        countingarr[i] +=1
    print(countingarr)
    k = 0
    for i in range(0,len(countingarr)):
        for j in range(0,countingarr[i]):
            arr[k] = i
            k+=1
    print(arr)  

arr = [9,5,0,17,4]
print(sorting1_nsquare(arr))


# In[ ]:


# sorting Question 9
# find a+b = c in arr A and B
def findcomplement(arrA, arrB,c):
    if len(arrA) <1 or len(arrB) <1:
        return
    arrA.sort()
    arrB.sort()
    for i in range(0,len(arrA)):
        if c-arrA[i] in arrB:
            print(arrA[i],arrA)
            return True
arrA = [5,6,-2,3,4]
arrB = [0,6,7,2,-3,5]
print(findcomplement(arrA,arrB,12))


# In[ ]:


def binarysearch(arr,start,end,element):
    if start>=end:
        print("Not found")
        return False
    mid = start + (end-start)//2
    print(mid)
    if arr[mid] == element:
        print("element present at location:-",mid)
        return True
    if arr[mid] > element:
        # Search in left
        binarysearch(arr,start,mid,element)
    else:
        # search in rigt
        binarysearch(arr,mid+1,end,element)
    
    
arr = [1,2,3,4,5,6,7,8,9,33,35,40]
binarysearch(arr,0,len(arr),6)


# In[ ]:


# Chapter sorting question 10
def findcomplement3array(arrA,arrB,arrC,sum_abc):
    if len(arrA)<1 or len(arrB)<1 or len(arrC)<1:
        retrun 
    pass
# TO BE COMPLETED


# In[ ]:


# Sorting Question 16:
# Sort an array of o's 1's and 2's

def sortarray(arr):
    print("running sortarray")
    ptr_0 = 0
    ptr_2 = len(arr)-1
    i = 0
    
    while i<len(arr):
        print(i,ptr_0,ptr_2,arr)
        if arr[i] == 2:
            arr[i],arr[ptr_2]=arr[ptr_2],arr[i]
            ptr_2 -= 1
        if arr[i] == 0:
            arr[i],arr[ptr_0]=arr[ptr_0],arr[i]
            ptr_0 +=1
        if arr[i] == 1:
            i += 1
    print(arr)
    
sortarray([1,0,1,2,1,2,0,0,1,2,0,1,0,1])
            


# In[ ]:


print("kamal")

