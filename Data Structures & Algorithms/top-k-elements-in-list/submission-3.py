class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        present={}
        frequent=[]

        for i in nums:
            if i in present.keys():
                present[i]+=1
            else:
                present[i]=1
        i=0;
        while i<k:

            frequent.append(sorted(present.items(), key=lambda item: item[1], reverse=True)[i][0])
            i+=1
        return frequent

        