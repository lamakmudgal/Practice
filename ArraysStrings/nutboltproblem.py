def mergenutsandbolts(nuts, bolts, low, high):
    if low < high:
        pivot = partition(nuts, low, high, bolts[high])
        print("nuts partition called", nuts[low:high + 1],pivot)
        # print(pivot,bolt[high])
        # print("nuts",nuts,pivot)
        partition(bolts, low, high, nuts[pivot])
        print("bolts partition called", bolts[low:high + 1])

        # print("bolts",bolts)
        print("low:-", low, "pivot-1", pivot - 1)
        print("pivot+1:-", pivot + 1, "high", high)
        mergenutsandbolts(nuts, bolts, low, pivot - 1)
        mergenutsandbolts(nuts, bolts, pivot + 1, high)
        print("Final Res:-",nuts,bolts)


def partition(arr, low, high, pivot):
    # print(arr[low:high+1])
    piv = 0
    i = low
    for j in range(low,high):
        if arr[j]<pivot:
            arr[i],arr[j] = arr[j],arr[i]
            i+=1
        elif arr[j] == pivot:
            arr[j],arr[high] = arr[high],arr[j]
            j-=1
    #print(arr)
    arr[i],arr[high] = arr[high],arr[i]
    #print(arr)
    return i


nuts1 = [5, 4, 6, 2, 1, 3]
bolts1 = [4, 5, 6, 1, 3, 2]
mergenutsandbolts(nuts1, bolts1, 0, 5)