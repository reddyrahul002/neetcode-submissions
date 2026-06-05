class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False
        closing = {')':'(','}':'{',']':'['}
        stack=[]
        for stng in s:
            if stng in closing:
                if len(stack)==0 or stack.pop() !=closing[stng]:
                    return False
            else:
                stack.append(stng)
        return len(stack)==0

