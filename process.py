#!/usr/bin/python

from os import system

print "Running <process.py>:\nBeginning processing stages..."
print "Running <to_csv.py>:\nConverting lists of dictionaries to csv file..."
system('python to_csv.py < v40.txt')

print "Running <generate_candidates.py>:\nGenerate list of candidate keys for analysis phases..."
system('python generate_candidates.py < v50.csv')

print "Complete"