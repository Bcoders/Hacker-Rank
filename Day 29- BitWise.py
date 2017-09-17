#!/bin/python3
""" This program takes in t test cases and perform bit wise operation on the set of first n natural numbers and prints the result that is max but less than k"""
import sys

#number of cases
t = int(input().strip())


for a0 in range(t):
    max_num = 0
    # n is the set of numbers which go under bit-wise operation
    # the result of bit wise operation should be less than k
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    
    # result of bit wise operation should be max k-1. 
    max_reach = k-1
    reach = False
    
    #for each case, we have to perform bit wise on first n set of natural numbers.
    #begin performing from the end because the chances it reaches max_reach is greater
    #trick: we don't have to iterate through all the numbers if we find a max_reach
    for i in range(n-1,0,-1):
        for j in range(n,i,-1):
            bit_sum = i & j
            
            # only analyse cases where max is less than k and greater than max_num
            if bit_sum < k and bit_sum >max_num:
                max_num = 
                #if we find one operation that results in max_reach, we can break from the loop and print the result.
                if max_num == max_reach:
                    reach = True
                    break
            
        if reach:
            break
        
        
        
    print (max_num)
            
