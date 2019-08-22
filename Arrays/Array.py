def rotate1(nums, k):
    helper(0, len(nums) - 1 - (k % len(nums)), len(nums) - 1, nums)  # mid belongs to left part


def helper(start, mid, end, nums):
    left, right = mid - start, end - mid - 1
    print("left",left,"right",right,"mid",mid,"end",end)
    if left < 0 or right < 0:
        return
    if left > right:
        for j in range(mid + 1, end + 1):
            nums[j], nums[start] = nums[start], nums[j]
            start += 1
        helper(start, mid, end, nums)
    elif right >= left:
        i = mid
        while i >= start:
            nums[i], nums[end] = nums[end], nums[i]
            i, end = i - 1, end - 1
        if left != right:
            helper(start, mid, end, nums)




def rotate(nums: 'List[int]', k: 'int') -> 'None':
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n,j,k = len(nums),0,k%len(nums)
        while n>0 and k%n > 0:
            print("back to while")
            for i in range(0,k):
                nums[i+j],nums[len(nums)-k+i] = nums[len(nums)-k+i],nums[i+j]
                print(nums)
            j = j+k
            n = n-k
            k = k%n


def findinprogram(s1,s2):
    counter = 0
    begin = 0
    end = len(s1)
    while True:
        loc = s1.find(s2,begin,end)
        print(loc)
        if loc!= -1:
            counter += 1
            begin = loc+len(s2)
        else:
            return counter


nums = [1,2,3,4,5,6,7,8,9,10,11,12,13]
#rotate1(nums,3)
#print(nums)
print(findinprogram("AMAZON","AZ"))

i = 1; k = 2
print(i,k)