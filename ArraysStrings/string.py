# Meta String

def ifMetaString(str1,str2):
    count = 0
    posoffirst = -1

    if len(str1) != len(str2):
        return False

    for i in range(len(str1)):
        print(posoffirst)
        if str1[i] != str2[i] and count ==1:
            if str1[i] != str2[posoffirst]:
                return False
            else:
                return True
        elif str1[i]!=str2[i] and count ==0:
            count = count +1
            posoffirst = i

    return False

str1= "geepks"
str2= "keepgs"

print(ifMetaString(str1, str2))

