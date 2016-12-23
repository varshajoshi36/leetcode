'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
'''

class MinStack(object):

    def __init__(self):
        self.stack = []
	self.minimum = []

    def push(self, x):
	self.stack.append(x)
	if len(self.minimum) is 0 or x <= self.getMin():
		self.minimum.append(x)
		

    def pop(self):
    	if len(self.stack) is None:
		return None
	pop = self.stack[len(self.stack) - 1]
        if pop is self.getMin():
                self.minimum.pop()
    
    def top(self):
    	if len(self.stack) is 0:
		return None
	return self.stack[len(self.stack) - 1]

    def getMin(self):
	if len(self.stack) == 0:
		return None

	return self.minimum[len(self.minimum) - 1]
