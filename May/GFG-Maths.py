def isjumpingnumber(n):
    strn = str(n)
    if len(strn)==1:
        return True
    for i in range(len(strn)-1):
        #print(strn[i],strn[i+1])
        if abs(int(strn[i]) - int(strn[i+1])) != 1:
            print("returnging false for:-",n)
            return False
    #print("returnging true for:-", n)
    return True

testcases = int(input())
for i in range(testcases):
    number = int(input())
    jumpingnums = []
    for iter in range(1,number):
        if isjumpingnumber(iter):
            jumpingnums.append(iter)
    print(jumpingnums)

