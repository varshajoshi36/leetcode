#! /usr/bin/python

'''
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

'''

def getLowestEl(lists):
	lowest_element = lists[0][0]
	lowest_index = 0
	for index in range(len(lists)):
		if lists[index][0] < lowest_element:
			lowest_element = lists[index][0]
			lowest_index = index
	
	return lowest_index


def mergeKLists(lists):
	sortedList = []
	if len(lists) is 0:
		return sortedList
	while len(lists) > 1:
		lowest_list_index = getLowestEl(lists)
		sortedList.append(lists[lowest_list_index][0])
		del(lists[lowest_list_index][0])
		if len(lists[lowest_list_index]) is 0:
			del(lists[lowest_list_index])
	
	for i in range(len(lists[0])):
		sortedList.append(lists[0][i])
	
	return sortedList


lists = [[2,3,4],[3,4]]
print mergeKLists(lists)
