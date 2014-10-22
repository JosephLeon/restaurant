"""
Restaurant service based tip calculator.

Adjusts the tip based on food and service quality. Will upload the rating to a
site so users can see a restaurants average tip and ratings.
"""

# Accept or reject generated tip percentage.
def accept_tip():
    global starting_tip
    enter_tip = raw_input("Do you want to use this percentage to calculate your tip? (yes/no) ")
    if enter_tip == "yes":
        print "accepted tip"
    elif enter_tip == "no":
        starting_tip = float(raw_input("Please enter the tip percentage (no '%' needed): "))
    else:
        print "You need to enter a yes or a no."
        accept_tip()
    return starting_tip

def adjust_tip(rating):
    global starting_tip
    if rating == 1:
        starting_tip = starting_tip - 5
    elif rating == 2:
        starting_tip = starting_tip - 2.5
    elif rating == 3:
        starting_tip = starting_tip + 2.5
    elif rating == 4:
        starting_tip = starting_tip + 3.5
    else:
        starting_tip = starting_tip + 5
    return starting_tip

# Get user input on restaurant experience.
while True:
    try:
        service_rating = int(raw_input("On a scale of 1 to 5 how would you rate the service? "))
    except ValueError:  # just catch the exceptions you know!
        print 'That\'s not a number!'
    else:
        if 1 <= service_rating <= 5:  # this is faster
            break
        else:
            print 'Out of range. Try again'

while True:
    try:
        food_rating = int(raw_input("On a scale of 1 to 5 how would you rate the food? "))
    except ValueError:  # just catch the exceptions you know!
        print 'That\'s not a number!'
    else:
        if 1 <= food_rating <= 5:  # this is faster
            break
        else:
            print 'Out of range. Try again'

# Set data types to float for calculations.
service_rating = float(service_rating)
food_rating = float(food_rating)

# Set start tip percentage.
starting_tip = 10

# Calculate tip percentage based on food and service.
adjust_tip(service_rating)
adjust_tip(food_rating)

print "Your suggested tip percentage is:", "{0:.0f}%".format(starting_tip)

# User decides if to accept tip.
accept_tip()

# Get value of meal.
meal_cost = raw_input("Now let's figure out the tip is...\n What is the cost of the meal? ")
meal_cost = float(meal_cost)

# Calculate tip amount and print it.
starting_tip = float(starting_tip)
tip = meal_cost * (starting_tip/100)
print "Tip: ${:.2f}".format(tip)
