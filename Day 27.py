#python 3
"""This program generates a test for a program using which a professors decides whether to
give lecture or not. If present number of students does not equal to
at least the counter number he has in mind, he doesn't attend the class.
We generate randomnumber of students and generate numbers from -1000 to +1000
where -ve integer means how many minutes you were early, positve means
how many you were late and 0 means on time.

For each run we have to make sure the number of students is not same
in each class, and there is at least one student late, early and on time. 

"""


import random
#number of lectures given by the professor
num_lec = 5
num = []
print(num_lec)

for i in range(num_lec):
    
    repeat = True
    while(repeat):
        num_student = random.randrange(3,200)
        if num_student not in num:
            repeat = False
    
    k = random.randrange(0,num_student)
    
    array = []
    array.append('0')
    for i in range(num_student-1):
        array.append(random.randrange(-1000,1000))
    
    print(num_student, k)
    
    for elem in array:
        print(elem, end=' ')
    print()   
