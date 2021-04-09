


# 1. Conditional Basics
# a. prompt the user for a day of the week, print out whether the day is Monday or not

weekdays = 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
while True:
    day_input = input('What day is it??? ')
    if day_input == 'Monday':
        print('So it\'s Monday')
    else:
        print('So it\'s not Monday')

# *** teacher notes
day_of_the_week = input('What day is it??? ')

if day_of_week.lower() == 'monday':
    print('its monday)
else:
    print('not monday')



# prompt the user for a day of the week, print out whether the day is a weekday or a weekend

weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

while True:
    day_input = input('What day is it?')
    if day_input in weekday:
        print('It\'s a weekday')
    else:
        print('It\'s a weekend')

# *** teacher notes


if day_of_week.lower().startswith('s'):
    print('weekend')
else:
    print('weekday')



# create variables and make up values for

# the number of hours worked in one week
# the hourly rate
# how much the week's paycheck will be
# write the python code that calculates the weekly paycheck. 
# You get paid time and a half if you work more than 40 hours

week_hours = 40
hourly_rate = 10
regular_week_paycheck = (week_hours * hourly_rate)
overtime = (week_hours * hourly_rate) + ((hourly_rate * 1.5) * (40 - week_hours))

if week_hours <= 40:
    print(regular_week_paycheck)
else: 
    print(overtime)



# Loop Basics
# While


# Create an integer variable i with a value of 5.
# Create a while loop that runs so long as i is less than or equal to 15
# Each loop iteration, output the current value of i, then increment i by one.

# Create an integer variable i with a value of 5.
# Create a while loop that runs so long as i is less than or equal to 15
# Each loop iteration, output the current value of i, then increment i by one.

i = 5

while i <= 15:
    print(i)
    i += 1


# Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.
# Alter your loop to count backwards by 5's from 100 to -10.
# Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 
# 1,000,000. Output should equal:

i=100
while i >= -10:
    print(i)
    i += -5
# ~~~
i = 2
while i <= 1000000:
    print(i)
    i **= 2

# Write a loop that uses print to create the output shown below.

i = 100

while i >= 5:
    print(i)
    i += -5


# For Loops

# Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.


proposed_num = input('Please inset a positive integer ')

for n in range(1,11):
    print(f'{proposed_num} X {n} = {proposed_num * n}')

proposed_num = int(proposed_num)


# Create a for loop that uses print to create the output shown below.

for n in range(1,10):
    print(str(n)*n)


# Prompt the user for an odd number between 1 and 50. Use a loop and a break 
# statement to continue prompting the user if they enter invalid input. 
# (Hint: use the isdigit method on strings to determine this). 
# Use a loop and the continue statement to output all the odd numbers between 
# 1 and 50, except for the number the user entered.

while True:
    positive_num = input('Please insert an odd number between 1 and 50: ')
    if positive_num.isdigit():
        if int(positive_num) % 2 == 1 and int(positive_num) <= 50:

# ~~~ 



while not positive_num.isdigit():
    positive_num = input('Your input did not meet qualifications ')
    if positive_num.isdigit():
        if int(positive_num) % 2 == 0 or int(positive_num) > 50:
            positive_num = "Please try again"
            break