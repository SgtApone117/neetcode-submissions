class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        st = set()
        for i in range(n):
            if nums[i] in st:
                return True
            st.add(nums[i])
        return False