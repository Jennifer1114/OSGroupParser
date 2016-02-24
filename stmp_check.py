#!/usr/bin/python

import re
import sys
import time
from datetime import datetime

def strictly_incr(L):
	num_errors = 0
	for index in range(len(L)-1):
		if (cmp(L[index]['time'], L[index+1]['time']) == 1):
			print (L[index]['time'], ':', L[index+1]['time'])
			num_errors = num_errors + 1

	return num_errors

dict = []

for line in sys.stdin:
	dict.append(eval(line))

print strictly_incr(dict)
