# Control Structures Exercises



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
    print('its monday')
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

# Write some code that prompts the user for a number, then shows a multiplication 
# table up through 10 for that number.


num = int(input('Please insert a positive integer '))

for n in range(1,11):
    print(num, ' X ', n, ' = ', (num * n))



# Create a for loop that uses print to create the output shown below.

for n in range(1,10):
    print(str(n)*n)


# Prompt the user for an odd number between 1 and 50. Use a loop and a break 
# statement to continue prompting the user if they enter invalid input. 
# (Hint: use the isdigit method on strings to determine this). 
# Use a loop and the continue statement to output all the odd numbers between 
# 1 and 50, except for the number the user entered.

while True:
    posited_num = input('Please insert an odd number between 1 and 50: ')
    if posited_num.isdigit():
        if int(posited_num) % 2 == 1 and int(posited_num) <= 50:
            break

while not posited_num.isdigit():
    posited_num = input('Your input did not meet qualifications ')
    if posited_num.isdigit():
        if int(posited_num) % 2 == 0 or int(posited_num) > 50:
            posited_num = "Please try again"
            break

posited_num = int(posited_num)
for num in range(1, 50, 2):
    if num == posited_num:
        print('Yikes! Skipping number: ', num)
    else:
        print('Here is an odd number: ', num)

# The input function can be used to prompt for input and use that input in your python code. 
# Prompt the user to enter a positive number and write a loop that counts from 0 to that number. 
# (Hints: first make sure that the value the user entered is a valid number, also note that the
# input function returns a string, so you'll need to convert this to a numeric type.)

while True:
    posited_num = input('Input a positive number: ')
    if posited_num.isdigit():
        if int(posited_num) > 0:
            posited_num =  int(posited_num)
            for i in range(0, posited_num + 1):
                print(i)

    while not posited_num.isdigit():
        posited_num = input("Incorrect input. Try again: ")
        if posited_num.isdigit():
            if int(posited_num) < 0:
                posited_num = input("Try again: ")
                break


# 2E - Write a program that prompts the user for a positive integer. 
#Next write a loop that prints out the numbers from the number the user entered down to 1.

while True:
  positive_num = input('Input a positive number: ')
  if positive_num.isdigit():
    if int(positive_num) > 0:
      positive_num = int(positive_num)
      for i in range(positive_num, 1, -1):
        print(i)
      break
      
  while not positive_num.isdigit():
    positive_num = ("Incorrect input. ")
    if positive_num.isdigit():
      if int(positive_num) < 0:
        positive_num = input("Try again: ")
        break


#    3. Fizzbuzz

# One of the most common interview questions for entry-level programmers is the FizzBuzz test. Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.

# Write a program that prints the numbers from 1 to 100.
# For multiples of three print "Fizz" instead of the number
# For the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('Fizzbuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)




# Display a table of powers.

# Prompt the user to enter an integer. Display a table of squares and 
# cubes from 1 to the value entered. Ask if the user wants to continue. 
# Assume that the user will enter valid data. Only continue if the user agrees to.

# Teacher example

while True:
    posited_num = input('Please insert a positive integer: ')
    if posited_num.isdigit():
        if int(posited_num) > 0:
            break
proceed = input('Do you want to continue and print a table of powers? :')
if proceed.lower().startswith('y'):
    posited_num = int(posited_num)
    print()
    print('number | squared | cubed')
    print('------ | ------- | -----')
    for i in range(1, posited_num + 1):
        i_squared = i ** 2
        i_cubed = i ** 3
        print(f'{i: 6} | {i_squared: 7} | {i_cubed: 5}')


# Convert given number grades into letter grades.

# Prompt the user for a numerical grade from 0 to 100. Display the corresponding 
# letter grade. Prompt the user to continue. Assume that the user will enter valid 
# integers for the grades. The application should only continue if the user agrees to.

# Grade Ranges:

#  A : 100 - 88
#  B : 87 - 80
#  C : 79 - 67
#  D : 66 - 60
#  F : 59 - 0



while True:
    user_number = input("Please enter your grade")
    if user_number.isdigit():
        user_number = int(user_number)
        if user_number < 0 or user_number > 100: 
            continue
        break
if grade in range(60):
    grade = 'F'
elif grade in range(60,67):
    grade = 'D'
elif grade in range(67,80):
    grade = 'C'
elif grade in range(80,88):
    grade = 'B'
else:
    grade = 'A'





