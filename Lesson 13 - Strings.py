# Operators can be used to alter strings
import you as you

word1 = "hello"
word2 = "There"
print (word1 + " " + word2)  # adds the words together
print (word1 * 5)  # multiplies by 5 or repeats 5 times

#REMEBER, len only works on sting data types

# 'len' is a function in python which takes value, gives back number of characters.
# number retrieved can be stored in variable, see below:

name_length = len("Tahsin Hussain")

# My name stored as character (13 for name, 1 for space = 14) in variable

print (name_length)

# 14 will be outputted

# QUIZ - STRINGS (FIX THE QUOTE)

# TODO: Fix this string!
ford_quote = 'Whether you think you can, or you think you can\'t--you\'re right.'

print (ford_quote)

coconut_count = "34"
mango_count = "15"

tropical_fruit_count = coconut_count + mango_count
print (tropical_fruit_count)

# Will print 3415 as these are two strings and not integers (int would print 49).

# SECOND LAST QUIZ - WRITE SERVER LOG MESSAGE

username = "Kinari"
timestamp = "4:50"
url = "http://petshop.com/pets/mammals/cats"

print (username + " accessed the site " + url + " at " + timestamp + ".")

# FINAL QUIZ - len()

given_name = "William"
middle_names = "Bradley"
family_name = "Pitt"

name_length = len(given_name + middle_names + family_name) + 2

print (name_length)

# Now we check to make sure that the name fits within the driving license character limit
# Nothing you need to do here

driving_license_character_limit = 28
print (name_length >= driving_license_character_limit)
