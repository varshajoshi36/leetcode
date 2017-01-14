'''
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
'''

def swapPairs(self, head):
        if head is None:
                return None
                
        dummy = head
        head = dummy.next
        while dummy.next is not None:
                dummy2 = dummy.next
                dummy.next = dummy.next.next
                dummy2.next = dummy
                dummy = dummy.next
                
        return head
