#Container With Most Water
def maxarea(arr):
    if len(arr)<2:
        return arr
    l = 0 
    r = len(arr)-1
    area = 0
    while l<r:
        area = max(area, min(arr[l],arr[r])*(r-l))
        print(area)
        if arr[l]>arr[r]:
            r-=1
        else:
            l+=1
    return area
# Driver code 
a = [1, 5, 4, 3] 
b = [3, 1, 2, 4, 5] 
print("###################### Max Area #######################")
print(maxarea(a)) 
print(maxarea(b))
print("###################### Max Area #######################")

def intToRoman(num):
    roman = ["I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"]
    divisor = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
    i = 12
    res = ""
    while num>0:
        if divisor[i] <= num:
            times = num//divisor[i]
            num = num%divisor[i]
            print(times,res)
            for j in range(0,times):
                res = res+roman[i]
            print("result",res,num)
            i -=1
        else:
            i -=1

print("################ INT TO ROMAN ###############################")
print(intToRoman(3456))
print("################ INT TO ROMAN ###############################")

# Roman to int
def value(r): 
    if (r == 'I'): 
        return 1
    if (r == 'V'): 
        return 5
    if (r == 'X'): 
        return 10
    if (r == 'L'): 
        return 50
    if (r == 'C'): 
        return 100
    if (r == 'D'): 
        return 500
    if (r == 'M'): 
        return 1000
    return -1


def romantoint(romannum):

    def romanToDecimal(str): 
        res = 0
        i = 0
        while (i < len(str)):
            s1 = value(str[i])
            if (i+1 < len(str)):
            # Getting value of symbol s[i+1]
                s2 = value(str[i+1])
                if (s1 >= s2): # Value of current symbol is greater
                    # or equal to the next symbol
                    res = res + s1
                    i = i + 1
                else:
                    # Value of current symbol is greater
                    # or equal to the next symbol
                    res = res + s2 - s1
                    i = i + 2
            else:
                res = res + s1
                i = i + 1
            return res
  
print("################ ROMAN TO INT ###############################")
print("IV")
print("################ ROMAN TO INT ###############################")

# Rotate Matrix
def printgrid(mat):
    for arr in mat:
        print(arr)
def tranpose(mat):
    for i in range(0,len(mat)):
        for j in range(i,len(mat)):
            mat[i][j],mat[j][i] = mat[j][i],mat[i][j]

def reversecol(mat):
    #c = len(mat)-1
    #j=0
    for i in range(0,len(mat)): # Col
        c = len(mat)-1
        j=0
        while j<c: # row
            mat[j][i],mat[c][i] = mat[c][i],mat[j][i]
            j+=1
            c-=1
def rotatemat(mat):
    tranpose(mat)
    printgrid(mat)
    reversecol(mat)
    printgrid(mat)
            
mat = [[1,2,3,4],
      [5,6,7,8],
      [9,10,11,12],
      [13,14,15,16]
      ]              

print("################ Rotate Matrix ###############################")
rotatemat(mat)
print("################ Rotate Matrix ###############################")

"""
Longest Substring Without Repeating Characters
"""
def longsubstr(s):
    if len(s)<2:
        return len(s)
    s = list(s)
    start = 0
    maxlen =1
    for i in range(1,len(s)):
        if s[i] in s[start:i]:
            print(s[start:i])
            maxlen = max(maxlen,i-start)
            start = i
    print(maxlen)

print("################ Longest Substring Without Repeating Characters ###############################")
longsubstr("seattleisveryrainy")
print("################ Longest Substring Without Repeating Characters ###############################")
            

def productExceptSelf(nums):
    #first lets create the output array using mult from right
    out = [0]*len(nums)
    start = 1

    #accumulate the mult from right in out array
    for i in range(len(nums)-1,-1,-1):
        out[i] = start
        start *= nums[i]
    print(out)
    #now maintain leftMult variable and use it for every index in out array
    leftMult = 1
    for i in range(len(out)):
        out[i] *= leftMult
        leftMult*=nums[i]
    print(out)
    return out
print("################ productExceptSelf ###############################")
productExceptSelf([1,2,3,4])
print("################ productExceptSelf ###############################")


class Solution:
    def missingNumber(self, nums):
        #sample = []
        #for i in range(0,len(nums))
        nums.sort()
        for i in range(0,len(nums)-1):
            if nums[i+1] != nums[i]+1:
                return nums[i+1]-1
        return 0
obj = Solution()
obj.missingNumber([1,2,4,5,9,8,0,7,6])


class Solution:
    def prisonAfterNDays(self, cells, N):
        def nextday(cells):
            next_day_cells = [0] *len(cells)
            for i in range(1,len(cells)-1):
                if cells[i-1] == cells[i+1]: 
                        next_day_cells[i] = 1
                else:
                        next_day_cells[i] = 0
            return next_day_cells
        
        seen = {}
        while N > 0:
            c = tuple(cells)
            if c in seen:
                N %= seen[c] - N
            seen[c] = N

            if N >= 1:
                N -= 1
                cells = nextday(cells)

        return cells
obj = Solution()
print("###### Prison after n days############")
print(obj.prisonAfterNDays([0,1,0,1,1,0,0,1],5))
print("###### Prison after n days############")


def findKthLargest(nums, k):
    # in-place quick-sort partition
    def partition(nums):
        i = 0
        pivot = nums[-1]
        for j in range(len(nums)-1):
            if nums[j] > pivot:
                nums[j],nums[i] = nums[i],nums[j]
                i += 1
        nums[i],nums[-1] = nums[-1],nums[i]
        return i
    
    while True:
            mid = partition(nums)
            print(nums)
            if mid+1 == k:
                return nums[mid]
            elif mid+1 < k:
                nums = nums[mid+1:]
                k -= (mid + 1) 
            else:
                nums = nums[:mid]
print("###### kth largest number by bin sort ############")
print(findKthLargest([13,7,2,8,4,3,9,22],5))
arr = [13,7,2,8,4,3,9,22]
arr.sort()
print(arr)
print("###### kth largest number by bin sort ############")

