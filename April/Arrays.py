def isAnagram(s1,s2):
    if len(s1) ==0 and len(s2)==0:
        return False
    print(sorted(s1))
    print(sorted(s2))
    if sorted(s1) == sorted(s2):
        return True

    else:
        return False


s1 = "clint eastwood"
s2 = "old west action"
#print(isAnagram(s1,s2))

def finduniquepair(s,k):
    dictpair = {}
    count = 0
    pairarr = []

    for item in s:
        if k-abs(item) in dictpair:
            count = count +1
            pairarr.append([item,k-item])
            dictpair.pop(k-item)
        else:
            dictpair[item] = 0

    print(pairarr)
    return count


s = [5,9,4,2,1,3,3,-1,-5,7,-1]
k = 6
print(finduniquepair(s,k))