# Data Types and Variables Exercises
 


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






