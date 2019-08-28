def printperm(arr,l,r):
    """
    n sized string
    This function print permutation of all strings you can make with two digits. 0's and 1's"""
    if l == r: # Print after the last swap in every iteration
        print(arr)
    for i in range(l,r+1):
        if arr[i] not in arr[l:i]:
            arr[l],arr[i] = arr[i],arr[l]
            printperm(arr,l+1,r)
            arr[l],arr[i] = arr[i],arr[l]
    if r-l == len(arr)-1 and 1 not in arr:
        # This check makes sure that the permutation of earlier array has been printed
        print("adding one")
        for i in range(0,len(arr)):
            arr[i] = 1
            printperm(arr,l,r)
arr = [0,0,0,0,0,0]
#printperm(arr,0,len(arr)-1)


def nsizedstring(n,k,mystr):
    if n <= 0:
        print(arr)
        return
    for i in range(0,k):
        mystr[n-1] = chr(i+ord('0'))
        print("b4 Track n i", n, i, mystr)
        nsizedstring(n-1,k,mystr)
        print("Track n i", n, i, mystr)
arr = [0,0,0]
nsizedstring(len(arr),2,arr)