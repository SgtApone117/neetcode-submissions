class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        x = 0
        for idx in range(len(nums)):
            if nums[idx] != 0:
                nums[idx],nums[x] = nums[x], nums[idx]
                x += 1
                
        print(nums)
        return nums
        

        