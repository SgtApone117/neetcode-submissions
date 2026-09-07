class Solution:
    def solve(self, nums: List[int], low: int, high: int, target: int) -> int:
        if low <= high:   
            mid = (low+high)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return self.solve(nums,mid+1, high, target)
            else:
                return self.solve(nums,low,mid-1, target)
        return -1


    def search(self, nums: List[int], target: int) -> int:
        return self.solve(nums,0, len(nums)-1, target)