#! /usr/bin/python
import ../easy/ListNode

class LinkedListPalindrome(object):
	def isPalindrome(self, head):
		string = ""
		node = head
		string += node.val
		while node.next != None:
			node = node.next
			string += node.val


		length = len(string)
		l, r = 0, length - 1
		isPalindrome = True
		while l <= r:
			if string[l] is string[r]:
				l += 1
				r -= 1
			else:
				isPalindrome = False
				break

		return isPalindrome



