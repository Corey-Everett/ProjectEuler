## Name: Corey Everett
## Date: January 30th, 2019
## Program: Project Euler Problem 3 Solver
## Purpose: This program completes problem 3 of Project Euler, which is as follows:
## What is the largest prime factor of the number 600851475143 ?

largestPrime = 600851475143;
currentDivisor = 2;
while (currentDivisor < largestPrime):
    if (largestPrime%currentDivisor == 0):
        largestPrime /= currentDivisor
    currentDivisor+=1;


print(largestPrime)