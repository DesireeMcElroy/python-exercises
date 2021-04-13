# IMPORT EXERCISES


# 1. Import and test 3 of the functions from your functions exercise file. 
# Import each function in a different way:

# 1a. Run an interactive python session and import the module. Call the is_vowel 
# function using the . syntax.

import function_exercises as fn

print(fn.is_vowel('b'))

# 1b. Create a file named import_exericses.py. Within this file, use from to import the 
# calculate_tip function directly. Call this function with values you choose and print the result.

from function_exercises import calculate_tip
print(calculate_tip(0.20, 100))

# 1c. Create a jupyter notebook named import_exercises.ipynb. Use from to import the get_letter_grade 
# function and give it an alias. Test this function in your notebook.


from function_exercises import get_letter_grade as grd
print(grd(85))


# 2. Read about and use the itertools module from the python standard library to help you solve the following problems:

# How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?

# import itertools
# print(itertools.product('abc', '123'))

# or


from itertools import product
print(len(list(product('abc', '123'))))
# answer is 9


# How many different combinations are there of 2 letters from "abcd"?

import itertools as it
print(len(list(it.combinations('abcd', 2))))
# answer is 6


# How many different permutations are there of 2 letters from "abcd"?

print(len(list(it.permutations('abcd', 2))))
# answer is 12





# 3. Use the load function from the json module to open this file.

import json
json.load(open('profiles.json'))

# print(json.keys())

# def total_number_of_users(x):
#     return len(x)
# print(total_number_of_users(x))
