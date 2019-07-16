def findfrequency(arr):
    n = len(arr)
    i = 0

    while i < n:
        if arr[i]<0:
            i = i + 1
            continue
        elementindex = arr[i] - 1
        if arr[elementindex] > 0:
            arr[i] = arr[elementindex]
            arr[elementindex] = -1
        else:
            arr[elementindex] = arr[elementindex] -1
            arr[i] = 0
            i = i +1
    print(arr)


arr = [5,4,4,3,2,3,1,1]
print(findfrequency(arr))

def permutationBT(arr,l,r):
    if arr == None:
        return -1
    if l == r :
        print(arr)
    else:
        for i in range(l,r+1):
            arr[l],arr[i] = arr[i],arr[l]
            #print("arr:-",arr)
            permutationBT(arr,l+1,r)
            arr[i], arr[l] = arr[l], arr[i]

arr = ["a","b","c"]
l = 0
r = len(arr)-1
permutationBT(arr,l,r)