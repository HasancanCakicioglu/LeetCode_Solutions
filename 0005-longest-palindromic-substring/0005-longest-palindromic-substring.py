class Solution:
    def longestPalindrome(self, s: str) -> str:
        sLen = len(s)

        for i in range(sLen,0,-1):
            for j in range(sLen-i+1):
                if s[j:j+i+1] == s[j:j+i+1][::-1]:
                    return s[j:j+i+1]