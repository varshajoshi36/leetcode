
'''
Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5
'''


class RemoveElements(object):
	def remove_elements(self, head, val):
		while head is not None and head.val is val:
			head = head.next
		
		if head is None:
			return None

		node = head
		while node is not None and node.next != None:
			while node.next is not None and node.next.val is val:
				node.next = node.next.next
                        node = node.next
		
		return head
