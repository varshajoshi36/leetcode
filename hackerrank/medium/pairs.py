'''
Given  integers, count the number of pairs of integers whose difference is .
'''

def pairs(a, k):
	a.sort()
	dictionary = {}
	count = 0

	for i in range(len(a)):
	dictionary[a[i]] = i
	if (abs(k - a[i]) in dictionary.keys() and abs(k - a[i]) != a[i]):
	    count += 1
	    
	return count

length, k = raw_input().split()
length, k = int(length), int(k)
a = raw_input().split()
a = map(int, a)
print pairs(a, k)
