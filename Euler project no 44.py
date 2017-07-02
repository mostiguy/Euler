# -*- coding: utf-8 -*-
"""
Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. The first ten 
pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 
70 − 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference 
are pentagonal and D = |Pk − Pj| is minimised; what is the value of D?

Analysis:

1. Generate the list of pantagonal numbers from 1 to 1,000
2. Generate a list where the sum 
    
"""
import time
import itertools
from math_functions import is_pandigital 

start_time = time.time()
p_max = 10000
p_list = []

for n in range (1, p_max) :
    p_list.append(int(n*((3*n)-1)/2))

for j in range (1, p_max,1) :
    for k in range (j+1,p_max,1) :
        s = p_list[j-1]+p_list[k-1]
        d = abs(p_list[j-1]-p_list[k-1])
        
        # verify if pantagonal
        if (is_pentagonal(s) and is_pentagonal(d)) :
            print ("Pentagonal pair Pj and Pk =",p_list[j],p_list[k],"sum ",s,"difference ",d)
            print ("j ",j,"k ",k)
            break

elapsed_time = time.time() - start_time
print ("Elapse time: {:.2f} sec".format(elapsed_time))

