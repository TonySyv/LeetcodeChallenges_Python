class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        n = len(s)
        sign = 1
        result = 0
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # 1. Ignore leading whitespace
        while i < n and s[i] == ' ':
            i += 1

        # 2. Check sign
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1

        # 3. Convert digits
        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord('0')

            # 4. Handle overflow before it happens
            if result > INT_MAX // 10 or (result == INT_MAX // 10 and digit > 7):
                return INT_MAX if sign == 1 else INT_MIN

            result = result * 10 + digit
            i += 1

        return sign * result
