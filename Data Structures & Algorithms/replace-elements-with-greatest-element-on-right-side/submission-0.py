class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        my_list = [-1]
        last_largest_seen = arr[len(arr)-1]
        for i in range(len(arr)-2, -1, -1):
            my_list.append(last_largest_seen)
            last_largest_seen = max(arr[i], last_largest_seen)
            
        return my_list[::-1]