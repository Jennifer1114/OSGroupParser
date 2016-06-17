#!/usr/bin/python

import sys
import re
import csv

dict = []

#read in list from analysis.txt
for line in sys.stdin:
	dict.append(eval(line))

for l in dict:
	index = 0
	while index < (len(l)-1):
		if l[index]['request'] == 0:
			del l[index]
		index += 1

dict2 = [l for l in dict if l != []]

ip_count = 0
line_count = 0

for l in dict2:
	index = 0
	ip_count += 1
	for index in range(len(l)):
		line_count += 1


sys.stdout.write("\n".join(map(str,dict2)) + '\n')

f = open('statfile', 'a')
f.write("\nAdding data from <reduce_path.py>...\n")
f.write("Task(s) completed - reduce path assigns number of accesses to path name\n")
ip_count = "Line count: " + str(line_count) + "\tIP Address Count: " + str(ip_count) + "\n"
f.write(ip_count)
