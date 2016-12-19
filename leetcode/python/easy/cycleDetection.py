import ListNode from ../medium/ListNode

class DetectCycle(object):
	def hasCycle(head):
		if head is None:
			return False
		tortoise = head
		hare = head.next

		while tortoise != hare:
			if tortoise.next is None or hare.next is None:
				return False
			elif hare.next.next is None:
				return False
			tortoise = tortoise.next
			hare = hare.next.next

		return True
