# Python 101_exercises




# Exercise 1
# On the line below, create a variable named on_mars_right_now and assign it the boolean value of False

on_mars_right_now = False

assert on_mars_right_now == False, "If you see a Name Error, be sure to create the variable and assign it a value."
print("Exercise 1 is correct.")





# Exercise 2
# Create a variable named fruits and assign it a list of fruits containing the following fruit names as strings: 
# mango, banana, guava, kiwi, and strawberry.

fruits = ["mango", "banana", "guava", "kiwi", "strawberry"]

assert fruits == ["mango", "banana", "guava", "kiwi", "strawberry"], "If you see an Assert Error, ensure the variable contains all the strings in the provided order"
print("Exercise 2 is correct.")




# Exercise 3
# Create a variable named vegetables and assign it a list of fruits containing the following vegetable names as strings: 
# eggplant, broccoli, carrot, cauliflower, and zucchini

vegetables = ["eggplant", "broccoli", "carrot", "cauliflower", "zucchini"]

assert vegetables == ["eggplant", "broccoli", "carrot", "cauliflower", "zucchini"], "Ensure the variable contains all the strings in the provided order"
print("Exercise 3 is correct.")




# Exercise 4
# Create a variable named numbers and assign it a list of numbers, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

assert numbers == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "Ensure the variable contains the numbers 1-10 in order."
print("Exercise 4 is correct.")




# Exercise 5
# Given the following assigment of the list of fruits, add "tomato" to the end of the list. 

fruits = ["mango", "banana", "guava", "kiwi", "strawberry"]
fruits.append('tomato')

assert fruits == ["mango", "banana", "guava", "kiwi", "strawberry", "tomato"], "Ensure the variable contains all the strings in the right order"
print("Exercise 5 is correct")




# Exercise 6
# Given the following assignment of the vegetables list, add "tomato" to the end of the list.

vegetables = ["eggplant", "broccoli", "carrot", "cauliflower", "zucchini"]
vegetables.append('tomato')


assert vegetables == ["eggplant", "broccoli", "carrot", "cauliflower", "zucchini", "tomato"], "Ensure the variable contains all the strings in the provided order"
print("Exercise 6 is correct")




# Exercise 7
# Given the list of numbers defined below, reverse the list of numbers that you created above. 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers.reverse()


assert numbers == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], "Assert Error means that the answer is incorrect." 
print("Exercise 7 is correct.")




# Exercise 8
# Sort the vegetables in alphabetical order
vegetables.sort()


assert vegetables == ['broccoli', 'carrot', 'cauliflower', 'eggplant', 'tomato', 'zucchini']
print("Exercise 8 is correct.")




# Exercise 9
# Write the code necessary to sort the fruits in reverse alphabetical order
fruits.sort(reverse=True)

assert fruits == ['tomato', 'strawberry', 'mango', 'kiwi', 'guava', 'banana']
print("Exercise 9 is correct.")




# Exercise 10
# Write the code necessary to produce a single list that holds all fruits then all vegetables in 
# the order as they were sorted above.

# fruits_and_veggies = fruits.extend(vegetables)
# print(fruits_and_veggies)

fruits_and_veggies = fruits + vegetables


assert fruits_and_veggies == ['tomato', 'strawberry', 'mango', 'kiwi', 'guava', 'banana', 'broccoli', 'carrot', 'cauliflower', 'eggplant', 'tomato', 'zucchini']
print("Exercise 10 is correct")




# Run this cell in order to generate some numbers to use in our functions after this.
import random
    
positive_even_number = random.randrange(2, 101, 2)
negative_even_number = random.randrange(-100, -1, 2)

positive_odd_number = random.randrange(1, 100, 2)
negative_odd_number = random.randrange(-101, 0, 2)
print("We now have some random numbers available for future exercises.")
print("The random positive even number is", positive_even_number)
print("The random positive odd nubmer is", positive_odd_number)
print("The random negative even number", negative_even_number)
print("The random negative odd number", negative_odd_number)


# Example function defintion:
# Write a say_hello function that adds the string "Hello, " to the beginning and "!" to the end of any given input.
def say_hello(name):
    return "Hello, " + name + "!"

assert say_hello("Jane") == "Hello, Jane!", "Double check the inputs and data types"
assert say_hello("Pat") == "Hello, Pat!", "Double check the inputs and data types"
assert say_hello("Astrud") == "Hello, Astrud!", "Double check the inputs and data types"
print("The example function definition ran appropriately")


# Another example function definition:
# This plus_two function takes in a variable and adds 2 to it.
def plus_two(number):
    return number + 2


assert plus_two(3) == 5
assert plus_two(0) == 2
assert plus_two(-2) == 0
print("The plus_two assertions executed appropriately... The second function definition example executed appropriately.")





# Exercise 11
# Write a function definition for a function named add_one that takes in a number and returns 
# that number plus one.
def add_one(number):
    return number + 1


    
assert add_one(2) == 3, "Ensure that the function is defined, named properly, and returns the correct value"
assert add_one(0) == 1, "Zero plus one is one."
assert add_one(positive_even_number) == positive_even_number + 1, "Ensure that the function is defined, named properly, and returns the correct value"
assert add_one(negative_odd_number) == negative_odd_number + 1, "Ensure that the function is defined, named properly, and returns the correct value"
print("Exercise 11 is correct.")





