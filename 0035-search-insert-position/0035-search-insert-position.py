class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        
        index=0
        lNum = len(nums)

        for i in range(lNum):
            if target>nums[i]:
                index+=1



        return index