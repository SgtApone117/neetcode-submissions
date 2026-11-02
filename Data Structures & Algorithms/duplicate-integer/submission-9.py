class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        st = set()
        n = len(nums)
        for num in nums:
            if num in st:
                return True
            st.add(num)
        return False