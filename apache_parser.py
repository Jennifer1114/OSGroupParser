#!/usr/bin/python

import re
import sys
import time
from datetime import datetime

log_data = []

parts = [
	r'(?P<host>\S+)',                   # host %h
	r'\S+',                             # indent %l (unused)
	r'(?P<user>\S+)',                   # user %u
 	r'\[(?P<time>.+)\]',                # time %t
 	r'"(?P<request>.*)"',               # request "%r"
 	r'(?P<status>[0-9]+)',              # status %>s
 	r'(?P<size>\S+)',                   # size %b (careful, can be '-')
 	r'"(?P<referrer>.*)"',              # referrer "%{Referer}i"
	r'"(?P<agent>.*)"',                 # user agent "%{User-agent}i"
]

pattern = re.compile(r'\s+'.join(parts)+r'\s*\Z')

#conversion from timestamp to epoch time
def epoch_time(epoch):
	try:
		date = epoch[1:epoch.find(' ')]
		d = int(time.mktime(time.strptime(date, "%e/%b/%Y:%H:%M:%S")))
	except ValueError:
		d = 0
	return d


# Change Apache log items into Python types.
def pythonized(d):
	# Clean up the request.
	d["request"] = d["request"].split()[1]
     
	# Some dashes become None.
	for k in ("user", "referrer", "agent"):
		d[k] = "-"

	# Change timestamp to seconds
	d["time"] = epoch_time(d["time"])

         
	# The size dash becomes 0.
	if d["size"] == "-" or d["size"] <= 0:
		d["size"] = 0
	else:
		d["size"] = int(d["size"])
     
	return d

line_count = 0

for line in sys.stdin:
	log_data.append(pythonized(pattern.match(line).groupdict()))
	line_count += 1
sys.stdout.write("\n".join(map(str, log_data)) + '\n')

#write statistics to file
f = open('statfile', 'w')
f.write("Adding data from <apache_parser.py>...\n")
line_count = "Line count: " + str(line_count) + "\n"
f.write(line_count)
