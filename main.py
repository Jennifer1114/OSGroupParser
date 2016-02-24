#!/usr/bin/python

from os import system

system('python apache_parser.py < access10000_2015 > stmp_chk.txt')

system('python stmp_check.py < stmp_chk.txt')
