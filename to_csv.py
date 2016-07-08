#!/usr/bin/python

import csv
import sys

dict = []
merged_dict = []

#read in list
for line in sys.stdin:
	dict.append(eval(line))

[ merged_dict.extend(l) for l in dict ]

keys = merged_dict[0].keys()

with open('v50.csv', 'wb') as output_file:
	dict_writer = csv.DictWriter(output_file, keys)
	dict_writer.writeheader()
	dict_writer.writerows(merged_dict)