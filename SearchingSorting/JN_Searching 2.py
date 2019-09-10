#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Question 40 Find elemement in bitonic array.
def find_num_bionic(arr,element):
    start = 0
    end = len(arr)-1
    while start<end:
        mid = (end+start)//2
        print("Arr Mid",arr[mid])
        if arr[mid] == element:
            print("Element found",arr[mid])
            return mid
        if arr[mid] >= arr[start]:
            if arr[start] <= element < arr[mid]:
                end = mid-1
            else:
                start = mid+1
        else:        
            if arr[mid] < element < arr[end]:
                start = mid+1
            else:
                end = mid-1
    
    print("Not Found")
    return False
arr = [15,16,19,20,25,1,3,4,5,7,10,14]
find_num_bionic(arr,15)


# In[ ]:


# question 41 find element in bitonic array using recurrsion. 

def find_elem_bitonic_recur(arr,start,end,element):
    if len(arr) < 2:
        return False
    mid = (start+end)//2
    
    if arr[mid] == element:
        print("found the element at ",mid,arr[mid])
        return True
    if arr[mid] >= arr[start]:
        if arr[start] > element > arr[mid]:
            return find_elem_bitonic_recur(arr,start,mid-1,element)
        else:
            return find_elem_bitonic_recur(arr,mid+1,end,element)

    else:
        if  arr[end] > element > arr[mid]:
            return find_elem_bitonic_recur(arr,mid+1,end,element)
        else:
           return find_elem_bitonic_recur(arr,start,mid-1,element)
arr = [15,16,19,20,25,1,3,4,5,7,10,14]
#print(find_elem_bitonic_recur(arr,0,len(arr)-1,15))
            


# In[ ]:


