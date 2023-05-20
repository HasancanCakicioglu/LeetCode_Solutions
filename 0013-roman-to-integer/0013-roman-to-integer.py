class Solution:
    def __init__(self) -> None:
        self.map = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }
    
    def bigger(self,s:str,i:int) -> bool:
        
        for c,k in enumerate(s):
            if c<i:
                continue
            if self.map[k] > self.map[s[i]]:
                return True
        return False


    def romanToInt(self, s: str) -> int:
        sLen = len(s)
        sum =0
        for i,k in enumerate(s):
            if self.bigger(s,i):
                sum -= self.map[k]
            else:
                sum += self.map[k]
        
        return sum