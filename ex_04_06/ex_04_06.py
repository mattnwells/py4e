"""
Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate).
"""

def computepay(hours, rate):
    # print("In computepay", hours, rate)
    if hours > 40:
        reg = rate * hours
        otp = (hours - 40.0) * (rate * 0.5)
        pay = reg + otp
    else:
        pay = hours * rate
    # print("Returning", pay)
    return pay

sh = input("Input hours: ")
sr = input("Input rate: ")

fh = float(sh)
fr = float(sr)

xp = computepay(fh, fr)
    
print("Pay:", xp)