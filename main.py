#!/usr/bin/python

from os import system

print "Running <apache_parser.py>:\nCleaning up request, empty items, negative file size, etc..."
system('python apache_parser.py < access10000_2015 > to_encode.txt')

print "Running <encode_parser.py>:\nEncode the IP address, organize by unique IP address ID..."
system('python encode_parser.py < to_encode.txt > stmp_chk.txt')

print "Running <stmp_check.py>:\nChecking timestamp on grouped IP addresses..."
system('python stmp_check.py < stmp_chk.txt > err_code_check.txt')

print "Running <err_code_chk.py>:\nReducing file, deleting error code lines..."
system('python err_code_chk.py < err_code_check.txt > analysis.txt')

print "Complete"
