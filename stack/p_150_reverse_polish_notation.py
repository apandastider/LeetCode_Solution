'''
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.
'''

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        ans = 0
        stack = []
        
        for c in tokens:
            if c!="+" and c!="-" and c!="/" and c!="*":
                stack.append(int(c))
            if c == "+":
                stack.append(stack.pop(-2)+stack.pop(-1))
            if c == "*":
                stack.append(stack.pop(-2)*stack.pop(-1))
            if c == "-":
                stack.append(stack.pop(-2)-stack.pop(-1))
            if c == "/":
                div = int(stack.pop(-2)/stack.pop(-1))                
                stack.append(div)
        return stack[0]
