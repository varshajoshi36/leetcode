#! /usr/bin/python

def fourSumCount(A, B, C, D):
        first_sum = {}
        second_sum = {}
        sol = []
        sol_count = 0
        for i in range(0, len(A)):
                for j in range(0, len(B)):
                        addition = A[i] + B[j]
                        indices = [i,j]
                        if addition in first_sum.keys():
                                first_sum[addition] += 1
                        else:
                                first_sum[addition] = 1

        for i in range(0, len(C)):
                for j in range(0, len(D)):
                        addition = C[i] + D[j]
                        indices = [i,j]
                        if addition in second_sum.keys():
                                second_sum[addition] += 1
                        else:
                                second_sum[addition] = 1

        for first_num in first_sum.keys():
                if -first_num in second_sum.keys():
                        sol_count += first_sum[first_num] * second_sum[-first_num]
                        '''for list1 in first_sum[first_num]:
                                for list2 in second_sum[-first_num]:
                                        sol1 = list1 + list2
                                        sol.append(sol1)'''
        return sol_count


