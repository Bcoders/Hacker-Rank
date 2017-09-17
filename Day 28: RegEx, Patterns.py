#!/bin/python3
"""This program produces test questions for another program that is designed to look for email
ids that end with @gmail.com"""

import sys

names = []
N = int(input().strip())
for a0 in range(N):
    firstName,emailID = input().strip().split(' ')
    firstName,emailID = [str(firstName),str(emailID)]
    domain = emailID[-10:] 
    if domain == '@gmail.com':
         names.append(firstName)
            
names.sort()
for items in names:
    print (items)
    
