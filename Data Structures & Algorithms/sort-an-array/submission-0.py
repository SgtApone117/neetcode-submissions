class Solution:
    def Merge(self,low,mid,high,nums):
        left = low
        right = mid+1
        temp = []
        while left <= mid and right <= high:
            if nums[left] <= nums[right]:
                temp.append(nums[left])
                left += 1
            else:
                temp.append(nums[right])
                right += 1
        
        while left <= mid:
            temp.append(nums[left])
            left += 1
        while right <= high:
            temp.append(nums[right])
            right += 1
        
        for i in range(low,high+1):
            nums[i] = temp[i-low]

    def MergeSort(self,low,high,nums):
        if low >= high:
            return
        mid = (low+high)//2
        self.MergeSort(low,mid,nums)
        self.MergeSort(mid+1,high,nums)
        self.Merge(low,mid,high,nums)
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        self.MergeSort(0,n-1,nums)
        return nums
        