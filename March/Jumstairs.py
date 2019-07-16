def numofways(n):
    cache = [-1] * (n+1)
    return numofwayscatche(n,cache)

def numofwayscatche(n,cache):
    #print(n)
    if n<0:
        return 0
    elif n == 0:
        return 1
    elif cache[n] > -1:
        return cache[n]
    else:
        #print("populating cache:",cache)
        cache[n] = numofwayscatche(n-1, cache)+numofwayscatche(n-2,cache)+numofwayscatche(n-3,cache)
       # print("populating cache:", cache)
        #print(cache[n])
        return cache[n]


if __name__ == "__main__":
    print((numofways(5)))
