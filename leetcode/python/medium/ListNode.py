class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next_node = None

	def get_val(self):
	        return self.val

	def get_next(self):
	        return self.next_node

	def set_next(self, new_next):
		self.next_node = new_next

