class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        my_result = [0] * n

        for idx,temperature in enumerate(temperatures):
            if not stack:
                stack.append((temperature, idx))
                continue
            while stack and temperature > stack[-1][0]:
                last_temperature_detail = stack.pop()
                last_temperature = last_temperature_detail[0]
                last_idx = last_temperature_detail[1]
                my_result[last_idx] = idx - last_idx
            stack.append((temperature,idx))
        return my_result
