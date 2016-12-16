#! /usr/bin/python

def isValid(s):
	is_valid = True
	par_pair = {'{':'}', '(':')', '[':']'}
	endPar = ['}', ')', ']']
	inputPar = []
	for p in s:
		if p not in endPar:
			inputPar.append(p)
		else:
			if not inputPar:
				is_valid = False
				print '1st'
				break
			if p != par_pair[inputPar.pop()]:
				is_valid = False
				print '2nd'
				break
	if inputPar:
		is_valid = False
		print '3rd'
	return is_valid


S = "[({})]"
print S
print isValid(S)