# Question 44 Median of n integers
def find_median(arr):
    arr.sort()
    n = len(arr)
    if n%2 == 0:
        return (arr[n//2] + arr[(n//2)-1])/2
    else:
        return arr[n//2]
arr =[5,10,15,20,25]
print(find_median(arr))


# In[ ]:


#Question 46: first occurance of number in sorted array
def first_occurance(arr,elem):
    start =0
    end = len(arr)-1
    
    continue_search = True
    while start<end:
        mid = (start+end)//2
        print(start,end,mid)
        if mid ==0 and arr[mid] == elem:
            print("first occurance at first element found")
            continue_search = False
            return mid
        if arr[mid] == elem: 
            print("Element found checking if its first occurance")
            if mid>0 and arr[mid-1] != elem:
                print("first occurance found")
                continue_search = False
                return mid
        if arr[mid] > elem:
            end = mid-1
        elif arr[mid] == elem:
            end =mid
        else:
            start = mid+1
    print("Element not found")
    return False
arr =[5,5,5,5,5,5,5,6,6,6,6,6,6,6,9,12,15,21,21,34,45,57,70,84,84,84,84,84,84,84,84]     
first_occurance(arr,6)

    


# In[ ]:


#Question 47: first occurance of number in sorted array
def last_occurance(arr,elem): # Fix NOT Working
    start =0
    end = len(arr)-1
    
    continue_search = True
    while start<end:
        mid = (start+end)//2
        print(start,end,mid)
        if arr[mid] ==arr[end] and arr[mid] == elem:
            print("Last occurance at Last element found")
            return mid
        if arr[mid] == elem: 
            print("Element found checking if its last occurance")
            if mid>0 and arr[mid+1] != elem:
                print("Last occurance found")
                continue_search = False
                return mid
        if arr[mid] > elem:
            end = mid-1
        elif arr[mid] == elem:
            start =mid
        else:
            start = mid+1
    print("Element not found")
    return False
arr =[5,5,5,5,5,5,5,6,6,6,6,6,6,6,9,12,15,21,21,34,45,57,70,84,84,84,84,84,84,84,84]     
last_occurance(arr,84)


# In[ ]:


# Q 48,49,50
# Counting sort
# Binary search and for loop
# Q47last occurange - 46 first occurance

# Q51 Bakwass

# Q 52 Second Smallest

# Q 53 tournament like method

# Q 54 most frequent element , element which appear n/2 times. 
# Q55,56,57,58


# In[ ]:


#Q59 Array of 2n element where n are same and n are different how to find. 
# When unsorted the same elements on instance of same would be maximum 2 places away or next to each ohter
# This way if you do a loop of 
# first pass compare i with i +1 and anything matches this is the result
# Second pass compare i with i+2 is any element match its the answe 


# In[ ]:


#60 array has 2n+1 elements....all but one is repeated.. find the one which is not repeated.
# XOR
def find_nonrepeated(arr):
    if len(arr)<2:
        return
    x = arr[0]
    for i in range(1,len(arr)):
        x = x^arr[i]
    
    return x
arr = [1,1,33,33,23,22,23,22,4,55,66,55,66]
print(find_nonrepeated(arr))


# In[ ]:


# 61 Throwing egg from a building
# refer to divide an concur chapter


# In[ ]:


#62 Local Minimun in an array
# a[i-1]>= a[i] <=a[i+1]
def local_min(arr):
    start = 0
    end  = len(arr)-1
   
    
    while start < end:
        mid = (start+end)//2
        print(start,end,mid)
        if mid == 0:
            if arr[mid] <= arr[mid+1]:
                print(arr[mid],"is local minimum at the begin")
                return arr[mid]
        if mid == len(arr)-1:
            if arr[mid] <= arr[mid-1]:
                print(arr[mid],"is local minimum at the end")
                return arr[mid]
        if arr[mid-1] >= arr[mid] <= arr[mid+1] :
            print("local minimum is arr[mid]")
            return arr[mid]
        if arr[mid] > arr [mid-1]:
            end = mid-1
        else:
            start = mid+1

arr = [22,14,15,16,14,13,17,35,67,78,22,88]
print(local_min(arr))


# In[ ]:


# q 63  and 64
# n*n array all element are distinct write a fun to find a value in o(n) time. columns and rows are 
# in assending order

def find_elem_matrix(arr,elem):
    row = 0 
    column = len(arr[0])-1
    print(row,column)
    
    while column > -1 and row < 4:
        print(arr[row][column])
        if arr[row][column] == elem:
            print("element found")
            return arr[row][column]
        if arr[row][column] > elem:
            column -= 1
        else:
            row +=1
    print("element not in the array")
arr = [[1,2,3,4,5,6,7,8,9],
      [11,12,13,14,15,16,17,18,19],
      [21,22,23,24,25,26,27,28,29],
       [31,32,33,34,35,36,37,38,39]]
find_elem_matrix(arr,121)


# In[ ]:


# Q 66 Work again


# In[ ]:


# Q67 : Array of unknow lenth has numbers in the begining and symbol in the end find
# the element where symbol starts
# start at begining and keep adding 2 to see if the element is symbol or number then do n-1 to come back


# In[ ]:


# 67 ,68,69, separate odd and even numbers
def separate_even_odd(arr):
    if len(arr)<2:
        return 
    even_count =len(arr)-1
    i = 0 
    while i < even_count:
        print(arr)
        if arr[i]%2 == 0:
            print("even num",arr[i],arr[even_count])
            arr[i],arr[even_count] = arr[even_count],arr[i]
            print("even num after swap",arr[i],arr[even_count])
            even_count -=1
        else:
            i +=1
    print(arr)
arr = [5,8,6,7,7,9,11,12,13,14,15,16,17,18,19]
separate_even_odd(arr)


# In[ ]:


# dutch flag problem
# Q70
def dutchflag(arr):
    z= 0
    i = 0
    t = len(arr)-1
    while z<t and i < t:
        print(arr,i,z,t)
        if arr[i] == 1:
            i += 1
        if arr[i] == 0:
            arr[i],arr[z] = arr[z],arr[i]
            z +=1
        if arr[i] == 2:
            arr[i],arr[t] = arr[t],arr[i]
            t -=1
    print(arr)

arr = [1,0,2,2,1,0,0,1,1,2,2,0,0,1,1,1,2,0,0,0,0]
print(dutchflag(arr))


# In[ ]:


# Q 71 Divide and concur revisit 


# In[ ]:


# Q 72 XOR all the elements.. problem of repeating odd times.


# In[ ]:


def trailingzero_fact(n):
    ten = n//10
    five = (n%10)//5
    two = ((n%10)%5)//2
    return ten+(five+two)//2
print(trailingzero_fact(100))


# In[1]:


# Q 74,75 [a1,a2,a3,a4,b1,b2,b3,b4] to [a1,b1,a2,b2,a3,b3,a4,b4]
def shufflecharacters(start,end,arr):
    #print("begin",start,end,arr)
    if end-start == 1:
        #print("exiting")
        return
    mid = (end+start)//2
    smallmid =(start+mid)//2
    temp = mid+1
    print(temp,smallmid)
    #print("before for",smallmid,mid)
    for i in range(smallmid+1,mid+1):
        #print(mid,i)
        arr[i],arr[temp] = arr[temp],arr[i]
        temp+=1
    #print("calling for left and right",arr,start,mid,end)
    shufflecharacters(start,mid,arr) 
    #print("left side done")
    shufflecharacters(mid+1,end,arr)
    print(arr)
arr =[1,2,3,4,5,6,7,8]
shufflecharacters(0,len(arr)-1,arr)


# In[6]:


#Q 76 77 WORK MORE
def max_index_diff(arr):
    currmax = 0
    i=0
    l=r=0
    n = len(arr)-1
    while i<len(arr)-1 and i<n:
        print(arr,i,n,currmax,l,r)
        if arr[n]>arr[i]:
            if currmax < n-i:
                currmax = n-i
                l = i
                r = n
            i += 1
            n = len(arr)-1
        else:
            n -= 1
    print(currmax,l,r)
arr = [34,8,10,3,2,80,30,33,1]
print(max_index_diff(arr))


# In[7]:


# 78 Pair sorting
# loop with 2 as increment


# In[14]:


# 79 find frequency add length....

def findfreq(arr):
    arr_len = len(arr)
    for i in range(0,arr_len):
        index = arr[i]%arr_len
        arr[index] = arr[index] + arr_len
    print(arr)
    for i in range(0,arr_len):
        arr[i] = arr[i]//arr_len
    print(arr)
arr = [10,1,9,4,7,6,5,5,1,2,1]
    
findfreq(arr)


# In[10]:


3%9

