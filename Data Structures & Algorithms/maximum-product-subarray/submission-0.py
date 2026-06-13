class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        result = nums[0]
        cur_max = cur_min = nums[0]

        for i in nums[1:]:

            candi = (i,cur_max*i,cur_min*i)
            cur_max = max(candi)
            cur_min = min(candi)
            result=max(result,cur_max)
        return result

        
        