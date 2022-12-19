"""
Exercise 3: Encapsulate this code in a function named count, and generalize it so that it accepts the string and the letter as arguments.
"""

def count_letter(word, searched):
    count = 0
    for letter in word:
        if letter == searched:
            count = count + 1
    print(count)

word = input('Input a word: ')
searched = input('Input a letter: ')

count_letter(word, searched)