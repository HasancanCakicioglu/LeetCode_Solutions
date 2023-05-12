class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        
        n = len(nums)
        if n == 0 or n == 1: 
            return n

        
        i = 0
        for j in range(1, n):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        return i + 1