import math

class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        
        y = x
        bas = []
        while y >= 1:
            bas.append(y % 10)
            y = y // 10
        
        number = 0
        for i in range(len(bas)):
            number = number + bas[i] * math.pow(10, len(bas) - i - 1)
        
        print(number)
        print(x)
        
        if number == x:
            return True
        else:
            return False
