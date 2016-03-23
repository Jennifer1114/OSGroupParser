#!/usr/bin/python

import re
import sys
import time
from datetime import datetime

dict = []
next = str(int(0))

for line in sys.stdin:
	dict.append(eval(line))

#give IP addresses unique ID's
for l in dict:
	for index in range(len(l)):
		l[index]['host'] = next
	next = str(int(next) + 1)

#check if timestamps are in ascending order
for l in dict:
	index = 0
	while index < (len(l)-1):
		if (cmp(l[index]['time'], l[index+1]['time']) == 1):
			del l[index]
		index += 1

#rewrite time to delta timestamp
for l in dict:
	index = 0
	first_time = l[index]['time']
	for index in range(len(l)):
		l[index]['time'] -= first_time


#write to next file, err_code_check.txt
sys.stdout.write("\n".join(map(str,dict)) + '\n')
