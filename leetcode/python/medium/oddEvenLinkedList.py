'''
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example:
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.

Note:
The relative order inside both the even and odd groups should remain as it was in the input. 
The first node is considered odd, the second node even and so on ...
'''

class OddEvenLinkedList(object):
	def oddEvenList(self, head):
		if head is None or head.next is None or head.next.next is None:
			return head

		tortoise = head
		hare = head.next.next
		even_end = tortoise.next
		while hare is not None:
			even_start = tortoise.next
			tortoise.next = hare
			even_end.next = hare.next
			odd_last = hare
			if hare.next is not None:
				hare = hare.next.next
			else:
				hare = hare.next
			odd_last.next = even_start
			tortoise = tortoise.next
			even = even.next

		return head

