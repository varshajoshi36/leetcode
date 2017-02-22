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
	no_shares = 0
	investment = 0
	returns = 0
	max_price = max(prices)
	for i in range(len(prices)):
		if i == len(prices) - 1:
			if no_shares > 0:
				returns += prices[i] * no_shares
                        	no_shares = 0
		elif prices[i] is max_price and no_shares > 0:
			returns += prices[i] * no_shares
			no_shares = 0
		elif max(prices[i+1:]) > prices[i]:
			investment += prices[i]
			no_shares += 1
		elif no_shares > 0:
			returns += prices[i] * no_shares
			no_shares += 1
	if(returns > investment):
		print returns - investment
	else:
		print 0
	
