class DynamicArray:
    
    def __init__(self, capacity: int):
        self.my_list = [-1] * capacity
        self.total_elements = 0
        self.size = capacity

    def get(self, i: int) -> int:
        return self.my_list[i]

    def set(self, i: int, n: int) -> None:
        self.my_list[i] = n

    def pushback(self, n: int) -> None:
        if self.total_elements == self.size:
            self.resize()
        self.my_list[self.total_elements] = n
        self.total_elements += 1

    def popback(self) -> int:
        self.total_elements -= 1
        element = self.my_list[self.total_elements]
        self.my_list[self.total_elements] = -1
        return element

    def resize(self) -> None:
        total_capacity = 2 * self.size
        add_to_list = [-1] * total_capacity
        self.my_list.extend(add_to_list)
        self.size *= 2

    def getSize(self) -> int:
        return self.total_elements
    
    def getCapacity(self) -> int:
        return self.size
