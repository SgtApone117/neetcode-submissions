class Solution:
    # sub-optimal brute force
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix_max = [0]*n
        prefix_max[0] = height[0]
        for i in range(1,n):
            prefix_max[i] = max(prefix_max[i-1],height[i])
        
        suffix_max = [0]*n
        suffix_max[n-1] = height[n-1]
        for i in range(n-2,-1,-1):
            suffix_max[i] = max(suffix_max[i+1],height[i])
        total = 0
        for i in range(n):
            left_max = prefix_max[i]
            right_max = suffix_max[i]

            if height[i] < left_max and height[i] < right_max:
                total += min(left_max,right_max) - height[i]
        return total

        