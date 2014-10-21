# Get user input on restaurant experience.
service_rating = raw_input("On a scale of 1 to 5 how would you rate the service? ")
food_rating = raw_input("On a scale of 1 to 5 how would you rate the food? ")

# Set data types to float for calculations.
service_rating = float(service_rating)
food_rating = float(food_rating)

starting_tip = 10

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

def accept_tip():
    enter_tip = raw_input("Do you want to use this percentage to calculate your tip? (yes/no) ")
    if enter_tip == "yes":
        print "accepted tip"
    elif enter_tip == "no":
        starting_tip = raw_input("Please enter the tip percentage: ")
        starting_tip = float(starting_tip)
    else:
        print "You need to enter a yes or a no."
        accept_tip()

accept_tip()

# Get value of meal.
meal_cost = raw_input("Now let's figure out the tip is...\n What is the cost of the meal? ")
meal_cost = float(meal_cost)

tip = meal_cost * (starting_tip/100)
print tip
