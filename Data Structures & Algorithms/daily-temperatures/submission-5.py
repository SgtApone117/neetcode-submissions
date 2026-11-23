class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        res = [0] * n

        for day,temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                last_temp_day,last_temp_record = stack.pop()
                res[last_temp_day] = day - last_temp_day
            stack.append((day,temp))
        return res
        
        