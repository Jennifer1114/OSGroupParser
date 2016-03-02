#!/usr/bin/python

from os import system

system('python apache_parser.py < access10000_2015 > to_encode.txt')

system('python encode_parser.py < to_encode.txt > stmp_chk.txt')

system('python stmp_check.py < stmp_chk.txt')
