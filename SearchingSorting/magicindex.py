def magixindex(k):
    for i in range (0,len(k)):
        if k[i] == i:
            return i
    return "none"

def efficientmagixindex(k,start,totalelements):
    print("start,totalelements",start,totalelements)
    middle = (totalelements+start)//2
    if middle == start:
        return 0
    if middle == k[middle]:
        return middle
    if k[middle] < middle:
        start = middle
        print("this")
        return efficientmagixindex(k,start,totalelements)
    elif k[middle] > middle:
        totalelements = middle
        return efficientmagixindex(k, start, totalelements)

if __name__ == "__main__":
    k = [-10, 1, 30,11,20, 42, 47]
    totalelements = len(k)
    start = 0
    val = efficientmagixindex(k,start,totalelements)
    print(totalelements)
    print("val:-",val)
