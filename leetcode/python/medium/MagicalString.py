#A magical string S consists of only '1' and '2' and obeys the following rules:

#The string S is magical because concatenating the number of contiguous occurrences of characters '1' and '2' generates the string S itself.

#The first few elements of string S is the following: S = 122112122122112112

#1 22 11 2 1 22 1 22 11 2 11 22

#and the occurrences of '1's or '2's in each group are:

#1 2	2 1 1 2 1 2 2 1 2 2

#You can see that the occurrence sequence above is the S itself.

#Given an integer N as input, return the number of '1's in the first N number in the magical string S.

#Note: N will not exceed 100,000.

#Example 1:
#Input: 6
#Output: 3
#Explanation: The first 6 elements of magical string S is "12211" and it contains three 1s, so return 3.
#Subscribe to see which companies asked this question


def magicalString(n):
	magical_string = [1,2,2]
	pointer = 2
	while len(magical_string) < n:
		if magical_string[-1] is 1:
			next_ele = 2
		else:
			next_ele = 1
		for i in range(magical_string[pointer]):
			magical_string.append(next_ele)
		pointer += 1

	return magical_string[:n].count(1)

n = int(raw_input())
print magicalString(n)

