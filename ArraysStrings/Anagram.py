"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
The order of output does not matter.
Example 1:
Input:
s: "cbaebabacd" p: "abc"
Output:
[0, 6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:
Input:
s: "abab" p: "ab"
Output:
[0, 1, 2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""

def findanagram(s,p):
    if len(s) == 0 or len(s) < len(p):
        return [0]
    #set_of_p = {val for val in p}
    #print(set_of_p)
    finallist = []
    for i in range(0,len(s)+1):
        if i < len(s)+1-len(p):
            print(s[i:i+len(p)])
            if isanagram(s[i:i+len(p)], p):
                finallist.append(i)
    return finallist


def isanagram(firststring, secondstring):
    len1 = len(firststring)
    len2 = len(secondstring)

    if len1 != len2:
        return False

    dictCounter = [0]*26

    for i in range(0, len(firststring)):
        dictCounter[ord(firststring[i])-ord("a")] +=1
        dictCounter[ord(secondstring[i])-ord("a")] -=1

    for counter in dictCounter:
        if counter != 0:
            return False
    #print(dictCounter)
    return True

def isAnagramsorting(s1,s2):
    if len(s1) ==0 and len(s2)==0:
        return False
    print(sorted(s1))
    print(sorted(s2))
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False

s = "cbaebabacb"
p = "abc"

print(findanagram(s,p))
#print(isanagram("kamal","lamak"))

something = "asdfadfadfadfadfadfqrgntyentynynynytngbrtyehdfgyh"
somethingdict = {}
for char in something:
    if char not in somethingdict:
        somethingdict[char] = 1
    else:
        somethingdict[char] +=1
#print(somethingdict)