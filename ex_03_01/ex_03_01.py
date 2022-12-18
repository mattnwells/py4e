"""
Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
"""

sh = input("Input hours: ")
sr = input("Input rate: ")

fh = float(sh)
fr = float(sr)

if fh > 40:
    reg = fr * fh
    otp = (fh - 40.0) * (fr * 0.5)
    xp = reg + otp
else:
    xp = fh * fr
    
print("Pay:", xp)