"""
Exercise 7: Rewrite the grade program from the previous chapter using a function called computegrade that takes a score as its parameter and returns a grade as a string.
"""

def computegrade(fscore):
    while True:
        score = input('Enter score:')
        if score == 'done':
            print('Goodbye!')
            break
        try:
            fscore = float(score)
            if  0.0 <= fscore <= 1.0:
                if fscore >= 0.9: print('A')
                elif fscore >= 0.8: print('B')
                elif fscore >= 0.7: print('C')
                elif fscore >= 0.6: print('D')
                elif fscore < 0.6: print('F')
            else:
                print('Value must be between 0.0 and 1.0')
        except:
            print('Bad score. Enter numbers only')
        continue

computegrade(input) 

