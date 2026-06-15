class Solution:
    def reverse(self, x: int) -> int:
        MIN, MAX = -2**31, 2**31 - 1

        sign = -1 if x < 0 else 1
        res = sign * int(str(abs(x))[::-1])   # abs handles negative, sign restores it

        return 0 if res < MIN or res > MAX else res