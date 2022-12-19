"""
Exercise 1: Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None. Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.
"""

def chop(list):
    del list[0]
    del list[-1]

def middle(list):
    middle_list = list[1:]
    del middle_list[-1]
    return middle_list

my_list = [1, 2, 3, 4]
my_list2 = [1, 2, 3, 4]

chop_list = chop(my_list)
print(my_list)
print(chop_list)

mid_list = middle(my_list2)
print(my_list2)
print(mid_list)