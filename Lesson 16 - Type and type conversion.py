street_name = "The crescent"
house_number = 13
town_home = "Belmont"

print (type(street_name))

# in the statement above, (type(street_name)) will be run first and then print will execute
# In that particular order.

# The 3 variables can be outputted as a String (even if there are int data types

address = str(house_number) + " " + street_name + " " + town_home

# The code above outputs everything as one string statement (as str(house_number)
# which will output 13 to '13'.

# QUIZ - TOTAL SALES

mon_sales = "121"
tues_sales = "105"
wed_sales = "110"
thurs_sales = "98"
fri_sales = "95"

# TODO: Print a string with this format: This week's total sales: xxx
# You will probably need to write some lines of code before the print statement.

total_sales = + int(mon_sales) + int(tues_sales) + int(wed_sales) + int(thurs_sales) + int(fri_sales)

# First need a variable to hold int version of data, convert strings to int and add up

# Convert the variable to string for print output below:
total_sales = str(total_sales)
print ("This week's total sales are: " + total_sales)
