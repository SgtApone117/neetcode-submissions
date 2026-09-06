class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        last_seen_idx = 0
        for idx,value in enumerate(nums):
            if value != val:
                nums[last_seen_idx] = nums[idx]
                last_seen_idx += 1

        return last_seen_idx
            