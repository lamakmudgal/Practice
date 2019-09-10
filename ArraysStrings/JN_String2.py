"""
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.
Example 1:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Example 2:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
"""
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        s1ptr,s2ptr,s3ptr = 0,0,0
        
        while s1ptr<len(s1) and s2ptr<len(s2) and s3ptr<len(s3):
            print(s1ptr,s2ptr,s3ptr)
            
            if s3[s3ptr] == s2[s2ptr]:
                s2ptr += 1
            elif s3[s3ptr] == s1[s1ptr]:
                s1ptr+=1
            else:
                print("main position",s1ptr,s2ptr,s3ptr)
                return False
            s3ptr+=1
        
        if s1ptr<len(s1):
            while s1ptr<len(s1) and s3ptr<len(s3):
                if s3[s3ptr] == s1[s1ptr]:
                    s1ptr+=1
                else:
                    print("s1 position",s1ptr,s3ptr)
                    return False
                s3ptr+=1
        elif s2ptr<len(s2):
              while s2ptr<len(s2) and s3ptr<len(s3):
                    if s3[s3ptr] == s2[s2ptr]:
                        s2ptr += 1
                    else:
                        print("s2 position",s2[s2ptr:],s3[s3ptr:])
                        return False
                    s3ptr+=1
        elif s3ptr<len(s3):
            return False
        return True
obj = Solution()
obj.isInterleave("aabcc","dbbca","aadbbcbcac")

def compressstring(string):
    if len(string)<1:
        return 0
    c = 0 
    t = 0 
    count = 1
    while c<len(string)-1 and t<len(string)-1:
        print(c,t,count,string)
        if string[c] == string[c+1]:
            count+=1
            c+=1
        elif string[c] != string[c+1] and count ==1 :
            t+=1
            c+=1
        else :
            string[t] = string[c]
            t+=1
            string[t] = count
            t+=1
            count = 1
            c+=1
    if count > 1:
        string[t] = string[c]
        t+=1
        string[t] = count
        t+=1
    else:
        string[t] = string[c]
        t+=1
    print(string,t)
print("################ Compress string ################")
compressstring(["a","a","b","c","c","c","d","d","d","d","e"])
print("################ Compress string ################")
