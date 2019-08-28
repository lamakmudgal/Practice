def findifanarrayisbionic(a):
    l= 0
    r = len(a)-1
    mid = (l+r)//2
    if a[l] < a[r]:
        print("Array is not biotonic")
        return False
    while l<r:
        print("l,r,mid",l,r,mid)
        if a[l]>a[mid]<a[r]: # starting point shall be on left
            print("if")
            r = mid
            mid = (l+r)//2

        elif a[l]<a[mid]>a[r]: # starting point is either ad mid or on right
            print("elif l,r,mid",l,r,mid)
            if a[mid-1]<a[mid]>a[mid+1]:
                print("Found begining of biotonic", a[mid])
                return a[mid]
            l = mid+1
            mid = (l+r)//2
        else:
            print("else")
            print("Repetitions")
            return -1

arr = [10,11,15,1,2,3,4,5,6,7,8,9]
findifanarrayisbionic(arr)