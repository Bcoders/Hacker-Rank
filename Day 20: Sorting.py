"""
Given an array,a, of size n distinct elements, sort the array in
ascending order using the Bubble Sort algorithm above.
"""
#!/bin/python3

import sys
def Bubblesort(a):
    #total num of swaps
    numOfSwaps = 0
    n = len(a)
    for i in range(n):
        #integers to calculate number of swaps
        numberOfSwaps = 0;
        for j in range (n-1):
            if a[j]>a[j+1]:
                a[j], a[j+1]= a[j+1],a[j]
                numOfSwaps += 1
                numberOfSwaps += 1
        if numberOfSwaps == 0:
            return (a[0],a[-1],numOfSwaps)
        
n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
firstElem, lastElem, swaps = Bubblesort(a)

print("Array is sorted in %d swaps." % swaps)
print( "First Element:",firstElem)
print ("Last Element:", lastElem)
