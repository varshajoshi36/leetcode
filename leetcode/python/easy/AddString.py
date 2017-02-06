'''
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''

def addStrings(num1, num2):
	length1 = len(num1)
	length2 = len(num2)
	if length1 == 0:
		return num2
	if length2 == 0:
		return num1
	res = ''
	i, j = -1, -1
	carry = 0
	while i >= -length1 and j >= -length2:
		ascii_add = carry + ord(num1[i]) + ord(num2[j]) - 2 * ord('0')
		digit = ascii_add % 10
		carry = ascii_add/10
		res = str(digit) + res
		i -= 1
		j -= 1

	if j >= -length2:
		if carry == 0:
			res = num2[:length2 + j + 1] + res
		else:
			res = addStrings(num2[:length2 + j + 1], str(carry)) + res
	elif i >= -length1:
		if carry == 0:
			res = num1[:length1 + i + 1] + res
		else:
			res = addStrings(num1[:length1 + i + 1], str(carry)) + res
	elif carry > 0:
		res = str(carry) + res
		

	return res

num1, num2 = "89", "11"
print 71+168899993
print addStrings(num1, num2)
