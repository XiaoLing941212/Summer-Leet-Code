'''
Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.

We repeatedly make duplicate removals on S until we no longer can.

Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.

Example 1:

Input: "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca". 

Note:

1 <= S.length <= 20000
S consists only of English lowercase letters.
'''

#Stack Data Structure
class Solution:
    def removeDuplicates(self, S: str) -> str:
        #Using stack
        strStack = [S[0]]
        
        for i in range(1, len(S)):
            if strStack == []:
                strStack.append(S[i])
            else:
                topValue = strStack.pop()
                if S[i] == topValue:
                    continue
                else:
                    strStack.append(topValue)
                    strStack.append(S[i])
        
        if strStack == []:
            return ""
        else:
            returnStr = str(strStack[0])
            
            for i in range(1, len(strStack)):
                returnStr = returnStr + str(strStack[i])
            
            return returnStr
