class Solution:
    def NextSmallestElement(self, arr: List[int], n: int) -> int:
        res = [0] * n
        stack = []

        for i in range(n-1,-1,-1):
            while stack and arr[i] <= arr[stack[-1]]:
                stack.pop()
            res[i] = stack[-1] if stack else n
            stack.append(i)
        return res

    def PreviousSmallestElement(self, arr: List[int], n: int) -> int:
        res = [0] * n
        stack = []

        for i in range(n):
            while stack and arr[i] <= arr[stack[-1]]:
                stack.pop()
            res[i] = stack[-1] if stack else -1
            stack.append(i)
        return res

    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        nse = self.NextSmallestElement(heights, n)
        pse = self.PreviousSmallestElement(heights, n)

        # print(nse)
        # print(pse)

        max_area = 0
        for i in range(n):
            max_area = max(max_area, heights[i] * (nse[i] - pse[i] - 1))
        return max_area
