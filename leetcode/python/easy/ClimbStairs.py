'''You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.'''

def climbStairs(n):
        """
        :type n: int
        :rtype: int
        """
        hop = []
        hop.insert(1, 1)
        hop.append(2)
        for i in range(2, n):
            hop.append(hop[i - 1] + hop[i - 2])
        return hop[n - 1]

print climbStairs(6)
