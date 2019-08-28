# Python3 effective program to
# shuffle an array of size 2n

# Function to shuffle an array of size 2n
def shufleArray(a, f, l):
    # If only 2 element, return
    if (l - f == 1):
        return

    # Finding mid to divide the array
    mid = int((f + l) / 2)

    # Using temp for swapping first
    # half of second array
    temp = mid + 1

    # Mid is use for swapping second
    # half for first array
    mmid = int((f + mid) / 2)
    print("mid,l,f",mid,l,f,mmid)
    # Swapping the element
    for i in range(mmid + 1, mid + 1):
        (a[i], a[temp]) = (a[temp], a[i])
        print(a)
        temp += 1

    # Recursively doing for first
    # half and second half
    shufleArray(a, f, mid)
    shufleArray(a, mid + 1, l)


# Driver Code
a = ["a1","a2","a3","a4","b1","b2","b3","b4"]
n = len(a)
shufleArray(a, 0, n - 1)

print(a)