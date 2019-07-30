'''
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:
Input: 1->2->3->3->4->4->5
Output: 1->2->5

Example 2:
Input: 1->1->1->2->3
Output: 2->3
'''

#BF:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        res = ListNode(0)
        res.next = head
        
        temp = res
        
        while temp.next and temp.next.next:
            if temp.next.val == temp.next.next.val:
                val = temp.next.val
                
                while temp.next and temp.next.val == val:
                    temp.next = temp.next.next
            else:
                temp = temp.next
                
        return res.next
