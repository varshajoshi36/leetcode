'''
Follow up for H-Index: What if the citations array is sorted in ascending order? Could you optimize your algorithm?

Hint:

Expected runtime complexity is in O(log n) and the input is sorted.

'''

def hIndex(citations):
	first = 0
	last = len(citations) - 1
	while first <= last:
		mid = first + (last - first)/2
		if citations[mid] < len(citations[mid:]):
			first = mid + 1
		elif citations[mid -1] > len(citations[mid:]):
			last = mid - 1
		else:
			return len(citations[mid:])


citations = [int(ele) for ele in raw_input().split()]
print citations
print hIndex(citations)
