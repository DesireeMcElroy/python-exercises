greeting = "Hello World"

print(greeting)

#  Identify the data type of the following values:
# 99.9 is a float
# "False" is a string
# False is a boolean
# '0' is a string
# 0 is an integer
# True is a boolean
# 'True' is a string
# [{}] is a list
# {'a': []} is a list?


# What data type would best represent:

# A term or phrase typed into a search box?
# If a user is logged in?
# A discount amount to apply to a user's shopping cart?
# Whether or not a coupon code is valid?
# An email address typed into a registration form?
# The price of a product?
# A Matrix?
# The email addresses collected from a registration form?
# Information about applicants to Codeup's data science program?


# For each of the following code blocks, read the expression and predict what the result of evaluating it would be, then execute the expression in your Python REPL.

'1' + 2 - Cannot concatenate a string and int
6 % 4 # - Will print 1
type(6 % 4) # - Will tell you the type which is int
type(type(6 % 4)) # - will print type 
'3 + 4 is ' + 3 + 4 # - cannot concatenate
0 < 0 # - false
'False' == False # prints false
True == 'True' # prints false
5 >= -5 # prints true
True or "42" # true
6 % 5 # 1
5 < 4 and 1 == 1 # false
'codeup' == 'codeup' and 'codeup' == 'Codeup' # false
4 >= 0 and 1 !== '1' # invalid syntax, can't compare string to integer
6 % 3 == 0 # true
5 % 2 != 0 # true
[1] + 2  # cannot concatenate list with int
[1] + [2] # [1, 2]
[1] * 2 # [1, 1]
[1] * [2] # can't multiply sequence by non-int of type 'list'
[] + [] == [] # true, because adding two empty sets equals an empty set
{} + {} # error: unsupported