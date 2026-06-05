class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        out = [0]*len(temperatures)
        stack=[]

        for day,temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                index,temp1 = stack.pop()
                out[index]=day-index
            stack.append([day,temp])
        return out