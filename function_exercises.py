
# 1. Define a function named is_two. It should accept one input and return True if the passed 
# input is either the number or the string 2, False otherwise.

def is_two(n):
    if n == 2 or n == '2':
        return True
    else:
        return False
print(is_two(2))


# 2. Define a function named is_vowel. 
# It should return True if the passed string is a vowel, False otherwise.

def is_vowel(a):
    if a in 'aeiouAEIOU':
        return True
    else:
        return False
print(is_vowel('i'))

# 3. Define a function named is_consonant. It should return True if the passed string 
# is a consonant, False otherwise. Use your is_vowel function to accomplish this.

def is_consonant(b):
    if is_vowel(b) == False:
        return True
print(is_consonant('q'))


# 4. Define a function that accepts a string that is a word. The function should 
# capitalize the first letter of the word if the word starts with a consonant.

def capitalize_word(n):
    if n[0] not in 'aeiouAEIOU':
        n = n.capitalize()
    return n
print(capitalize_word('potato'))


# 5. Define a function named calculate_tip. It should accept a tip percentage 
# (a number between 0 and 1) and the bill total, and return the amount to tip.


def calculate_tip(tip_percentage, bill_total):
    tip = tip_percentage * bill_total
    return tip
print(calculate_tip(0.25, 100))


# 6. Define a function named apply_discount. It should accept a original price, 
# and a discount percentage, and return the price after the discount is applied.

def apply_discount(original_price, discount_percentage):
    discount = original_price * discount_percentage
    return original_price - discount

print('Price after discount is: ', apply_discount(100, .30))



# 7. Define a function named handle_commas. It should accept a string that is a 
# number that contains commas in it as input, and return a number as output.

def handle_commas(n):
    num = n.replace(',', '')
    return int(num)
print(handle_commas('6,000,000'))


# 8. Define a function named get_letter_grade. It should accept a number and 
# return the letter grade associated with that number (A-F).

def get_letter_grade(grade):
    if grade < 60:
        return 'F'
    elif grade < 70:
        return 'D'
    elif grade < 80:
        return 'C'
    elif grade < 90:
        return 'B'
    elif grade < 101:
        return 'A'
    elif grade > 100:
        return 'Invalid'

print(get_letter_grade(99))



# 9. Define a function named remove_vowels that accepts a string and returns a 
# string with all the vowels removed.

def remove_vowels(n):
    vowel = 'aeiouAEIOU'
    for x in n:
        if x in vowel:
            n = n.replace(x, "")
    return n

print(remove_vowels('potato are good'))


# 10. Define a function named normalize_name. It should accept a string and return a 
# valid python identifier, that is:

# anything that is not a valid python identifier should be removed
# leading and trailing whitespace should be removed
# everything should be lowercase
# spaces should be replaced with underscores
# for example:
# Name will become name
# First Name will become first_name
# % Completed will become completed

def normalize_name(word):
    output = '' 
    word = word.lower()
    for let in word:
        if let.isidentifier() or let == ' ':
            output += let
    output = output.strip()
    output = output.replace(' ', '_')
    return output
print(normalize_name('6He_y crew123 !'))




# Exercise 11
# Write a function named cumulative_sum that accepts a list of numbers and returns a list 
# that is the cumulative sum of the numbers in the list.

# cumulative_sum([1, 1, 1]) returns [1, 2, 3]
# cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]


# def cumulative_sum(numbers):
#     output = []
    
#     # Enumerate gives us the index as well as the element at that index
#     for i, number in enumerate(numbers):
        
#         # Calculate the sum of the list up to and including the given index
#         sum_so_far = sum(numbers[:i + 1])
        
#         # append the sum_so_far to the output list
#         output.append(sum_so_far)
    
#     return output
# print(cumulative_sum([1, 2, 3, 4])
