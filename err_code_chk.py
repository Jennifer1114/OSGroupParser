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

#filtering empty lists, do recount
dict2 = [l for l in dict if l != []]

ip_count = 0
line_count = 0

for l in dict2:
	for index in range(len(l)):
		line_count += 1
	ip_count += 1

#write out successful code lines
sys.stdout.write("\n".join(map(str,dict2)) + '\n')

#write statistics to statfile
f = open('statfile', 'a')
f.write("\nAdding data from <err_code_chk.py>...\n")
f.write("Task(s) completed - obtaining only successful requests\n")
ip_count = "Line Count: " + str(line_count) + "\tIP Address Count: " + str(ip_count) + "\n"
f.write(ip_count)
