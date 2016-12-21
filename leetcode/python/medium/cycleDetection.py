import ListNode from ../medium/ListNode

'''
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?'''

class DetectCycle(object):
	def hasCycle(head):
		if head is None or head.next is None or head.next.next is None:
                        return None
                tortoise = head.next
                hare = head.next.next

                while tortoise is not hare:
                        if hare.next is None or hare.next.next is None:
                            return None
                        tortoise = tortoise.next
                        hare = hare.next.next

                tortoise = head
                
                while tortoise is not hare:
                        tortoise = tortoise.next
                        hare = hare.next

                return tortoise
