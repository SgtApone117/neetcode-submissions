class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        new_number = 0
        while temp > 0:
            rem = temp % 10
            new_number = new_number *10 + rem
            temp //= 10
        return new_number == x