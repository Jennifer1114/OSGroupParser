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

for key, items in groupby(dict, key=itemgetter('host')):
	result.append(list(items))
dict = result

#write as new grouped IP address list
sys.stdout.write("\n".join(map(str,dict)) + '\n')
