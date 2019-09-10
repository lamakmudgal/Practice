def findunique(s1,s2):
    dict1 = {}
    output = []
    for item in s1:
        if item not in dict1:
            dict1[item] = 1
        else:
            dict1[item] = dict1[item] + 1
    print(dict1)

    for item in s2:
        if item not in dict1:
            dict1[item] = 1
        else:
            dict1[item] = dict1[item] -1
    print(dict1)
    for keys in dict1:
        if dict1[keys] != 0:
            output = output+ [keys] * abs(dict1[keys])

    return output

s1 = [4,5,6]
s2 = [4,5,5,7]
print(findunique(s1,s2))
