def binarysearch(arr,element):
    found = False
    l = 0
    r = len(arr)
    mid = (l+r)//2
    while l<=r:
        print("l,r,mid",l,r,mid,arr[mid])
        if arr[mid] == element:
            print("Found the element")
            return mid
        if element < arr[mid]: # in left
            r = mid-1
            mid = (l+r)//2
        else:
            l=mid+1
            mid = (l + r) // 2

arr = [1,3,5,7,9,14,15,18,28,45,56,78,89,99,130]
print(binarysearch(arr,130))
print(binarysearch(arr,1))
print(binarysearch(arr,7))
print(binarysearch(arr,78))