"""
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.
"""

def trailingZeroes(n):
    five = 5
    no_fives = n/5
    no_zeros = 0
    while no_fives > 0:
        no_zeros += no_fives
        five *= 5
        no_fives = n/five


    return no_zeros

def main():
    print trailingZeroes(int(raw_input()))

if __name__ == '__main__':
    main()
