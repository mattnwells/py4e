"""
Exercise 2: Write a program to look for lines of the form:

New Revision: 39772

Extract the number from each of the lines using a regular expression and the findall() method. Compute the average of the numbers and print out the average as an integer.

Enter file:mbox.txt
38549

Enter file:mbox-short.txt
39756
"""

import re

fname = input('Input a file name: ')
try:
    hand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

lst = list()

for line in hand:
    line = line.rstrip()
    num = re.findall('^New Revision:(\s[0-9.]+)', line)
    if len(num) > 0:
        for number in num:
            number = float(number)
        lst.append(number)

avg = sum(lst)/len(lst)
print(avg)