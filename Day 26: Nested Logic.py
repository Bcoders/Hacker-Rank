# python 3
""" This program calculates how much a person needs to be charged when they
return the book to the library. If late by month is is 500 times number of month,
if late by a year, it is automatically 1000 and if late by days it is 15 times
number of days."""


r_day,r_month,r_year = map(int, input().strip().split(" ")) #returned dates
e_day,e_month,e_year = map(int, input().strip().split(" ")) #expeted dates

if r_year > e_year: #if late by year
    print ("10000")

elif r_year < e_year: # if early by a year, no charge.
    print('0')
    
else:
    if r_month > e_month: #if late by month
        print(500*(r_month-e_month))

    elif r_month < e_month: #if early by a month
        print('0')
        
    else:
        if r_day > e_day: #if late by day
            print(15*(r_day-e_day))
            
        else:
            print('0')
