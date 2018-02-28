"""
There is a garden with N slots. In each slot, there is a flower. The N flowers will bloom one by one in N days. In each day, there will be exactly one flower blooming and it will be in the status of blooming since then.

Given an array flowers consists of number from 1 to N. Each number in the array represents the place where the flower will open in that day.

For example, flowers[i] = x means that the unique flower that blooms at day i will be at position x, where i and x will be in the range from 1 to N.

Also given an integer k, you need to output in which day there exists two flowers in the status of blooming, and also the number of flowers between them is k and these flowers are not blooming.

If there isn't such day, output -1.

Example 1:
Input: 
flowers: [1,3,2]
k: 1
Output: 2
Explanation: In the second day, the first and the third flower have become blooming.
Example 2:
Input: 
flowers: [1,2,3]
k: 1
Output: -1
"""

#Efficient
class Solution(object):
    def getPosDayArray(self, flowers):
        days_at_pos = [0]*len(flowers)
        for day in range(1, len(flowers) + 1):
            days_at_pos[flowers[day - 1] - 1] = day
        return days_at_pos
    
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        '''Window of size k
        if any value is smaller than the greater of two, 
        shift the window, if found return max of two'''
        day_at_pos = self.getPosDayArray(flowers)
        
        start_pos = 0
        end_pos = start_pos + k + 1
        valid_day =  float('inf')     
            
        
        while start_pos < (len(flowers) - (k+1)):
            current_blooming_day = max(day_at_pos[start_pos], day_at_pos[end_pos])
            valid_window = True
            i = start_pos + 1
            while i < end_pos:
                if day_at_pos[i] < current_blooming_day:
                    valid_window = False
                    break
                i += 1
            if valid_window:
                valid_day = min(valid_day, current_blooming_day)
                start_pos = end_pos
            else:
                start_pos = i
            end_pos = start_pos + k + 1
        
        if valid_day != float('inf'):
            return valid_day
        return -1

"""
#Valid solution, exceeds time limit
class Solution(object):
    def getPosDayArray(self, flowers):
        days_at_pos = [0]*len(flowers)
        for day in range(1, len(flowers) + 1):
            days_at_pos[flowers[day - 1] - 1] = day
        return days_at_pos
    
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        '''Window of size k
        if any value is smaller than the greater of two, 
        shift the window, if found return max of two'''
        day_at_pos = self.getPosDayArray(flowers)
        start_pos = 0
        end_pos = start_pos + k + 1
        valid_days = []
        while start_pos < (len(flowers) - (k+1)):
            current_blooming_day = max(day_at_pos[start_pos], day_at_pos[end_pos])
            valid_window = True
            for i in range(start_pos + 1, end_pos):
                if day_at_pos[i] < current_blooming_day:
                    valid_window = False
                    break
            if valid_window:
                valid_days.append(current_blooming_day)
            start_pos += 1
            end_pos += 1
        
        if len(valid_days) > 0:
            return min(valid_days)
        return -1
"""
