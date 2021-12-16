# This lesson covers variables. You know why this shit important

mv_population = 74728

# Assigning multiple variables:

x, y, z = 2, 3, 5

# x = 2, y = 3, z = 5 - quick way of assigning amirite but not descriptive

# Say 4000 people move in but 650 people move out of MV, can be updated as such:


mv_population = mv_population + 4000 - 600

print (mv_population)
# Can shorthand this to:

mv_population += 4000 - 650
mv_population -= 4000 - 650  # Opposite of +=

print (mv_population)

# QUIZ FOR VARIABLES:

# The current volume of a water reservoir (in cubic metres)
reservoir_volume = 4.445e8
# The amount of rainfall from a storm (in cubic metres)
rainfall = 5e6

# decrease the rainfall variable by 10% to account for runoff

rainfall *= 0.9

# add the rainfall variable to the reservoir_volume variable

reservoir_volume += rainfall

# increase reservoir_volume by 5% to account for stormwater that flows
# into the reservoir in the days following the storm

reservoir_volume *= 1.05

# decrease reservoir_volume by 5% to account for evaporation

reservoir_volume *= 0.95

# subtract 2.5e5 cubic metres from reservoir_volume to account for water
# that's piped to arid regions.

reservoir_volume -= 2.5e5

# print the new value of the reservoir_volume variable

print (reservoir_volume)

#Link to the lesson and quiz : https://classroom.udacity.com/courses/ud1110/lessons/23fc3d8b-a2a4-48ba-aada-652b2c216f2e/concepts/0edf3cc8-5c35-43a9-bd6e-d410f0ad2978



