'''
Your friend is typing his name into a keyboard.  Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.
You examine the typed characters of the keyboard.  Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

Example 1:
Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.

Example 2:
Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.

Example 3:
Input: name = "leelee", typed = "lleeelee"
Output: true

Example 4:
Input: name = "laiden", typed = "laiden"
Output: true
Explanation: It's not necessary to long press any character.
'''

#BF:

class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        if name is None and typed is None:
            return True
        if len(typed) < len(name):
            return False
        
        name = list(name)
        
        #First element not match
        if typed[0] != name.pop(0):
            return False
        
        for i in range(1, len(typed)):
            if name and typed[i] == typed[i - 1] and typed[i] != name[0]:
                continue
            
            if name:
                poped = name.pop(0)
                
            if typed[i] != poped:
                return False
            
        return not name
