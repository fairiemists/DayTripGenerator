import random

print()


# Would like to research restaurants/entertainment specific to each destination. 

# add counter to say "there's only so many options" after 5 choices & loop back to choices ??

entertainments = ['on a wine, beer, or liquor tour', 'shopping', 'museum or gallery viewing', 'to a concert', 'sightseeing', 'hiking']
destinations = ["San Juan Islands", "Leavenworth", "Bellingham", "Gig Harbor", "Walla Walla"]
restaurants = ["Denny's", "Shari's", "Old Country Buffet", "Olive Garden", "a teriyaki", "a steakhouse"]
transportations = ["car", "motorcycle", "rollerskates", "horseback", "bicycle"]



def choose_entertainment():
    random_entertainment = random.choice(entertainments)
    user_input = ()
    while user_input != "y": 
        user_input = input(f"Would you like to go {random_entertainment}? Select y/n for yes/no. ")
        if user_input == "y": 
            print(f"Great! Going {random_entertainment} is a great idea!")
            return random_entertainment
        else: 
            print("Let's try that again. ")
            random_entertainment = random.choice(entertainments)    



def choose_destination(selected_entertainment):
    random_destination = random.choice(destinations)
    user_input = ()
    while user_input != "y":
        user_input = input(f"Would you like to go {selected_entertainment} in {random_destination}? Select y/n for yes/no. ")
        if user_input == "y":
            print(f"{random_destination} is one of the best places to go {selected_entertainment}. ")
            return random_destination
        else: 
            print("Let's try that again. ")
            random_destination = random.choice(destinations)



def choose_restaurant():
    random_restaurant = random.choice(restaurants)
    user_input = ()
    while user_input != "y":
        user_input = input(f"Would you like to eat at {random_restaurant} restaurant on your trip? Select y/n for yes/no. ")
        if user_input == "y":
            print(f"{random_restaurant} restaurant is one of my favorites. Good choice! ")
            return random_restaurant
        else: 
            print("Let's try that again. ")
            random_restaurant = random.choice(restaurants)


def choose_transportation():
    random_transportation = random.choice(transportations)
    user_input = ()
    while user_input != "y":
        user_input = input(f"Would you like to get around by {random_transportation} during your trip? Select y/n for yes/no. ")
        if user_input == "y":
            print(f"That sounds like a fun way to get around. ")
            return random_transportation
        else:
            print("Let's try that again. ")
            random_transportation = random.choice(transportations)


def run_planner():
    print()
    selected_entertainment = choose_entertainment()
    print()
    selected_destination = choose_destination(selected_entertainment)
    print()
    selected_restaurant = choose_restaurant()
    print()
    selected_transportation = choose_transportation()
    print()
    confirm_plan(selected_entertainment, selected_destination, selected_restaurant, selected_transportation)


def confirm_plan(selected_entertainment, selected_destination, selected_restaurant, selected_transportation):
    print()
    print(f"Let's see here. For your daytrip you have chosen to go {selected_entertainment} in {selected_destination} then dining at {selected_restaurant} restaurant. ")
    print(f"You'll also be getting around by {selected_transportation} throughout the day. This sounds like fun! ")
    print()

    user_input = ()
    while user_input != "y":
        user_input = input(f"Your daytrip looks complete. Would you like to lock in your choices? Select y/n for yes/no. ")
        if user_input == "n":
            print("That's okay. Let's start over. ")
            return run_planner()
        if user_input == "y":
            print("Yay! Congratulations! Enjoy the fun trip you have planned. ")
            break
        else:
            print("I'm sorry. I didn't understand that. ")



print("Having difficulty planning your weekend? I can help!")
run_planner()



