import ListNode

class LinkedListAddition(object):

	def __init__(self, x):
		self.x = x
		print "Created Object"	
		l11 = ListNode.ListNode(1)
		l12 = ListNode.ListNode(2)
		l11.next_node = l12
		l21 = ListNode.ListNode(5)
		l22 = ListNode.ListNode(6)
		l21.next_node = l22
		l3 = self.addTwoNumbers(l11, l21)
		print 'l3 val in init',l3.val
		while (l3.next_node != None):
			print 'l3 val in init',l3.next_node.val
			l3 = l3.next_node
		#self.addTwoNumbers(l1, l2)		
	
	def addTwoNumbers(self, l1, l2):
		numbers = []
		for l in (l1, l2):
			tens = 1
			no = 0
			no = no + (l.val * tens)
                        tens = tens * 10
			while(l.next_node != None):
				no = no + l.next_node.val * tens
				tens = tens * 10
				l = l.next_node
			numbers.append(no)

		l_sum = numbers[0] + numbers[1]
		first_val = l_sum % 10
		l_sum = l_sum/10
		l3 = ListNode.ListNode(first_val)
		head = l3
		while(l_sum > 0):
			val = l_sum % 10
			l_sum = l_sum/10
			l_node = ListNode.ListNode(val)
			l3.next_node = l_node
			l3 = l3.next_node
			
		return head


