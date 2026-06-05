class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack=[]

        def operate(operator,oper1,oper2):
            if operator=='+':
                return int(oper1)+int(oper2)
            elif operator=='-':
                return int(oper1)-int(oper2)
            elif operator=='*':
                return int(oper1)*int(oper2)
            elif operator=='/':
                if int(oper2)==0:
                    return 0
                else:
                    return int(oper1/oper2)
            else :
                return null
                
        for each_token in tokens:
            if each_token not in ["+",'-','*','/']:
                stack.append(int(each_token))
            else:
                oper1=stack.pop()
                oper2=stack.pop()
                stack.append(operate(each_token,oper2,oper1))
        return stack[-1]


        