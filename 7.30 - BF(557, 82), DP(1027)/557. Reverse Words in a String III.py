'''
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
'''

#BF:

class Solution:
    def reverseWords(self, s: str) -> str:
        strList = s.split(" ")
        
        for i in range(len(strList)):
            strList[i] = list(strList[i])
            strList[i].reverse()
            strList[i] = "".join(strList[i])
        
        strList = " ".join(strList)    
        return strList
