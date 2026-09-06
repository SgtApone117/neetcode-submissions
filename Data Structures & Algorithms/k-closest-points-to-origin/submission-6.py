class Solution:
    def dist(self,x,y):
        return x * x + y * y
        
    def PartitionIndex(self, low, high, points):
        pivot = points[high]
        pivot_dist = self.dist(points[high][0], points[high][1])
        idx = low-1
        for i in range(low,high):
            if self.dist(points[i][0], points[i][1]) <= pivot_dist:
                idx += 1
                points[i],points[idx] = points[idx],points[i]
        idx += 1
        points[high],points[idx] = points[idx],points[high]
        return idx
            
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
        
