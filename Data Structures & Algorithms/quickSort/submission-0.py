# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def Partition(self, pairs: List[Pair], low: int, high: int) -> int:
        pivot = pairs[high].key
        left = low - 1
        for j in range(low, high):
            if pairs[j].key < pivot:
                left += 1
                pairs[left],pairs[j] = pairs[j],pairs[left]
        pairs[left + 1], pairs[high] = pairs[high], pairs[left + 1]
        return left + 1
    def QuickSort(self, pairs: List[Pair], low: int, high: int) -> None:
        if low >= high:
            return
        partition_index = self.Partition(pairs,low,high)
        self.QuickSort(pairs,low, partition_index-1)
        self.QuickSort(pairs,partition_index+1, high)
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.QuickSort(pairs,0, len(pairs)-1)
        return pairs
        