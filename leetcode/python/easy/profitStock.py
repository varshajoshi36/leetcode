"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.
"""
def maxProfit2(prices):
        max_profit = 0
        if len(prices) == 0:
            return 0
        smallest = prices[0]
        largest = -1
        for i in range(1, len(prices)):
            if prices[i] < smallest:
                smallest = prices[i]
                largest = -1
            elif prices[i] > largest and prices[i] > smallest:
                largest = prices[i]
                if largest - smallest > max_profit:
                    max_profit = largest - smallest

        if largest != -1 and largest - smallest > max_profit:
            max_profit = largest - smallest

        return max_profit

def maxProfit(prices):
    max_profit = 0
    for i in range(len(prices) - 1):
        next_max = max(prices[i + 1:])
        if next_max - prices[i] > max_profit:
            max_profit = next_max - prices[i]

    return max_profit


def main():
    print maxProfit2(map(int, raw_input().split(',')))

if __name__ == '__main__':
    main()
        
