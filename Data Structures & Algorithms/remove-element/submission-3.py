class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0
        n = len(nums)
        for i in range(n):
            if nums[i] != val:
                nums[i],nums[idx] = nums[idx], nums[i]
                idx += 1
        return idx
            