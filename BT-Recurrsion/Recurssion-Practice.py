class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        return self.isInterleaveRecur(s1, 0, s2, 0, "", s3)

    def isInterleaveRecur(self, s1, i, s2, j, res, s3):
        print("result is",res,i,j)
        if res == s3 and i == len(s1) and j == len(s2):
            print("Sucess",res)
            return True
        ans = False
        if i < len(s1):
            ans |= self.isInterleaveRecur(s1, i + 1, s2, j, res + s1[i], s3)
            print("after return s1",res,i,j)
        if j < len(s2):
            ans |= self.isInterleaveRecur(s1, i, s2, j + 1, res + s2[j], s3)
            print("after return s2", res, i, j)
        return ans


obj = Solution()
print(obj.isInterleave("ab", "cd", "acdb"))
