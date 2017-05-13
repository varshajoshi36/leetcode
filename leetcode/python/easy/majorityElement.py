"""
"""

def majorityElement(nums):

	return sorted(nums)[len(nums)/2]

def main():
	print majorityElement(map(int, raw_input().split(',')))

if __name__ == '__main__':
	main()
