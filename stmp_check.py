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

#remove empty entries in list
dict2 = [l for l in dict if l != []]

#rewrite time to delta timestamp
ip_count = 0
line_count = 0

for l in dict2:
	index = 0
	ip_count += 1
	first_time = l[index]['time']
	for index in range(len(l)):
		l[index]['time'] -= first_time
		line_count += 1

#write to next file, err_code_check.txt
sys.stdout.write("\n".join(map(str,dict2)) + '\n')


#write statistics to statfile
f = open('statfile', 'a')
f.write("\nAdding data from <stmp_check.py>...\n")
f.write("Task(s) completed - ensure correct order for timestamps, rewrite as delta timestamp\n")
ip_count = "Line count: " + str(line_count) + "\tIP Address Count: " + str(ip_count) + "\n"
f.write(ip_count)
