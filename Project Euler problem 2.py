# -*- coding: utf-8 -*-
"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
By starting with 1 and 2, the first 10 terms will be:

     1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
find the sum of the even-valued terms.

"""


# Fibonacci function.
# n is the number of iteration

def fib(n):
    a,b = 1,1
    print (a)
    for i in range(n-1):
        a,b = b,a+b
        print (a)
    return a

# main program
# Generate all the fibonacci numbers and keep only the 
            
max_sequence = 4000000
total = 0
# print (fib(10))
for s in range (1,34):
    f = fib(s)
    print (f,s)
    if (f<max_sequence):
        if f % 2 == 0:
            total = total + f
            print ("total", total)
    else:
        break
            
    print (total)



