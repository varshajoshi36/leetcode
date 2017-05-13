"""
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.
"""

def plusOne(digits):
	carry = 0
	summation = digits[-1] + 1
	carry = summation / 10
	digits[-1] = summation % 10
	if carry > 0:
		for i in range(len(digits) - 2, -1, -1):
			summation = digits[i] + carry
			carry = summation / 10
			digits[i] = summation % 10

	if carry > 0:
		digits.insert(0, carry)

	return digits

def main():
	print plusOne(map(int, raw_input().split(',')))

if __name__ == '__main__':
	main()
		
