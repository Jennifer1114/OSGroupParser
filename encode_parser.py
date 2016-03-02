#!/usr/bin/python

import re
import sys
from operator import itemgetter
from itertools import groupby

def IP_sort(L):
	return sorted(L, key=itemgetter('host'))

def IP_group(L):
	result = []
	new_ID = 0
	for key, items in groupby(L, key=itemgetter('host')):
		result.append(list(items))
		new_ID = new_ID + 1
	return result

dict = []

for line in sys.stdin:
	dict.append(eval(line))

newdict = IP_group(IP_sort(dict))
sys.stdout.write("\n".join(map(str,newdict)) + '\n')
