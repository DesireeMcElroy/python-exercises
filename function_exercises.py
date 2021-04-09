
# Define a function named is_two. It should accept one input and return True if the passed 
# input is either the number or the string 2, False otherwise.

def is_two(n):
    if n == 2 or n == '2':
        return True
    else:
        return False
print(is_two(2))


# Define a function named is_vowel. 
# It should return True if the passed string is a vowel, False otherwise.

def is_vowel(a):
    if a in 'aeiouAEIOU':
        return True
    else:
        return False
print(is_vowel('i'))

# Define a function named is_consonant. It should return True if the passed string 
# is a consonant, False otherwise. Use your is_vowel function to accomplish this.

def is_consonant(b):
    if b not in 'aeiouAEIOU':
        return True
    else:
        return False
print(is_consonant('q'))


# Define a function that accepts a string that is a word. The function should 
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
print(calculate_tip(0.25, 465797))






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
        ....
    elif

print(get_letter_grade(99))