#!/usr/bin/python

import re
import sys

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

# Change Apache log items into Python types.
def pythonized(d):
	# Clean up the request.
	d["request"] = d["request"].split()[1]
     
	# Some dashes become None.
	for k in ("user", "referrer", "agent"):
		if d[k] == "-":
			d[k] = None
         
	# The size dash becomes 0.
	if d["size"] == "-":
		d["size"] = 0
	else:
		d["size"] = int(d["size"])
     
	return d

for line in sys.stdin:
	log_data.append(pythonized(pattern.match(line).groupdict()))
sys.stdout.write("\n".join(map(str, log_data)) + '\n')
