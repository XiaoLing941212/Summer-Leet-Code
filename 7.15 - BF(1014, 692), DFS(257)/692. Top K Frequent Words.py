'''
Given a non-empty list of words, return the k most frequent elements.
Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1:
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.

Example 2:
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.

Note:
1. You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
2. Input words contain only lowercase letters.

Follow up:
1. Try to solve it in O(n log k) time and O(n) extra space.
'''

#BF: (Use Counter)

from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wordDict = dict(Counter(words))
        sortedWord = sorted(wordDict.items(), key = lambda kv : (-kv[1], kv[0]))
        
        res = []
        count = 0
        for i in range(len(sortedWord)):
            print(sortedWord[i][0])
            res.append(sortedWord[i][0])
            
            if i == k-1:
                break
        
        return res
