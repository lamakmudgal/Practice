#!/bin/python3

import os
import sys

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    #
    # Write your code here.
    #
    newgrades = []
    count = 0
    for i in grades:
        if i<38:
            newgrades.append(i)
            break
        elif i%5 ==3 or i%5 == 4:
            newgrades.append(int(i)+(5-i%5))
        else:
            newgrades.append(i)
    return newgrades

if __name__ == '__main__':

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    print(result)
