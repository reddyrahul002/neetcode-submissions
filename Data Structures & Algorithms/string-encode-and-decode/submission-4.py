class Solution:

    def encode(self, strs: List[str]) -> str:
        stng=""
        for i in strs:
            stng+='3#'+i
        return stng

    def decode(self, s: str) -> List[str]:
        sfi=[]
        for each_stng in s.split("3#"):
             sfi.append(each_stng)
        sfi.remove("")
        return sfi
