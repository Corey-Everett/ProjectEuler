## Name: Corey Everett
## Date: January 25th, 2019
## Program: Project Euler Problem 2 Solver
## Purpose: This program completes problem 2 of Project Euler, which is as follows:
## By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

finalValue = 0;

fib1 = 1; #Higher
fib2 = 1; #Lower
fibNew = 0;

while fib1 < 4000000: ##Find next term
    fibNew = fib1+ fib2
    if fibNew%2==0:
        finalValue+= fibNew;
    fib2=fib1;
    fib1=fibNew;

print(finalValue);