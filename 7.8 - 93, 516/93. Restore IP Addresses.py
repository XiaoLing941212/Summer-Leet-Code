'''
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
'''

#BackTrack method
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        
        def getSubAddress(curIP, s, lvl):
            if lvl == 0 and s == "":
                result.append(curIP[:-1])
            elif lvl != 0:
                for i in range(0, min(3, len(s))):
                    if i > 0 and s[0] == "0":
                        continue
                    if 0 <= int(s[0:i+1]) <= 255:
                        getSubAddress(curIP + s[0:i+1] + ".", s[i+1:], lvl-1)
                        
        lvl = 4
        getSubAddress("", s, lvl)
        
        return result
