# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def merge(self, low, mid, high, pairs):
        left = low
        temp_list = []
        right = mid + 1
        while left <= mid and right <= high:
            if pairs[left].key <= pairs[right].key:
                temp_list.append(pairs[left])
                left += 1
            else:
                temp_list.append(pairs[right])
                right += 1
        while left <= mid:
            temp_list.append(pairs[left])
            left += 1
        while right <= high:
            temp_list.append(pairs[right])
            right += 1
        for i in range(low, high+1):
            pairs[i] = temp_list[i-low]

    def mergeSortAlgorithm(self,low,high, pairs):
        if low >= high:
            return
        mid = (low+high)//2
        self.mergeSortAlgorithm(low, mid, pairs)
        self.mergeSortAlgorithm(mid+1, high, pairs)
        self.merge(low,mid,high,pairs)

    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        n = len(pairs)
        self.mergeSortAlgorithm(0,n-1,pairs)
        return pairs
