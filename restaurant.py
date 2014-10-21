# Accept or reject generated tip percentage.
def accept_tip():
    enter_tip = raw_input("Do you want to use this percentage to calculate your tip? (yes/no) ")
    if enter_tip == "yes":
        print "accepted tip"
    elif enter_tip == "no":
        starting_tip = raw_input("Please enter the tip percentage (no '%' needed): ")
        starting_tip = float(starting_tip)
    else:
        print "You need to enter a yes or a no."
        accept_tip()

# Get user input on restaurant experience.
service_rating = raw_input("On a scale of 1 to 5 how would you rate the service? ")
if service_rating != ['1', '2', '3', '4', '5']:
    print "Rating needs to be a number between 1 and 5."
    service_rating = raw_input("On a scale of 1 to 5 how would you rate the service? ")
else:
    True

food_rating = raw_input("On a scale of 1 to 5 how would you rate the food? ")
if food_rating == ['1', '2', '3', '4', '5']:
    print "Rating needs to be a number between 1 and 5."
    food_rating = raw_input("On a scale of 1 to 5 how would you rate the food? ")
else:
    True

# Set data types to float for calculations.
print service_rating
service_rating = float(service_rating)
food_rating = float(food_rating)

# Set start tip percentage.
starting_tip = 10

# Calculate tip percentage based on food and service.
if service_rating == 1:
    starting_tip = starting_tip - 5
elif service_rating == 2:
    starting_tip = starting_tip - 2.5
elif service_rating == 3:
    starting_tip = starting_tip + 2.5
elif service_rating == 4:
    starting_tip = starting_tip + 3.5
else:
    starting_tip = starting_tip + 5

if food_rating == 1:
    starting_tip = starting_tip - 5
elif food_rating == 2:
    starting_tip = starting_tip - 2.5
elif food_rating == 3:
    starting_tip = starting_tip + 2.5
elif food_rating == 4:
    starting_tip = starting_tip + 3.5
else:
    starting_tip = starting_tip + 5

print "Your suggested tip percentage is:", "{0:.0f}%".format(starting_tip)

accept_tip()

# Get value of meal.
meal_cost = raw_input("Now let's figure out the tip is...\n What is the cost of the meal? ")
meal_cost = float(meal_cost)

# Print tip amount.
tip = meal_cost * (starting_tip/100)
print "${:.2f}".format(tip)
