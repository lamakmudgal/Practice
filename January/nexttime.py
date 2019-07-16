class Solution:
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        digits = set(digit for digit in time.replace(":", ""))
        print(digits)
        hour, minute = time.split(":")
        print(hour,minute)
        while True:
            # Increment by one minute + handle minute 59 overflow
            if minute == '59':
                hour = str(int(hour) + 1)
                minute = '00'
            else:
                minute = str(int(minute) + 1)

            # Fix hour overflow 23 -> 00 if needed
            if int(hour) > 23:
                hour = '00'

            # Fill digits with zero if needed
            if len(hour) == 1:
                hour = '0' + hour
            if len(minute) == 1:
                minute = '0' + minute

            if all(x in digits for x in hour + minute):
                return hour + ':' + minute

if __name__ == '__main__':
    obj_sol = Solution()
    print(obj_sol.nextClosestTime("23:59"))