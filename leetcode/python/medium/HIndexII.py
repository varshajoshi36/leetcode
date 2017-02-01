'''
Follow up for H-Index: What if the citations array is sorted in ascending order? Could you optimize your algorithm?

Hint:

Expected runtime complexity is in O(log n) and the input is sorted.

'''
class Solution(object):
    def recursive_hindex(self, citations, start_index, end_index):
        mid_index = start_index + (end_index - start_index + 1)/2
        elements_greater = len(citations[mid_index:])
        if mid_index is 0:
            return len(citations)
        elif mid_index is 1 and citations[mid_index] >= elements_greater:
            if citations[0] > elements_greater:
                return len(citations)
            else:
                return len(citations[mid_index:])
        elif citations[mid_index - 1] <= elements_greater and citations[mid_index] >= elements_greater:
                return len(citations[mid_index:])
        elif citations[mid_index] <= elements_greater:
                return self.recursive_hindex(citations, mid_index, end_index)
        else:
                return self.recursive_hindex(citations, start_index, mid_index)
                
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if len(citations) is 0:
                return 0
        if citations[-1] is 0:
                return 0
        if len(citations) is 1 and citations[0] > 0:
                return 1
        length = len(citations)
        return self.recursive_hindex(citations, 0, length - 1)
        
        


citations = [int(ele) for ele in raw_input().split()]
print citations
print hIndex(citations)
