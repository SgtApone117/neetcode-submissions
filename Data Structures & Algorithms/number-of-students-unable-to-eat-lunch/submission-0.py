from collections import deque
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        q = deque(students)
        for sandwich in sandwiches:
            n = len(q)
            for _ in range(n):
                element = q.popleft()
                if element == sandwich:
                    break
                q.append(element)
            if n == len(q):
                return len(q)
        return len(q)