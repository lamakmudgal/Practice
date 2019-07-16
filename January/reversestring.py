def reversestringwordbyword(str):

    str = str.strip()
    if len(str)==0:
        return 0
    if len(str)==1:
        return str
    finalstr=""
    liststr = str.split(" ")
    print(liststr)
    if len(str.strip())==0:
        return 0


    for i in range (len(liststr)-1,-1,-1):
        #print("som")
        print(liststr[i])
        if liststr[i] == "":
            continue
        elif i != -1:
            finalstr = finalstr + liststr[i][::-1] + " "

    return finalstr

#Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
#Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]

def reverseinplace(str):
    if len(str)==0:
        return " "
    if len(str) == 1:
        return str
    str.reverse()
    start = 0

    for i,items in enumerate(str):
        if items == " " or i== len(str)-1:
            print(str[start:i])
            reverse(str,start,i)
            start = i+1

def reverse(s):
    #print(s)
    if len(s) == 1:
        return s
    else:
        #newstr = s[-1] + newstr
        return (s[-1]+(reverse(s[:-1])))

def reverselist(s):
        #print(s)
        if len(s) == 1:
            return s
        else:
            return (list(s[-1])+(reverselist(s[:-1])))


def reverse(str, l, r):
    while l < r:
        str[l], str[r] = str[r], str[l]
        l += 1
        r -= 1

#print(reversestringwordbyword("hello how are you?"))
#print(reversestringwordbyword("I    am fine"))
#print(reversestringwordbyword(" "))
input = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
#input=["k","a","m","a","l"]
(reverseinplace(input))
print(input)