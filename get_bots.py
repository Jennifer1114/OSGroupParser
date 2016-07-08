#!usr/bin/python

# To get the robots.log from the access log, use the following cmd line prompt:
#
# cat access10000_2015 | grep -e bot -e robot -e spider -e crawler | awk '{print $1}'
# | uniq | sort > robots.log


import sys

with open("robots.log") as log:
	robots = log.readlines()

