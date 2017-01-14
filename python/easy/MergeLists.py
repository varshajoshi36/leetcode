'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
 :type l1: ListNode
 :type l2: ListNode
 :rtype: ListNode
'''

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
                return l2
        elif l2 is None:
                return l1
        if l1.val < l2.val:
                sorted_list = l1
                l1 = l1.next
        else:   
                sorted_list = l2
                l2 = l2.next
        
        head = sorted_list
        sorted_list.next = None
        
        while (l1 is not None) and (l2 is not None):
                if l1.val < l2.val:
                        sorted_list.next = l1
                        l1 = l1.next
                else:   
                        sorted_list.next = l2
                        l2 = l2.next
                sorted_list = sorted_list.next
                sorted_list.next = None

        if l1 is not None:
                sorted_list.next = l1
        elif l2 is not None:
                sorted_list.next = l2

        return head
