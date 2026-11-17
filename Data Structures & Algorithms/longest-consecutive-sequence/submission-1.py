class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        st = set(nums)
        longest_sequence = 0
        for i in range(n):
            if nums[i]-1 not in st:
                current_element = nums[i]
                count = 1
                while current_element + 1 in st:
                    count += 1
                    current_element += 1
                longest_sequence = max(longest_sequence, count)
        return longest_sequence