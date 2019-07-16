def printarg(a,b,*c):
    print(a)
    print(b)
    print(c)
s = (1,2,3)
t = (11,12,13,14,15,16)
printarg(s,*t)