class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        max_element = max(nums) + 1
        # print(max_element)
        count_arr = [0] * max_element
        # print(count_arr)
        for num in nums:
            count_arr[num] += 1
        # print(count_arr)
        
        i = j = 0
        while i < len(count_arr):
            if count_arr[i] != 0:
                nums[j] = i
                count_arr[i] -= 1
                j += 1
            else:
                i += 1
        return nums