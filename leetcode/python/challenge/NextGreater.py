class Solution(object):

    def nextGreaterElements(self, nums):

        """

        :type nums: List[int]

        :rtype: List[int]

        """

        length = len(nums)

        sol = []

        for i in range(length):

            flag = True

            for j in range(i+1, length):

                if nums[j] > nums[i]:

                    sol.append(nums[j])

                    flag = False

                    break

            if flag:

                for j in range(i):

                    if nums[j] > nums[i]:

                        sol.append(nums[j])

                        flag = False

                        break

            if flag:

                sol.append(-1)

                

        return sol

        
