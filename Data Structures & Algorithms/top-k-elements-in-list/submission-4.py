class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        present={}
        frequent=[]

        for i in nums:
            if i in present.keys():
                present[i]+=1
            else:
                present[i]=1
        present= sorted(present.items(), key=lambda item: item[1], reverse=True)[:k]
        return [key[0] for key in present]
          

        