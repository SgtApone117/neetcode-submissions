class Solution:
    def dist(self,point):
        return point[0] * point[0] + point[1] * point[1]
    def Partition(self, points: List[List[int]], low: int, high: int) -> int:
        pivot_dist = self.dist(points[low])
        i = low + 1
        j = high
        while i <= j:

            while i <= j and self.dist(points[i]) <= pivot_dist:
                i += 1
            while i <= j and self.dist(points[j]) > pivot_dist:
                j -= 1
            if i < j:
                points[i],points[j] = points[j],points[i]
        points[low],points[j] = points[j],points[low]
        return j
    def QuickSort(self, points: List[List[int]], low: int, high: int) -> None:
        if low >= high:
            return
        partition_index = self.Partition(points, low, high)
        self.QuickSort(points,low,partition_index-1)
        self.QuickSort(points,partition_index+1, high)
        
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.QuickSort(points,0, len(points) - 1)
        return points[:k]
        