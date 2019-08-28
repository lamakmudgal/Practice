def printbin(arr,l):
    if l == len(arr):
        print(arr)
        return
    if arr[l] == "?":
        for i in range(0,2):
            arr[l] = i
            printbin(arr,l+1)
            #arr[l] = "1"
            #printbin(arr, l + 1)
            arr[l] = '?'
    else:
        printbin(arr,l+1)
arr = [1,"?",1,"?",0,1]
printbin(arr,0)
