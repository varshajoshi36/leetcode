'''
Your algorithms have become so good at predicting the market that you now know what the share price of Wooden Orange Toothpicks Inc. (WOT) will be for the next N days.

Each day, you can either buy one share of WOT, sell any number of shares of WOT that you own, or not make any transaction at all. What is the maximum profit you can obtain with an optimum trading strategy?
'''
#!/bin/python

import sys

t = int(raw_input().strip())
prices_list = []
for a0 in xrange(t):
	N = int(raw_input().strip())
	prices = map(int, raw_input().strip().split(' '))
	prices_list += [prices]
	
for prices in prices_list:
	profit = 0
	max_so_far = 0
	for i in range(len(prices) - 1, -1, -1):
		if prices[i] > max_so_far:
			max_so_far = prices[i]
		profit += max_so_far - prices[i]

	print profit
