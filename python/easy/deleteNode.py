import ListNode from ../medium/ListNode

'''
Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node with value 3, the linked list should become 1 -> 2 -> 4 after calling your function.
'''


class DeleteNode(object):
	def deleteNode(self, node):
		while node.next is not None:
			while node.next is not None:
                        	if node.next.next is None:
                                	node.val = node.next.val
	                                node.next = None
        	                else:
                	                node.val = node.next.val
                        	        node = node.next
