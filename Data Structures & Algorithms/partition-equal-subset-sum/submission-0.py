class Solution:
    def canPartition(self, nums):
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2

        possible_sums = {0}                 # with no numbers used, sum=0 is possible
        for num in nums:
            new_sums = set()
            for s in possible_sums:
                new_sums.add(s)              # skip num — keep old sum
                new_sums.add(s + num)        # take num — add to old sum
            possible_sums = new_sums

            if target in possible_sums:      # early exit if found
                return True

        return target in possible_sums