def numofways(n):
    cache = [-1] * (n+1)
    return numofwayscatche(n,cache)
def numofways_raw(n):
    if n<0:
        return 0
    elif n == 0:
        return 1
    return numofways(n-1)+numofways(n-2)+numofways(n-3)

def numofwayscatche(n,cache):
    #print(n)
    if n<0:
        return 0
    elif n == 0:
        return 1
    elif cache[n] > -1:
        #print(cache[n])
        return cache[n]
    else:
        #print("populating cache:",cache)
        cache[n] = numofwayscatche(n-1, cache)+numofwayscatche(n-2,cache)+numofwayscatche(n-3,cache)
       # print("populating cache:", cache)
        #print(cache[n])
        return cache[n]


if __name__ == "__main__":
    import time

    start = time.time()
    print((numofways_raw(500)))
    "the code you want to test stays here"
    end = time.time()
    print(end - start)
    #start = time.time()
    print((numofways(50)))
    #end = time.time()
    #print(end - start)
