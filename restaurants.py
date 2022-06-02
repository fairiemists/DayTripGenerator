import random

trees = ["evergreen"]
cars = ["ford"]


def random_item_picker(list):
    random_item = random.choice(list)
    return random_item

result = random_item_picker(trees)


result = random_item_picker(cars)