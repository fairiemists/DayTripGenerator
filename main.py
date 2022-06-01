import random

print()

# Need Lists for DESTINATION / RESTAURANT / MODE OF TRANSPORTATION / 
# FORM OF ENTERTAINMENT. 

# Need random generator for each list. 

# Would like to research restaurants/entertainment 
# specific to each destination. 

# Order of questions = entertainment/destination/transportation/restaurant

# add counter to say "there's only so many options" after 5 choices & loop back to choices ??

entertainments = ['on a wine, beer, or liquor tour', 'shopping', 'museum or gallery viewing', 'to a concert', 'sightseeing', 'hiking']
destinations = ["San Juan Islands", "Leavenworth", "Bellingham", "Gig Harbor", "Walla Walla"]
restaurants = ["Denny's", "Shari's", "Old Country Buffet", "Olive Garden", "a Teriyaki"]
transportations = ["car", "motorcycle", "rollerskates", "horseback", "bicycle"]



def choose_entertainment():
    random_entertainment = random.choice(entertainments)
    user_input = input(f"Would you like to go {random_entertainment}? Select y/n for yes/no. ")
    if user_input == "n":
        choose_entertainment()
    elif user_input == "y":
        print(f"Great! Going {random_entertainment} is a great idea!")
        return random_entertainment
    else:
        print("I'm sorry. I didn't understand that. Let me try something else. ")
        choose_entertainment()



def choose_destination():
    random_destination = random.choice(destinations)
    user_input = input(f"Would you like to go {selected_entertainment} in {random_destination}? Select y/n for yes/no. ")
    if user_input == "n":
        choose_destination()
    elif user_input == "y":
        print(f"{random_destination} is one of the best places to go {selected_entertainment}. ")
        return random_destination
    else: 
        print("I'm sorry. I didn't understand that. Let me try something else. ")
        choose_destination()


def choose_restaurant():
    random_restaurant = random.choice(restaurants)
    user_input = input(f"Would you like to eat at {random_restaurant} restaurant on your trip? Select y/n for yes/no. ")
    if user_input == "n":
        choose_restaurant()
    elif user_input == "y":
        print(f"{random_restaurant} restaurant is one of my favorites. Good choice! ")
        return random_restaurant
    else: 
        print("I'm sorry. I didn't understand that. Let me try something else. ")
        choose_restaurant()


def choose_transportation():
    random_transportation = random.choice(transportations)
    user_input = input(f"Would you like to get around by {random_transportation} during your trip? Select y/n for yes/no. ")
    if user_input == "n": 
        choose_transportation()
    elif user_input == "y":
        print(f"By {random_transportation} sounds like a fun way to get around. ") 
        return random_transportation
    else: 
        print("I'm sorry. I didn't understand that. Let me try something else. ")


print("Having difficulty planning your weekend? I can help!")

selected_entertainment = choose_entertainment()
selected_destination = choose_destination()
selected_restaurant = choose_restaurant()
selected_transportation = choose_transportation()

print(f"Let's see here. For your daytrip you have chosen to go {selected_entertainment} in {selected_destination} and eating at {selected_restaurant} restaurant. ")
print(f"You'll also be getting around by {selected_transportation} throughout the day. This sounds like fun! ")
user_input = input(f"Your daytrip looks complete. Would you like to lock in your choices? Select y/n for yes/no. ")
if user_input == "y":
    print(f"Yay! Congratulations! Enjoy the fun daytrip you have planned. ")
elif user_input == "n":
    print("That's okay. Let's start over. ")
    choose_entertainment()
else: 
    print("I'm sorry. I didn't understand that. ")
    user_input = input(f"Would you like to lock in your choices? Select y/n for yes/no. ")





