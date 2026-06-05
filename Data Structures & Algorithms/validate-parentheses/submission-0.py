class Solution:
    def isValid(self, s: str) -> bool:
        closing = {')':'(','}':'{',']':'['}
        stack=[]
        for stng in s:
            if stng in closing:
                if not stack or stack.pop() !=closing[stng]:
                    return False
            else:
                stack.append(stng)
        return not stack

