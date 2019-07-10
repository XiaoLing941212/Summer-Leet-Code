'''
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
'''

#Two pointer

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if head == None or head.next == None:
            return head
        
        #initial 2 iteration, put value smaller than x in iter1 and o.w. in iter2
        #need head1 for output
        #need head2 for connection with iter1
        head1 = iter1 = ListNode(0)
        head2 = iter2 = ListNode(0)
        
        while head != None:
            if head.val < x:
                iter1.next = head
                iter1 = iter1.next
            else:
                iter2.next = head
                iter2 = iter2.next
            
            head = head.next
        
        #iter1 before iter2
        iter1.next = head2.next
        iter2.next = None
        
        return head1.next
        
