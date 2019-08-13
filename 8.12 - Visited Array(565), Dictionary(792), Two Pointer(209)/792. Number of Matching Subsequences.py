'''
Given string S and a dictionary of words words, find the number of words[i] that is a subsequence of S.

Example :
Input: 
S = "abcde"
words = ["a", "bb", "acd", "ace"]
Output: 3
Explanation: There are three words in words that are a subsequence of S: "a", "acd", "ace".
'''

#Dictionary

from collections import defaultdict

class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        wordDict = defaultdict(list)
        count = 0
        
        for word in words:
            wordDict[word[0]].append(word)
        
        for c in S:
            curWordsChar = wordDict[c]
            wordDict[c] = []
            
            for w in curWordsChar:
                if len(w) == 1:
                    count += 1
                else:
                    wordDict[w[1]].append(w[1:])
            
        return count
