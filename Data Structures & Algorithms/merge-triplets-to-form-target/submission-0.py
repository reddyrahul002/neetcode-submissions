class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        result=[0,0,0]


        for triplet in triplets:

            if triplet[0]> target[0] or triplet[1]> target[1] or triplet[2]> target[2]:
                continue
            
            result[0]=max(result[0],triplet[0])
            result[1]=max(result[1],triplet[1])
            result[2]=max(result[2],triplet[2])

        return result == target
            


        