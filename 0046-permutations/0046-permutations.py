class Solution:

    def permutasyon(self,per):
        sum=1
        for i in per:
            sum*=i
        return sum
    
    def isExistEqual(self,eqList:list[int]):

        for i in range(len(eqList)):
            for k in range(len(eqList)):
                if i!=k and eqList[i]==eqList[k]:
                    return True

        return False


    def permute(self, nums: list[int]) -> list[list[int]]:
        newList = []
        
        
         
        nLen= len(nums)
        numberOfOutput = self.permutasyon(nums)
        countP = numberOfOutput / nLen


        
        for f in nums:
            if self.isExistEqual([f]) is False and 1 == nLen:
                                    newList.append([f])
            for s in nums:
                if self.isExistEqual([f,s]) is False and 2 == nLen:
                                    newList.append([f,s])
                for t in nums:
                    if self.isExistEqual([f,s,t]) is False and 3 == nLen:
                                    newList.append([f,s,t])
                    for fo in nums:
                        if self.isExistEqual([f,s,t,fo]) is False and 4 == nLen:
                                    newList.append([f,s,t,fo])
                        for fi in nums:
                            if self.isExistEqual([f,s,t,fo,fi]) is False and 5 == nLen:
                                    newList.append([f,s,t,fo,fi])
                            for si in nums:
                                if self.isExistEqual([f,s,t,fo,fi,si]) is False and 6 == nLen:
                                    newList.append([f,s,t,fo,fi,si])
                    
        
        print(newList)
        return newList