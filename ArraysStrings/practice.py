class Solution:
    def containsNearbyDuplicate(self, nums: 'List[int]', k: 'int') -> 'bool':
        if len(nums) < k:
            return False
        dictduplicate = {}
        for i,items in enumerate(nums):
            if items in dictduplicate:
                print("1",dictduplicate)
                print("2",dictduplicate[items], i)
                if i - dictduplicate[items] <= k:
                    return True
            else:
                dictduplicate[items] = i
        print("3",dictduplicate)
        return False

    def myPow(self, x: 'float', n: 'int') -> 'float':

        neg = False
        pow = x

        if n == 0:
            return 1
        if n < 0:
            n = 0 - n
            neg = True
        n = n-1
        while True:
            if n ==0 :
                break
            pow = pow*x
            n = n-1
        if neg == True:
            return 1/pow
        else:
            return pow


    def wordBreak(self, s: 'str', wordDict: 'List[str]') -> 'bool':
        wordDict = set(wordDict)
        print(set(wordDict))
        state = [False for _ in range(len(s)+1)]
        state[0] = True
        for i in range(len(s)+1):
            print(i)
            for j in range(i):
                print("j",j)
                if not state[j]:
                    continue
                if s[j:i] in wordDict:
                    print(s[j:i])
                    state[i] = True
        print(state)
        return state[-1]


obj = Solution()


input = [1,2,3,1,2,3]
k =2
print(obj.containsNearbyDuplicate(input,k))
#print(obj.containsNearbyDuplicate(input,k))
#print(obj.myPow(8.95371,-1))

#print(obj.wordBreak("applepenapple",["apple","pen"]))
