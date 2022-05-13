# Conditional Execution

# Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
# Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. 
# Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
# You should use input to read a string and float() to convert the string to a number.
# Do not worry about error checking the user input - assume the user types numbers properly.

hrs = input("Enter hours : ")
hrs = float(hrs)
rate = input("Enter Rate per hour : ")
rate = float(rate)
pay = hrs * rate

if hrs > 40 :
    pay = pay + (hrs - 40) * (rate*0.5)

print(pay)

# Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. 
# If the score is between 0.0 and 1.0, print a grade using the following table:
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# If the user enters a value out of range, print a suitable error message and exit. 
# For the test, enter a score of 0.85.

score = input("Enter Score : ")
score = float(score)
# print (score)

if score > 1.00:
    print("Value is of out of range. The value should be between (0, 1)")
elif score >= 0.9:
    print("A")
elif score >= 0.80:
    print("B")
elif score >= 0.70:
    print("C")
elif score >= 0.60:
    print("D")
else:
    print("F")