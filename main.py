

import random

# List of options
trip_destinations = ['Kenya, Africa', 'Crete, Greece', 'Verona, Italy', 'Bonn, Germany', 'Mallorca, Spain']
best_restaurants = ['Luigis', 'Carellis', 'Ocean 44', 'Protos Pizza', 'Sushi SaSa']
best_transportations = ['Uber', 'Electric Scooter', 'Bus', 'Train', 'Walk']
best_entertainments = ['Museum', 'Skydiving', 'Paint and Sip Classes', 'Rock Climbing', 'Carnival']

# Function to randomly re-select an option
def reselect_option(option_list, current_option):
    new_option = random.choice(option_list)
    while new_option == current_option:
        new_option = random.choice(option_list)
    return new_option

# Function to print the options
def print_options(destination, restaurant, transportation, entertainment):
    print(f'Destination: {destination}')
    print(f'Restaurant: {restaurant}')
    print(f'Transportation: {transportation}')
    print(f'Entertainment: {entertainment}')

# Function to prompt user for re-selection
def prompt_reselection(message):
    choice = input(message)
    return choice.lower() == 'y'

# Loop until user is satisfied
while True:
    # Randomly select initial options
    destination = random.choice(trip_destinations)
    restaurant = random.choice(best_restaurants)
    transportation = random.choice(best_transportations)
    entertainment = random.choice(best_entertainments)

    # Print initial options
    print_options(destination, restaurant, transportation, entertainment)

    # Prompt user for re-selection
    reselect = prompt_reselection('Do you want to re-select any options? (y/n): ')

    if not reselect:
        break

    # Process re-selection
    if prompt_reselection('Do you want to re-select the destination? (y/n): '):
        destination = reselect_option(trip_destinations, destination)

    if prompt_reselection('Do you want to re-select the restaurant? (y/n): '):
        restaurant = reselect_option(best_restaurants, restaurant)

    if prompt_reselection('Do you want to re-select the mode of transportation? (y/n): '):
        transportation = reselect_option(best_transportations, transportation)

    if prompt_reselection('Do you want to re-select the form of entertainment? (y/n): '):
        entertainment = reselect_option(best_entertainments, entertainment)

    print() 

# Print final options
print(f'Final Trip:')
print(f'Destination: {destination}')
print(f'Restaurant: {restaurant}')
print(f'Transportation: {transportation}')
print(f'Entertainment: {entertainment}')