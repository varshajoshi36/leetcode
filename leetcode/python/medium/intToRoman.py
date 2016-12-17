#! /usr/bin/python

def intToPython(num):
	roman = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        r_to_int = [1, 5, 10, 50, 100, 500, 1000]
	roman_num = ""
	while num > 0:
		division = 0
		for i in range(len(roman) - 1, -1, -1):
			division = num/r_to_int[i]
			if division > 0:
				if i % 2 != 0 and num >= r_to_int[i + 1] - r_to_int[i + 1]/10:
					roman_num += roman[i - 1] + roman[i + 1]
					num = num - (r_to_int[i + 1] - r_to_int[i - 1])
					break
				elif division <= 3:
					roman_num += division * roman[i]
					num = num - division * r_to_int[i]
					break
				else:
					roman_num += roman[i] + roman[i + 1]
					num = num - (r_to_int[i + 1] - r_to_int[i])
					break
	return roman_num

num = 463
print intToPython(num)	
