class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_pos_speed = sorted(zip(position,speed),reverse=True)
        # print(car_pos_speed)
        time_taken = [(target - pos) / speed for pos,speed in car_pos_speed]
        # print(time_taken)
        fleets = []
        for time in time_taken:
            if not fleets:
                fleets.append(time)
            elif fleets[-1] < time:
                fleets.append(time)
        return len(fleets)