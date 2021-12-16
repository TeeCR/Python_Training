#   This lesson looking at bool (boolean - true and false).

NameOfPerson = "Jessica"

#   Types of comparison operators - these operators compare two values

5 < 3  # Less than
5 > 3  # More than
3 <= 3  # Less than or equal to
3 >= 3  # more than or equal to
3 == 5  # equal to
3 != 5  # Not equal to

#   Logical operators

#           |Boolean|

5 < 3 and 5 == 5  # False     'AND' Evaluates ALL statement to see if true
5 < 3 or 5 == 5  # True     'OR' Evaluates to see if one OR the other is true
not 5 < 3  # True   'NOT' FLIPS the boolean value

#   QUIZ - BOOLEAN

sf_population, sf_area = 864816, 231.89
rio_population, rio_area = 6453682, 486.5

san_fransisco_pop_density = sf_population / sf_area
rio_de_janeiro_pop_density = rio_population / rio_area

# Write code that prints True if San Francisco is denser than Rio, and False otherwise

# print ("SF population: ", san_fransisco_pop_density, " and Rio population: ", rio_de_janeiro_pop_density)

print (san_fransisco_pop_density > rio_de_janeiro_pop_density)

# comparison operators use '==' to compare as '=' is used to assign value to variables

