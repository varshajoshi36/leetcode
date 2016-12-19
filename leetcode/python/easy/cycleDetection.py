import ListNode from ../medium/ListNode

class DetectCycle(object):
	def hasCycle(head):
		if head is None:
			return False
		tortoise = head
		hare = head

		while hare.next is not None and hare.next.next is not None:
			tortoise = tortoise.next
			hare = hare.next.next
			if tortoise == hare:
				return True

		return False
