"""
Exercise 2: Write another program that prompts for a list of numbers as above and at the end prints out both the maximum and minimum of the numbers instead of the average.
"""

largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    else:
        try:
            inum = int(num)
            if largest is None or inum > largest:
                largest = inum
            elif smallest is None or inum < smallest:
                smallest = inum
        except:
            print('Invalid input')
            continue        
   
print("Maximum is", largest)
print("Minimum is", smallest)