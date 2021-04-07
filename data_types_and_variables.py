# Data Types and Variables Exercises
 

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


# For each of the following code blocks, read the expression and predict what the result of evaluating it would be, 
# then execute the expression in your Python REPL.

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


# You have rented some movies for your kids: The little mermaid (for 3 days), 
# Brother Bear (for 5 days, they love it), and Hercules (1 day, you don't know yet if 
# they're going to like it). If price for a movie per day is 3 dollars, 
# how much will you have to pay?

the_little_mermaid = 3
brother_bear = 5
hercules = 1

print(3 * (the_little_mermaid + brother_bear + hercules))


# Suppose you're working as a contractor for 3 companies: 
# Google, Amazon and Facebook, they pay you a different rate per hour. 
# Google pays 400 dollars per hour, Amazon 380, and Facebook 350. 
# How much will you receive in payment for this week? You worked 10 hours for Facebook, 
# 6 hours for Google and 4 hours for Amazon.

google_hour = 400
amazon_hour = 380
facebook_hour = 350

print(10 * facebook_hour + 6 * google_hour + 4 * amazon_hour)


# A student can be enrolled to a class only if the class is not full 
# and the class schedule does not conflict with her current schedule.

class_full = False
class_conflict = False
student_may_enroll = False # must assign false so if opposite is true, then print false

if (class_full == False) and (class_conflict == False):
    student_may_enroll = True
print(student_may_enroll)


# A product offer can be applied only if people buys more than 2 items, 
# and the offer has not expired. Premium members do not need to buy a 
# specific amount of products.

items_bought = 1 # the guyyy only bought 1 so he don't get no offer
required_items = 2
offer_expired = True
premium_member = True
product_offer = False # set to false originally so test conditions in program up for it to be true

if (offer_expired == False) and (items_bought > required_items):
    product_offer = True
if (premium_member == True) and (offer_expired == False):
    product_offer = True

print(product_offer)



# Create a variable that holds a boolean value for each of the following conditions:
# the password must be at least 5 characters
# the username must be no more than 20 characters
# the password must not be the same as the username
# bonus neither the username or password can start or end with whitespace

username = 'codeup'
password = 'notastrongpassword'

passlength = (len(password) >= 5)
userlength = (len(username) <= 20)
conflict = (username == password)
whitespace = ((username[0] == " ") or (username[-1] == " ") or (password[0] == " ") or (password[-1] == " "))

print(passlength, userlength, conflict, whitespace)



