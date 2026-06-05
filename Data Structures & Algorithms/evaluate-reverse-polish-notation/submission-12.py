class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack=[]

        def operate(operator,oper1,oper2):
            if operator=='+': return int(oper1)+int(oper2)
            if operator=='-': return int(oper1)-int(oper2)
            if operator=='*': return int(oper1)*int(oper2)
            if operator=='/': return int(oper1/oper2)

                
        for each_token in tokens:
            if each_token not in ["+",'-','*','/']:
                stack.append(int(each_token))
            else:
                oper1=stack.pop()
                oper2=stack.pop()
                stack.append(operate(each_token,oper2,oper1))
        return stack[-1]


        