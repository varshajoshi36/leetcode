"""
Implement int sqrt(int x).

Compute and return the square root of x.
"""

def mySqrt(x):
    """
    :type x: int
    :rtype: int
    """
    start = 0
    end = x/2 + 1
    ans = 0

    while start <= end:
        mid = (start + end)/2

        if mid * mid == x:
            return mid

        if mid * mid < x:
            start = mid + 1
            ans = mid

        if mid * mid > x:
            end = mid - 1

    return ans

x = 900
print mySqrt(x)

