'''
Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5
'''

class RemoveElements(object):
	def removeElements(self, head, val):
		if head is None:
			return None

		head.next = self.removeElements(head.next, val)
		return head.val == val ? head.next : head


