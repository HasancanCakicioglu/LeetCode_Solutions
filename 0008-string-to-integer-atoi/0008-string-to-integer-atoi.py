class Solution:
    def __init__(self) -> None:
        self.numbers = [str(i) for i in range(10)]
        self.minus=1
        self.startedI = 0

    
    def countNumbers(self,s:str) -> int:
        count=0
        for i in s:
            if i in self.numbers:
                count+=1
            else:
                break
        return count
        

    def myAtoi(self, s: str) -> int:

        minus = 0
        plus = 0
        
        s = s.strip()
        if not s:
            return 0
        sLen = len(s)

        count = 0
        for i,k in enumerate(s):

            if k != "-" and k not in self.numbers and k!="+" and k != " " and k != "_":
                return 0

            if k=="-":
                minus+=1
                if sLen > i+1 and  s[i+1] not in self.numbers:
                    return 0
            elif k=="+":
                plus+=1
                if sLen > i+1 and  s[i+1] not in self.numbers:
                    return 0
            
            if minus>0 and plus>0:
                return 0


            if k == "-" and sLen!= i+1 and s[i+1] in self.numbers:
                self.minus=-1
            elif self.minus==-1 and k not in self.numbers:
                self.minus=1
            
            
            if k in self.numbers:
                
                count = self.countNumbers(s[i:])
                self.startedI=i
                
                break
        
        number = 0
        us = count
        for i in range(self.startedI,self.startedI+count):
            us-=1
            number+=int(s[i])*10**us
            
        
        number = number*self.minus

        if number > 2**31-1:
            return 2**31-1
        elif number < -2**31:
            return -2**31


        return number