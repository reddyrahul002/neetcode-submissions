class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group={}

        for s in strs:
            count =[0]*26
            for i in range(len(s)):
                count[ord(s[i])-ord('a')]+= 1

            key = tuple(count)
            
            if key in group.keys():
                group[key].append(s)
            else:
                group[key]=[s]
        return list(group.values())


