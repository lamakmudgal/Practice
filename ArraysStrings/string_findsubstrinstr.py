def findsubstring(s1,s2):
    a = len(s1)
    b = len(s2)
    if a<1 or b < 1 or b>a:
        print("incorrect input")
        return -1
    count = 0
    for i in range(0,a-b+1):
        if s1[i:i+b] == s2:
            print("found substring", s1[i:i+b])
            count = count+1
    if count == 0:
        print("Not found")
        return 0
    else:
        print("found : - ", count , " times")
        return count

s1 = "geieksforgeieks"
s2 = "geek"

print(findsubstring(s1,s2))

# replace consonent with nearest vowel
def replaceconsonant(s1):
    #nearvowel = "aaaeeeeiiiiioooooouuuuuuuu"
    nearconsonant = "bbcddfghhjklmnnpqrsttvwxyz"
    for i in range(0,len(s1)):
        s1 = s1.replace(s1[i],nearconsonant[ord(s1[i])-97])

    print(s1)
s1 = "kkmmll"
replaceconsonant(s1)