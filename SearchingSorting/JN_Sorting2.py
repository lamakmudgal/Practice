#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Sorting Question 22:
# Nearly sorted. Every element in array with n element is at max k steps away from correct sorted position. 
# Approach divide the array n/k arrays. Sort and merge these. 
def nearlysortedarray(arr,k):
    karray = []
    start = 0
    end = len(arr)
    loop = True
    while loop :
        karray.append(sorted(arr[start:start+k]))
        if end-(start+k) > k:
            start = start+k
        else:
            karray.append(arr[start+k:])
            loop = False
    # merge sorted array
    loop = True
    result = []
    for arrnum in range(1,len(karray)):
        result = []
        i = j = l=0
        while i<(len(karray[0])) and j<len(karray[arrnum]):
            #print(i,j,k,arrnum,len(karray[0]))
            if karray[0][i] <= karray[arrnum][j]:
                result.append(karray[0][i])
                i+=1
            else:
                result.append(karray[arrnum][j])
                j+=1
        if i<len(karray[0]):
            for item in range(i,len(karray[0])):
                result.append(karray[0][item])
        if j<len(karray[arrnum]):
            for item in range(j,len(karray[arrnum])):
                result.append(karray[arrnum][item])
        karray[0] = result
        print("karray",karray[0])
nearlysortedarray([1,22,3,4,5,66,7,8,99,10,111,12,103,134,15,16],3)
    


# In[4]:


import heapq
def nearlysortedheap(arr,k):
    heaparr = []
    result = []
    for i in range (0,k):
        heaparr.append(arr[i])
    heapq.heapify(heaparr)
    j=k+1
    while len(heaparr)>0 and j<len(arr):
        heapq.heappush(heaparr,arr[j])
        j+=1
        #print(j)
        result.append(heapq.heappop(heaparr))
    if len(heaparr)>0:
        while len(heaparr)>0:
            result.append(heapq.heappop(heaparr))
    print(result)   
nearlysortedheap([1,22,3,4,5,66,7,8,99,10,111,12,103,134,15,16],3)
 


# In[13]:


#Sorting chapter problem 33
#sorted arr1 len = m+n element m , sorted arr2, len n element n.
def mergesortedarrayinplace(arr1,arr2):
    sort = True
    l = len(arr1)-1
    n= len(arr2)-1
    k = n
    j=0
    while n>-1 and k>-1 and l>-1:
        if arr1[k] > arr2[n]:
            arr1[l]=arr1[k]
            k -= 1
            l -= 1
        else:
            arr1[l] = arr2[n]
            n-=1
            l-=1
    if k>-1:
        while k>-1 and l>-1:
            arr1[l] = arr1[k]
            k -= 1
            l -= 1
    if n>-1:
        while n>-1 and l>-1:
            arr1[l] = arr2[n]
            n -= 1
            l -= 1
    print(arr1)
    
arr1 = [17,27,37,47,50,0,0,0,0,0]
arr2 = [1,14,15,16,17]
mergesortedarrayinplace(arr1,arr2)       


# In[30]:


def mergenutsandbolts(nuts,bolt,low,high):
    if low<high:
        pivot = partition(nuts,low,high,bolt[high])
        print("nuts partition called",nuts[low:high+1])
        #print(pivot,bolt[high])
        #print("nuts",nuts,pivot)
        partition(bolts,low,high,nuts[pivot])
        print("bolts partition called",bolts[low:high+1])
        
        #print("bolts",bolts)
        print("low:-",low,"pivot-1",pivot-1)
        print("pivot+1:-",pivot+1,"high",high)
        mergenutsandbolts(nuts,bolts,low,pivot-1)
        mergenutsandbolts(nuts,bolts,pivot+1,high)

def partition(arr,low,high,pivot):
    #print(arr[low:high+1])
    piv = 0
    i = low
    while i < high:
       # print(arr[i],pivot,piv)
        if arr[i]<pivot:
            arr[i],arr[piv] = arr[piv],arr[i]
            piv +=1
            i+=1
        elif arr[i] == pivot:
            arr[i],arr[high] = arr[high],arr[i]
           # i+=1
        else:
            i+=1
            
    #print("partitioned",arr)
    arr[high],arr[piv] = arr[piv],arr[high]
    #print("partitioned",arr)
    return piv

nuts1= [5,4,6,2,1,3]
bolts1 = [4,5,6,1,3,2]
mergenutsandbolts(nuts1,bolts1,0,5)

