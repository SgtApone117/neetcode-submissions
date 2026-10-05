class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hmp = set()
        for num in nums:
            if num in hmp:
                return True
            hmp.add(num)
        # print(res)
        return False


