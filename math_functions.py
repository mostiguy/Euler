# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 07:35:20 2017

@author: mostiguy

Usefull math function

"""
import math

fact = (1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880)
# Fibonacci function.
# n is the number of iteration

def fib(n):
    a,b = 1,1
    print (a)
    for i in range(n-1):
        a,b = b,a+b
        print (a)
    return a

# Return True if prime and False if not a prime

def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    else:
        max = int(math.sqrt(num))
        for div in range(2,max+1):
            if num % div == 0:
                return False
        return True
    
def is_perm(a,b): return sorted(str(a))==sorted(str(b))
# 
def is_pandigital(n, s=10): n=str(n); return len(n)==s and not '1234567890'[:s].strip(n)

#--- sum of factorial's digits-------------------------------------------------------------------
def sof_digits(n):
    if n==0: return 1
    s = 0
    while n > 0:
        s, n = s + fact[n % 10], n // 10
    return s

#
def is_pentagonal(n):
    i = ((math.sqrt((24*n)+1)+1)/6)  
    return i.is_integer()
    
#--- sum of the digits to a power e-------------------------------------------------------------
def pow_digits(n, e):
    s = 0
    while n > 0:
        s, n = s + (n % 10)**e, n // 10
    return s


def prime_sieve(n):
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n//2) if sieve[i]]

def gcd(a,b):
    r = a % b
    while r > 0:
        print (a, b, r)
        a, b, r = b, r, b%r
    return b
