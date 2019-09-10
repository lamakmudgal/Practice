def sumofnumbers(n):
    if n == 0:
        return 1
    else:
       return n * sumofnumbers(n-1)

def sumofdigits(n):

    print(n)
    if n<=9:
        return n
    #else:
    #print(n%(10^len(str(n))))
        return sumofdigits(n//10) + n%10

def reverse(s):
    #print(s)
    if len(s) == 1:
        return s
    else:
        #newstr = s[-1] + newstr
        return (s[-1]+reverse(s[:-1]))
print(reverse("kamal mudgal"))
def permutaion(s):
    # base case:
    print("s is:",s)
    out = []
    if len(s) == 1:
        out= [s]
    # Recurssion Case:
    else:
        for i,let in enumerate(s):
            print("let",let)
            for perm in permutaion(s[:i]+s[i+1:]):
                print("perm",perm)
                out += [let+perm]
                print("out",out)
    return out

def fib(n):
    if n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)


def fibnum(n, known_results):
    # base case 0 and 1 as the value is one.
    if n < 2:
        return 1
    if known_results[n] > 0:
        return known_results[n]

    val = fibnum(n - 1, known_results) + fibnum(n - 2, known_results)
    known_results[n] = val
    return val

def coinchangedyn(target, coinarr, known_results):
    print("target=",target)
    min_coins = target

    if target in coinarr:
        known_results[target] =1
        return 1
    elif known_results[target]>0: # return known result
        return known_results[target]
    else:
        #lessvalcoins =
        for i in [c for c in coinarr if c<=target]:
            print("Started for")
            num_coins = 1+ coinchangedyn(target-i,coinarr,known_results)
            print("num_coins",num_coins,target-i)
            if num_coins  < min_coins:
                min_coins = num_coins
                known_results[target] = min_coins
    return min_coins

def coinchange(target, coinarr):
    print("target=",target)
    min_coins = target

    if target in coinarr:
        return 1
    else:
        #lessvalcoins =
        for i in [c for c in coinarr if c<=target]:
            print("Started for")
            num_coins = 1+ coinchange(target-i,coinarr)
            print("num_coins",num_coins,target-i)
            if num_coins  < min_coins:
                min_coins = num_coins
    return min_coins
#print(sumofnumbers(800))
#print(sumofdigits(1000))
#print(reverse("KAMAL"))
#print(reverse("jai mata di"))
#print(reverse("1233453453545"))
#print(reverse("3445445%%%%%//////234"))
#print(permutaion("abc"))
#print(fib(5))
kr = [0]*101
#print(coinchangedyn(63,[1,5,10,25],kr))

#print(fibnum(100,kr))
import random
def roll():
	return random.randint(1,5)


def roll5_7():
    while True:
        roll1 = (roll() - 1) * 5
        roll2 = roll()

        if (roll1 + roll2) > 21:
            pass
        else:
            return (roll1 + roll2) % 7 + 1

#for i in range(0,100):
#    print(roll5_7())

def findsqrt(n):
    if n < 0:
        return ValueError

    if n == 1:
        return 1

    for i in range(1, (n // 2 + 1)):
        print(i)
        if i * i == n:
            return i
        elif i*i > n:
            return i - 1
    return i
def findsqrtfast(n):
    if n < 0:
        return ValueError

    if n == 1:
        return 1
    low = 0
    high = n//2+1

    while low+1 <high:
        mid = low + (high-low)/2
        midsqr = mid * mid
        if  midsqr==n:
            return mid
        elif midsqr < n:
            low = mid
        else:
            high = mid
        return low

#print(findsqrt("kamal"))

k = [1, 5, 6, 21, 33, 44, 45, 46, 56, 67, 78, 88, 89, 99, 101, 109, 123]


def searchnumber(num, sorted_arr):
    low = 0
    high = len(sorted_arr)
    while low + 1 < high:
        mid = low + (high - low) // 2
        print("low,mid,high",low,mid,high)
        if sorted_arr[mid] == num:
            return mid
        elif sorted_arr[mid] < num:
            low = mid
        else:
            high = mid
    return "Not Found"

#print(searchnumber(123,k))
arr_num = [-14,-20,5,6,8,4]
def highofthree (arr_num):
    high = max(arr_num[0],arr_num[1])
    low = min(arr_num[0],arr_num[1])
    high_pdtof2 = arr_num[0]*arr_num[1]
    low_pdtof2 = arr_num[0] * arr_num[1]
    high_pdtof3 = arr_num[0]*arr_num[1]*arr_num[2]
    for i in range(2,len(arr_num)):
        high_pdtof3 = max(high_pdtof3,high_pdtof2*arr_num[i],low_pdtof2*arr_num[i])
        high_pdtof2 = max(high_pdtof2,high*arr_num[i])
        low_pdtof2 = min(low_pdtof2, low*arr_num[i])
        high = max(high, arr_num[i])
        low = min(low, arr_num[i])
    return high_pdtof3

#print(highofthree(arr_num))

def findmindenom(target, arr_coin,known_val):
    mincoins = target
    if target in arr_coin:
        return 1
    elif known_val[target]>0:
        return known_val[target]
    else:
        for i in [c for c in arr_coin if c<target]:
            numofcoins = 1 + findmindenom((target - i), arr_coin,known_val)
            if mincoins > numofcoins:
                mincoins = numofcoins
                known_val[target] = mincoins

    return mincoins
target = 63
arr_coin = [1,5,10,25]
known_val = [0]*(target+1)
#print(findmindenom(target,arr_coin,known_val))
def strtoint(strdig):
    dig = ""
    sign=""
    finalnum = 0
    for i,chars in enumerate(strdig.strip()):
        #rint(chars)
        if i == 0 and chars not in ["+","-","1","2","3","4","5","6","7","8","9","0"]:
            return 0
        elif i == 0 and (chars == "-" or chars =="+"):
            #print("chars",chars)
            sign = chars
        elif chars in ["1","2","3","4","5","6","7","8","9","0"]:
            dig= dig+chars
        else:
            break

    if sign == "-":
        finalnum = 0-int(dig)
    else:
        finalnum = int(dig)

    if (finalnum < -2 ** 31):
        return -2 ** 31
    elif (finalnum > 2 ** 31 - 1):
        return 2 ** 31 - 1
    else:
        return finalnum



#print(strtoint("3.14159"))
#print(strtoint("   -42"))
#print(strtoint("4193 with words"))
#print(strtoint("words and 987"))
#print(strtoint("  asd456 kamla"))
#print(strtoint("-91283472332"))
#print(strtoint("  -452457845724857245724387528475892437582345724857485"))




