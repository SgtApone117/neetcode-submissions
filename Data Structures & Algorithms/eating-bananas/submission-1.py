class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        get_max_pile = max(piles)
        low = 1
        high = get_max_pile
        while low <= high:
            speed = (low + high) // 2
            hours = 0
            for pile in piles:
                hours += ((pile + speed - 1) // speed)
            if hours <= h:
                high = speed - 1
            else:
                low = speed  + 1
        return low