#!/usr/bin/python

import re
import sys
from operator import itemgetter
from itertools import groupby


dict = []

for line in sys.stdin:
	dict.append(eval(line))

#sort the list
dict = sorted(dict, key=itemgetter('host'))

#group list by unique IP address
result = []
ip_count = 0

for key, items in groupby(dict, key=itemgetter('host')):
	result.append(list(items))
	ip_count += 1
dict = result

#write as new grouped IP address list
sys.stdout.write("\n".join(map(str,dict)) + '\n')

#write statistics to statfile
f = open('statfile', 'a')
f.write("\nAdding data from <encode_parser.py...\n")
f.write("Task(s) completed - grouped log by unique ip address\n")
ip_count = "Unique IP Address Count:" + str(ip_count) + "\n"
f.write(ip_count)
