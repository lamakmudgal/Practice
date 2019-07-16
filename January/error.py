class Solution:
    def fractionToDecimal(self, numerator: 'int', denominator: 'int') -> 'str':
        if denominator == 0:
            return ValueError
        if numerator == 0:
            return 0

        output = numerator / denominator
        listfraction = str(output).split(".")
        print(output,listfraction[-1])

ojSol = Solution()
ojSol.fractionToDecimal(5,7)
