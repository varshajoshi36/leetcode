#!/usr/bin/python
import math

class PrimeNumbers(object):
	def countPrimes(self, n):
		count = 0
		for j in range(2, n):
			upper = math.ceil((math.sqrt(j)))
			for i in range(2, int(upper) + 1):
				if(j % i == 0):
					break
				if(i == int(upper)):
					count += 1

		return count + 1



x = PrimeNumbers()
print x.countPrimes(11)

