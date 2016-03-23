#!/usr/bin/python

import sys

dict = []

#read in list
for line in sys.stdin:
	dict.append(eval(line))

#remove codes that are not 200 (success code - 200)
for l in dict:
	index = 0
	while index < len(l):
		if (l[index]['status'] != "200"):
			del l[index]
		index += 1

sys.stdout.write("\n".join(map(str,dict)) + '\n')
