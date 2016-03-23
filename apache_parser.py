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
	date = epoch[1:epoch.find(' ')]
	d = int(time.mktime(time.strptime(date, "%d/%b/%Y:%H:%M:%S")))
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

for line in sys.stdin:
	log_data.append(pythonized(pattern.match(line).groupdict()))
sys.stdout.write("\n".join(map(str, log_data)) + '\n')
