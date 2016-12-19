import ListNode from ../medium/ListNode


'''Given a singly linked list, determine if it is a palindrome.
Follow up:
Could you do it in O(n) time and O(1) space?
'''

class LinkedListPalindrome(object):
	def isPalindrome(head):
		if head == None:
                        return True
                temp_node = ListNode(head.val)
                orig_head = temp_node
                node  = head
                while node.next != None:
                        node = node.next
                        new_node = ListNode(node.val)
                        temp_node.next = new_node
                        temp_node = new_node 
                        
                next_node = None
                prev_node = None
                curr_node = head
                while curr_node != None:
                        next_node = curr_node.next
                        curr_node.next = prev_node
                        prev_node = curr_node
                        curr_node = next_node
                        
                head = prev_node
                isPalindrome = True
                
                while head.next != None:
                        if head.val != orig_head.val:
                                isPalindrome = False
                                break
                        else:   
                                head = head.next
                                orig_head = orig_head.next
                                
                return isPalindrome
