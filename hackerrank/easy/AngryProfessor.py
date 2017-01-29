#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = map(int,raw_input().strip().split(' '))
    students_on_time = sum(i <= 0 for i in a)
    if students_on_time >= k:
        print 'NO'
    else:
        print 'YES'
