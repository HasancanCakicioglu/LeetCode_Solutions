import math as math

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        sLen = len(nums)
        k =0

        for i in range(sLen):
            if nums[i] != val:
                nums[k] = nums[i]
                k+=1
        
        return k