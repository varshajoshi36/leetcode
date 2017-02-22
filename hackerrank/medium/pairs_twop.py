'''
Given  integers, count the number of pairs of integers whose difference is .
'''

def pairs(a, k):
	a.sort()
	count = 0
	i, j = 0, 0
	while i < len(a) and j < len(a):
		diff = a[j] - a[i]
		if diff == k:
			count += 1
			i += 1
			j += 1
		if diff > k:
			i += 1
		if diff < k:
			j+= 1
	return count

length, k = raw_input().split()
length, k = int(length), int(k)
a = raw_input().split()
a = map(int, a)
print pairs(a, k)
