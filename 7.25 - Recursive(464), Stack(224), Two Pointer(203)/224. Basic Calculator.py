'''
Implement a basic calculator to evaluate a simple expression string.
The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

Example 1:
Input: "1 + 1"
Output: 2

Example 2:
Input: " 2-1 + 2 "
Output: 3

Example 3:
Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23
'''

#Stack:

class Solution:
    def evaluate(self, stack):
        if stack:
            res = stack.pop()
        else:
            res = 0
        
        while stack and stack[-1] != ')':
            sign = stack.pop()
            
            if sign == '+':
                res += stack.pop()
            else:
                res -= stack.pop()
        
        return res
    
    def calculate(self, s: str) -> int:
        stack = []
        n = 0
        operand = 0
        
        for i in range(len(s) - 1, -1, -1):
            character = s[i]
            
            if character.isdigit():
                operand = (10 ** n * int(character)) + operand
                n += 1
            elif character != ' ':
                if n:
                    stack.append(operand)
                    n, operand = 0, 0
                
                if character == '(':
                    res = self.evaluate(stack)
                    stack.pop()
                    
                    stack.append(res)
                else:
                    stack.append(character)
        
        if n:
            stack.append(operand)
            
        return self.evaluate(stack)
