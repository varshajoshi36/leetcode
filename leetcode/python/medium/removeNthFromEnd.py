"""
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.

"""

def removeNthFromEnd(head, n):
	initial = head
	for i in range(n):
		initial = initial.next
	
	if initial is None:
		return head

	if initial is None:
		return head.next
	
	follow = head
	while initial.next.next is not None:
		initial = initial.next
		follow = follow.next

	follow.next = follow.next.next

	return head
