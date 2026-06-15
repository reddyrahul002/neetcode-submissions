class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF           # 32 bit mask

        while b & mask:             # constrain b to 32 bits
            carry = (a & b) << 1
            a = a ^ b
            b = carry

        # handle negative result
        if b == 0:
            return a
        else:
            return ~(a ^ mask)      # convert back to python negative