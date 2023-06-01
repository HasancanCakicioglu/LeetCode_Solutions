class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        
        myStr = ""
        sumStr=""
        for i in range(len(strs[0])):
            myStr=strs[0][i]
            for j in strs:
                if len(j)>i and  j[i] == myStr:
                    pass
                else:
                    return sumStr
            sumStr+=myStr
        
        return sumStr