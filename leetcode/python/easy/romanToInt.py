#! /usr/bin/pythonin 


def romanToInt(S):
	roman = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
	r_to_int = [1, 5, 10, 50, 100, 500, 1000]
	int_val = 0
	i = 0
	print len(S)
	while(i < len(S)):
		if i == len(S) - 1:
			int_val += r_to_int[roman.index(S[i])]
			print 'int_val, r_to_int[roman.index(S[i])]', i, int_val, r_to_int[roman.index(S[i])]
			i += 1
		else:
			if(roman.index(S[i]) < roman.index(S[i + 1])):
				int_val += r_to_int[roman.index(S[i + 1])]- r_to_int[roman.index(S[i])]
				i += 2
				print 'in 2nd if', i
			else:
				int_val += r_to_int[roman.index(S[i])]
				i += 1
				print 'in last else', i, int_val
	return int_val


S = 'MMXL'
print S
print romanToInt(S)
