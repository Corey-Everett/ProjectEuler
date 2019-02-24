## Name: Corey Everett
## Date: January 24th, 2019
## Program: Project Euler Problem 1
## Purpose: This program solves problem 1 from Project Euler, which is as follows:
## Find the sum of all the multiples of 3 or 5 below 1000.The sum of these multiples is 23.

number = 1000;
finalNumber = 0;

i = 1;
while i < 1000:
    if i%5 == 0 or i%3 == 0:
        finalNumber+=i
    i+=1

print(finalNumber);


