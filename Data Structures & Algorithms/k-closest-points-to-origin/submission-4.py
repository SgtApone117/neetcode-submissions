class Solution:
    def dist(self,x,y):
        return x * x + y * y
    def PartitionIndex(self, low, high, points):
        pivot = points[low]
        pivot_dist = self.dist(points[low][0], points[low][1])
        i = low + 1
        j = high

        while i <= j:
            while i <= j and self.dist(points[i][0], points[i][1]) <= pivot_dist:
                i += 1

            while i <= j and self.dist(points[j][0], points[j][1]) > pivot_dist:
                j -= 1
            if i < j:
                points[i],points[j] = points[j],points[i]
                i += 1
                j -= 1
        points[low],points[j] = points[j],points[low]
        return j
            
    def QuickSort(self, low, high, points, k):
        if low >= high:
            return
        partition_index = self.PartitionIndex(low,high,points)
        if partition_index == k-1:
            return
        if partition_index > k-1:
            self.QuickSort(low, partition_index-1,points,k)
        else:
            self.QuickSort(partition_index+1,high,points,k)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        n = len(points)
        self.QuickSort(0, n-1,points,k)
        return points[:k]
        
