def finduniquepair(s,k): # using hash
    """
    Find two pair of number in this array whose sum is K.
    :param s:
    :param k:
    :return:
    """
    dictpair = {}
    count = 0
    pairarr = []

    for item in s:
        if k-(item) in dictpair:
            count = count +1
            pairarr.append([item,k-item])
            dictpair.pop(k-item)
        else:
            dictpair[item] = 0

    print(pairarr)
    return count


def finduniquepairsort(s,k): # using hash
    if s is None or k is None:
        print("asd")
        return 0
    #s.sort()
    res = []
    for i in range(0,len(s)):
        remain = k-s[i]
        print("New start",s[i],remain)
        l = i+1
        r = len(s)
        while l<r:
            print("inwhileloop",s[l])
            if s[l]== remain:
                res.append([s[i],s[l]])
            l+=1
    print(res)
    return res


s = [5,9,4,2,1,3,3,-1,-5,-1,7]
k = 6
#print(finduniquepair(s,k))
print(finduniquepairsort(s,k))