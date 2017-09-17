#python 3

"""This program calculates whether a number is prime or not"""

import sys
import math 

def check_prime(num):
    # special case 1
    if num == 1: 
        return 0
    #special case 2 
    elif num == 2:
        return 1

    #eliminating all even numbers
    elif num%2 == 0:
        return 0
    
    # a number n is prime if it is not divisible by any number from
    # 2 to under_square_root(n)
    
    
    for i in range(3,int(math.sqrt(num))+1,2):
        if num%i == 0:
            return 0
                 
    return 1 

n = int(input())
for iter in range(n):
    num = int(input())
    result = check_prime(num)
    if result == 1:
        print ("Prime")
    else:
        print ("Not prime")
