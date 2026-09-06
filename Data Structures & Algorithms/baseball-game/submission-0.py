class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result = []
        for ops in operations:
            if ops == "C":
                result.pop()
            elif ops == "D":
                element = result[-1]
                result.append(element*2)
            elif ops == "+":
                x = result[-1]
                y = result[-2]
                result.append(x+y)
            else:
                result.append(int(ops))
        return sum(result)
