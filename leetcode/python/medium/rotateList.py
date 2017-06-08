"""
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def rotateRight(self, head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    pointer = head
    length = 0
    while pointer.next is not None:
        if pointer.next.next is None:
            last = pointer.next
        pointer = pointer.next
        length += 1

    k = k % length
    if k == 0:
        return head

    pointer = head
    for i in range(length - k - 1):
        pointer = pointer.next

    new_head = pointer.next
    pointer.next = None
    last.next = head
    head = new_head
    

