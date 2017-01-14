#! /usr/bin/python

'''
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

:type lists: List[ListNode]

:rtype: ListNode
'''

def getLowestEl(lists):
	lowest_element = lists[0].val
	lowest_index = 0
	for index in range(len(lists)):
		if lists[index].val < lowest_element:
			lowest_element = lists[index].val
			lowest_index = index
	
	return lowest_index


def mergeKLists(lists):
	lowest_list_index = getLowestEl(lists)
	sortedList = lists[lowest_list_index]
	head = sortedList
	lists[lowest_list_index] = lists[lowest_list_index].next
	sortedList.next = None
	if lists[lowest_list_index] is None:
		del(lists[lowest_list_index])
	
	if len(lists) is 0:
		return None
	while len(lists) > 1:
		lowest_list_index = getLowestEl(lists)
		sortedList.next = lists[lowest_list_index]
		sortedList = sortedList.next
		lists[lowest_list_index] = lists[lowest_list_index].next
		sortedList.next = None
		if lists[lowest_list_index] is None:
			del(lists[lowest_list_index])
	
	while lists[0] is not None:
		sortedList.append(lists[0].val)
		lists[0] = lists[0].next
	
	return head


lists = [[2,3,4],[3,4]]
print mergeKLists(lists)
