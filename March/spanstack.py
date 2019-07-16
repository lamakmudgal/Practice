def findspan(arr):

    if len(arr) < 1:
        return 0

    span = [1]*len(arr)
    stack1 = [0]

    for i in range(1,len(arr)):

        while arr[stack1[-1]] <= arr[i]:
            stack1.pop()

        if len(stack1) ==0:
            span[i] = i+1
        else:
            span[i] = i - stack1[-1]
        stack1.append(i)

    print(span)

arr = [100, 80, 60, 70, 60, 75, 85]
findspan(arr)


