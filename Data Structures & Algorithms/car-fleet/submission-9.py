class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_speed_sorted = sorted(zip(position, speed), key= lambda x: x[0], reverse=True)
        # print(position_speed_sorted)
        fleets = 0
        curr_prev = 0
        for car in position_speed_sorted:
            dist_cal = (target - car[0]) / car[1]
            if curr_prev < dist_cal:
                fleets += 1
                curr_prev = dist_cal
        return fleets