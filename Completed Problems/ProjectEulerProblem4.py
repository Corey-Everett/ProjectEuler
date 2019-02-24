## Name: Corey Everett
## Date: February 20th, 2019
## Program: Project Euler Problem 4 Solver
## Purpose: This program completes problem 4 of Project Euler, which is as follows:
## Find the largest palindrome made from the product of two 3-digit numbers.

largestPalindrome = 0;
num1 = 900;
num2 = 900;

def isPalindromic(sum):

    text = str(sum);
    if ((text[0] == text[5]) & (text[1] == text[4]) & (text[2] == text[3])):
        return True;
    return False;

while (num1 < 1000):
    num2=900;
    while (num2 < 1000):
        sum = num1*num2;
        if (True == isPalindromic(sum)):
            largestPalindrome = sum;
            print("Palindromic sum found!");
        num2+=1;

    num1+=1;
print("Largest palindrome: " + str(largestPalindrome));

