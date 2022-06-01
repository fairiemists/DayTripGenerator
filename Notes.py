import random

print()

# Need Lists for DESTINATION / RESTAURANT / MODE OF TRANSPORTATION / 
# FORM OF ENTERTAINMENT. 

# Need random generator for each list. 

# Would like to research restaurants/entertainment 
# specific to each destination. 

# Order of questions = Destination/transportation/entertainment/restaurant



# 1:1 Meeting

destinations = ["San Juan Islands", "Leavenworth", "Bellingham", "Gig Harbor", "Walla Walla"]

def select_destination():
    rand_dest = random.choice(destinations)
    user_input = input(f'Your destination is {rand_dest}')
    if user_input == "y":
        select_destination()
    if user_input == 'n':
        return rand_dest

selected_destination = select_destination()