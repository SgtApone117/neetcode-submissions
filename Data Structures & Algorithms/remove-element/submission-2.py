class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        my_list = []
        for num in nums:
            if val != num:
                my_list.append(num)
        i = 0
        for num in my_list:
            nums[i] = num
            i += 1
        return i
            