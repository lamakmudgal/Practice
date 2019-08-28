class Solution:
    def existsLargerDigit(self, cur_digit, sorted_digits, max_digit_value):
        """
        Returns digit in digits that is larger than cur_digit but less than or
        equal to max_digit_value
        Returns -1 if this cannot be satisfied
        """
        for digit in sorted_digits:
            if cur_digit < digit <= max_digit_value:
                return digit
        return -1

    def formatTimeString(self, digits):
        return str(digits[0]) + str(digits[1]) + ":" + str(digits[2]) + str(digits[3])

    def setDigitsAfter(self, digits, idx, new_digit):
        for i in range(idx + 1, len(digits)):
            digits[i] = new_digit

    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """

        digits = []

        for char in time:
            if char != ":":
                digits.append(int(char))

        sorted_digits = sorted(digits)

        print(time)
        print(digits)
        print(sorted_digits)

        # __:_M, any will do, i.e. has to be <= 9
        new_digit = self.existsLargerDigit(digits[3], sorted_digits, 9)
        print(new_digit)
        if new_digit >= 0:
            digits[3] = new_digit
            return self.formatTimeString(digits)

        # __:M_, has to be <= 5
        new_digit = self.existsLargerDigit(digits[2], sorted_digits, 5)
        if new_digit >= 0:
            digits[2] = new_digit
            self.setDigitsAfter(digits, 2, sorted_digits[0])
            return self.formatTimeString(digits)

        # xH:__, if x is 0 or 1, H has to be <= 9
        #        if x is 2, has to be <= 4
        if digits[0] == 0 or digits[0] == 1:
            new_digit = self.existsLargerDigit(digits[1], sorted_digits, 9)
        else:
            new_digit = self.existsLargerDigit(digits[1], sorted_digits, 4)
        if new_digit >= 0:
            digits[1] = new_digit
            self.setDigitsAfter(digits, 1, sorted_digits[0])
            return self.formatTimeString(digits)

        # H_:__, has to be <= 2
        new_digit = self.existsLargerDigit(digits[0], sorted_digits, 2)
        if new_digit >= 0:
            digits[0] = new_digit
            self.setDigitsAfter(digits, 0, sorted_digits[0])
            return self.formatTimeString(digits)

        # If all of these fail
        self.setDigitsAfter(digits, -1, sorted_digits[0])
        return self.formatTimeString(digits)

if __name__ == '__main__':
    obj_sol = Solution()
    print(obj_sol.nextClosestTime("23:54"))