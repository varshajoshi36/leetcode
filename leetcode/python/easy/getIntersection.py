
'''
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
'''

class IntersectionNode(object):
	def getIntersectionNode(self, headA, headB):
		if headA is None or headB is None:
			return None	
		nodeA = headA
		lenA = 0
		while nodeA is not None:
			nodeA = nodeA.next
			lenA += 1

		nodeB = headB
		lenB = 0
		while nodeB is not None:
			nodeB = nodeB.next
			lenB += 1
		
		if lenA < lenB:
			node_short = headA
			node_long = headB
		else:
			node_short = headB
			node_long = headA

		for i in range(abs(lenA - lenB)):
			node_long = node_long.next


		while node_long is not None:
			if node_long is not None and node_long is node_short:
				return node_long
			node_long = node_long.next
			node_short = node_short.next

		return None
