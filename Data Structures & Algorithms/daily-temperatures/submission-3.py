class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = n * [0]
        last_recorded_temperature = []
        for idx,temp in enumerate(temperatures):
            while last_recorded_temperature and temp > last_recorded_temperature[-1][1]:
                last_temperture_idx, last_temp_record = last_recorded_temperature.pop()
                res[last_temperture_idx] = idx - last_temperture_idx
            last_recorded_temperature.append((idx,temp))
        return res