'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
'''
import sys

def maxProfit(prices):
    lowest = sys.maxint
    profit = 0
    for price in prices:
        if price < lowest:
            lowest = price
        else:
            profit += price - lowest
            lowest = price

    return profit


prices = [1,2,4]
print maxProfit(prices)

