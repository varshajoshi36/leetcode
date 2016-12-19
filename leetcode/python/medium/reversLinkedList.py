#! /usr/bin/python

'''
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.

'''

class ReverseLinkedList(object):
	def reverseLinkedList(head, m, n):
		if head is None:
			return head
		start_node = head
		for i in range(m - 1):
			start_node = start_node.next
		
		last_node = start_node
		for i in range(m - n):
			last_node = end_node.next

		prev_node = last_node.next
		next_node = None
		curr_node = start_node.next

		while curr_node != last_node.next:
			next_node = curr_node.next
			curr_node.next = prev_node
			prev_node = curr_node
			curr_node = next_node

		start_node.next = prev_node

		return head
