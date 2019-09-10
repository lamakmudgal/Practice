
# find a substring in a string
def findsubstr(string , substr):
    if len(substr) < 1 or len(string)<len(substr):
        return
    res =[]
    for i in range(0,len(string)-len(substr)+1):
        for j in range(0,len(substr)):
            print(i,j)
            if substr[j]!=string[i+j]:
                print("no match so breaking")
                break
            elif j == len(substr)-1:
                print("found at location ",i,string[i:])
                res.append(i)
    print(res)
    return res
findsubstr("amazonamazonamazonamazonamazonamazon","on")   
            
# reverse string
def reversestring(string):
    start = 0
    end = len(string)-1
    arr = list(string)
    while start<end:
        arr[start],arr[end]=arr[end],arr[start]
        start +=1
        end -=1
    return ("".join(arr))
print(reversestring("kamal"))

def reversestringsecond(string):
    c =""
    for char in string:
        c = char+c
    print(c)
reversestringsecond("kamal")

def reverse_sen_words(string):
    string = list(string.split(" "))
    for i in range(0,len(string)):
        string[i] = reversestring(string[i])
    print(string)
print("############# Reverse sentence new#################")
reverse_sen_words("I am not doing this")
print("############# Reverse sentence new#################")



def reverseasentence(string):
    string = list(string)
    start = 0
    end = len(string)
    w_start = 0
    w_end= 0
    
    while start<end:
        if string[start] == " " or start == end-1:
            if start ==end-1:
                w_end=start
            else:    
                w_end= start-1
            while w_start < w_end:
                string[w_start],string[w_end] = string[w_end],string[w_start]
                w_start += 1
                w_end -=1
            w_start = start+1
        start +=1
        #end -=1
    return("".join(string))
print("############ Reverse a sentense ##############################")
reverseasentence("I am not doing this")
print("############ Reverse a sentense ##############################")

# permutaion of a string
def permutations(elems):
    for perm in recur_param(elems,[]):
        print(perm)
def recur_param(elems,sofar):
    if len(elems) ==0:
        yield sofar
    else:
        for i in range(0,len(elems)):
            for perm in recur_param(elems[0:i]+elems[i+1:],sofar+[elems[i]]):
                yield perm
print("######### Permutations ############")
print(permutations("abc"))
print("######### Permutations ############")


res = []
def perm(l,r,arr):
    if l == r:
        temp = "".join(arr)
        res.append(temp)
    for i in range(l,len(arr)):
        if arr[i] not in arr[l:i]:
            arr[l],arr[i] = arr[i],arr[l]
            perm(l+1,r,arr)
            arr[l],arr[i] = arr[i],arr[l]
        #arr[l],arr[i] == arr[i],arr[l]
perm(0,2,["a","d","c"])


print("########## Combination ###############")
def comb(elems,s,idx,res):
    for i in range(idx,len(elems)):
        s+=elems[i]
        res.append(s)
        comb(elems,s,i+1,res)
        s=s[0:-1]
res = []
comb("abc","",0,res)
print(res)
print("########## Combination ###############")

print("############# substring in string ##########")
class Solution:
    result = []
    
    def createperm(self,s1arr,l,r):
        if l == r:
            self.result.append("".join(s1arr))
        for i in range(l,r+1):
            if s1arr[i] not in s1arr[l:i]:
                s1arr[l],s1arr[i] = s1arr[i],s1arr[l]
                self.createperm(s1arr,l+1,r)
                s1arr[l],s1arr[i] = s1arr[i],s1arr[l]
    def findsubstr(self,patteren,string):
        #print("function call", patteren,string)
        for i in range(0,len(string)-len(patteren)):
            for j in range(0,len(patteren)):
                if patteren[j] != string[i+j]:
                    break
                if j == len(patteren)-1:
                    print("found at",string[i+j:])
                    return True
    def checkInclusion(self, s1: str, s2: str) -> bool:
        self.createperm(list(s1),0,len(s1)-1)
        print(self.result)
        for item in self.result:
            if self.findsubstr(item,s2) is True:
                print("Found it")
                return True
        else:
            return False
        
obj = Solution()
print(obj.checkInclusion("adc","dcda"))
print("############# substring in string ##########")

def decode(str):
    arr = list(str)
    res = ""
    substr =""
    blockstart = 0
    while len(arr)>0:
        elem = arr.pop()
        #print(elem)
        if elem == "]":
            if blockstart == 0:
                res = substr+res
                substr = ""
            blockstart += 1
        elif elem == "[":
            blockstart -=1
        elif elem.isdigit() is True:
            if blockstart ==0:
                res = int(elem)*substr+res
                substr = ""
            else:
                substr = int(elem)*substr
        else:
            substr = elem+substr
            #print("substr",substr)
    return res
print(decode("100[leetcode]"))
                
"""
Leet Code :DI String Match
Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.
Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:
If S[i] == "I", then A[i] < A[i+1]
If S[i] == "D", then A[i] > A[i+1]
"""
class Solution:
    def diStringMatch(self, S: str):
        lo, hi = 0, len(S)
        ans = []
        for x in S:
            if x == 'I':
                ans.append(lo)
                lo += 1
            else:
                ans.append(hi)
                hi -= 1
        return ans + [lo]

