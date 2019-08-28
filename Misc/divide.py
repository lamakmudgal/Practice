def divide(dividend,divisor):
    #dividend1 = dividend
    #divisor1 = divisor
    i = 0
    negative = False
    #print(dividend,divisor)
    if divisor < 0:
        print("divisor less than 0")
        if negative == False:
            negative = True
            divisor = divisor * -1
        else:
            negative == False
    if dividend < 0:
        print("dividend less than 0")
        if negative == False:
            negative = True
            dividend = dividend*-1
        else:
            negative == False
    cont = True
    while cont:
        print(dividend,divisor)
        dividend = dividend-divisor
        i = i +1
        if dividend<=divisor:
            cont = False
            #break
    #if i>2**31:
    #    return 2**31 - 1
    #return i

    print("result", i)
    if negative == True:
        print("as one of them was negative")
        return i*-1
    else:
        print("1111")
        return i


print(divide(-7,-3))