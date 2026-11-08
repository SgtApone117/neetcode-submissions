class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        print(k)
        print(n)
        def reverse(start,end):
            left = start
            right = end - 1
            while left < right:
                # print(nums[i], nums[end-start-i])
                nums[left],nums[right] = nums[right],nums[left]
                left += 1
                right -= 1
            
        reverse(0,n-k)
        print(nums)
        reverse(n-k,n)
        print(nums)
        reverse(0,n)
        print(nums)


        