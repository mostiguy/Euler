# -*- coding: utf-8 -*-
"""
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
By starting at the top of the triangle below and moving to adjacent numbers on 
the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by 
trying every route. However, Problem 67, is the same challenge with a triangle 
containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)
"""

import time
import math 

data = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

start_time = time.time()

table=[]
i = 0

# build a table
for row in data.splitlines():
    row_int=[]
    for j in row.split():
        row_int.append(int(j))
    table.append(row_int)
    i += 1
    
for r in range(len(table)-1, 0,-1):
    for c in range(0, r):
        table[r-1][c] += max(table[r][c], table[r][c+1])

print ("Maximum path sum total in triangle", table[0][0])
 
   
elapsed_time = time.time() - start_time
print ("Elapse time: {:.2f} sec".format(elapsed_time))