'''
Given a string , find the number of "unordered anagrammatic pairs" of substrings.

Input Format 
First line contains , the number of testcases. Each testcase consists of string  in one line.
'''

from collections import *
for i in range(input()):
    s = raw_input()
    check = defaultdict(int)
    l = len(s)
    for i in range(l):
        for j in range(i+1,l+1):
            sub = list(s[i:j])
            sub.sort()
            sub = "".join(sub)
            check[sub]+=1
    sum_no = 0
    print check
    for i in check:
        n = check[i]
        sum_no += (n*(n-1))/2
    print sum_no
