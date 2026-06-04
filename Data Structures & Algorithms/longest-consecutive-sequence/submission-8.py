class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        check = set(nums)
        largest =0

        for i in nums:
            if i-1  not in check:
                length=0
                while i+length in check:
                    length+=1

                largest =max(largest,length)
        
        return largest
            


            
       


    

        