# Exercise 12
# Write a function definition named is_positive that takes in a number and returns True or False if that number is positive.

def is_positive(number):
    if number > 0:
        return True
    else:
        return False



assert is_positive(positive_odd_number) == True, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_positive(positive_even_number) == True, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_positive(negative_odd_number) == False, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_positive(negative_even_number) == False, "Ensure that the function is defined, named properly, and returns the correct value"
print("Exercise 12 is correct.")




# Exercise 13
# Write a function definition named is_negative that takes in a number and returns True or False if that number is negative.

def is_negative(number):
    return number < 0

assert is_negative(positive_odd_number) == False, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_negative(positive_even_number) == False, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_negative(negative_odd_number) == True, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_negative(negative_even_number) == True, "Ensure that the function is defined, named properly, and returns the correct value"
print("Exercise 13 is correct.")




# Exercise 14
# Write a function definition named is_odd that takes in a number and returns True or False if that number is odd.

def is_odd(number):
    return number % 2 == 1


assert is_odd(positive_odd_number) == True, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_odd(positive_even_number) == False, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_odd(negative_odd_number) == True, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_odd(negative_even_number) == False, "Ensure that the function is defined, named properly, and returns the correct value"
print("Exercise 14 is correct.")






# Exercise 43
# Write a function definition named is_vowel that takes in value and returns True if the 
# value is a, e, i, o, u in upper or lower case.
def is_vowel(letter):
    if letter in 'aeiouAEIOU':
        return True
    else:
        return False

# or

# def is_vowel(char):
#     all_vowels = 'aeiouAEIOU'
#     return char in all_vowels

assert is_vowel("a") == True
assert is_vowel("U") == True
assert is_vowel("banana") == False
assert is_vowel("Q") == False
assert is_vowel("y") == False
print("Exercise 43 is correct.")



# Exercise 44
# Write a function definition named has_vowels that takes in value and returns True if 
# the string contains any vowels.
def has_vowels(word):
    for n in word:
        if n in 'aeiouAEIOU':
            return True
        else:
            return False

# or
# def has_vowels(char):
#     return any(c in char for c in 'aeiou')

# assert has_vowels("banana") == True
# assert has_vowels("ubuntu") == True
# assert has_vowels("QQQQ") == False
# assert has_vowels("wyrd") == False
# print("Exercise 44 is correct.")





# Exercise 54
# Write a function definition named last that takes in sequence and returns the last value 
# of that sequence.
def last(word):
    return word[-1]


# or 

# def last(string):
#     end=len(string)-1
#     return string[end]
    

assert last("ubuntu") == "u"
assert last([1, 2, 3, 4]) == 4
assert last(["python", "is", "awesome"]) == "awesome"
assert last(["kiwi", "mango", "guava"]) == "guava"
print("Exercise 54 is correct.")




# Exercise 68
# Write a function definition named only_even_numbers that takes in sequence of 
# numbers and returns the even numbers in a list.

def only_even_numbers(number):
    evens = []
    for i in number:
        if i % 2 == 0:
            evens.append(i)
    return evens



assert only_even_numbers([1, 2, 3]) == [2]
assert only_even_numbers([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]) == [-4, -2, 2, 4]
assert only_even_numbers([-4, -3, 1]) == [-4]
print("Exercise 68 is correct.")






# Exercise 70
# Write a function definition named only_negative_numbers 
# that takes in sequence of numbers and returns the negative numbers in a list.

def only_negative_numbers(number):
    negatives = []
    for i in number:
        if i < 0:
            negatives.append(i)
    return negatives



assert only_negative_numbers([1, 2, 3]) == []
assert only_negative_numbers([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]) == [-5, -4, -3, -2, -1]
assert only_negative_numbers([-4, -3, 1]) == [-4, -3]
print("Exercise 70 is correct.")



# Run this cell in order to have some setup data for the next exercises
books = [
    {
        "title": "Genetic Algorithms and Machine Learning for Programmers",
        "price": 36.99,
        "author": "Frances Buontempo"
    },
    {
        "title": "The Visual Display of Quantitative Information",
        "price": 38.00,
        "author": "Edward Tufte"
    },
    {
        "title": "Practical Object-Oriented Design",
        "author": "Sandi Metz",
        "price": 30.47
    },
    {
        "title": "Weapons of Math Destruction",
        "author": "Cathy O'Neil",
        "price": 17.44
    }
]


# Exercise 91
# Write a function named get_number_of_books that takes in a list of objects 
# and returns the number of dictionaries in that list.

def get_number_of_books(numbers):
    return len(numbers)


assert get_number_of_books(books) == 4
print("Exercise 91 is complete.")




# Exercise 92
# Write a function named total_of_book_prices that takes in a list of 
# dictionaries and returns the sum total of all the book prices added together

def total_of_book_prices(number):
    total = 0
    for i in number:
        total = total + number[i]['price']
    return total



assert total_of_book_prices(books) == 122.9
print("Exercise 92 is complete.")