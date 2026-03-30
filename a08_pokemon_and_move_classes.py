#Team Members: Elijah Palmer, Maddox Swift, Zachary Worthington, [Name 4]

import random

# ============================================================
# Maddox: Create the Move class
# ============================================================

class Move:
    def __init__(self, move_name, elemental_type, low_attack_points, high_attack_points):
        
        #Initialize instance variables
        self.move_name = move_name
        self.elemental_type = elemental_type
        self.low_attack_points = low_attack_points
        self.high_attack_points = high_attack_points

    def get_info(self):
        # Return formatted string:
        # "<move name> (Type: <elemental type>): <low> to <high> Attack Points"
        return f'{self.move_name} (Type: {self.elemental_type}): {self.low_attack_points} to {self.high_attack_points}'

    def generate_attack_value(self):
        # TODO: Return a random int between low_attack_points and high_attack_points (inclusive)
        return random.randint(self.low_attack_points, self.high_attack_points)


# ============================================================
# Zachary Worthington: Create the Pokemon class
# ============================================================

class Pokemon:
    def __init__(self, name, elemental_type, hit_points):
        # Initialize instance variables
        self.name = name
        self.elemental_type = elemental_type
        self.hit_points = hit_points

    def get_info(self):
        # Return formatted string
        return f"{self.name} - Type: {self.elemental_type} - Hit Points: {self.hit_points}"

    def heal(self):
        # Add 15 to hit_points and print updated message
        self.hit_points += 15
        print(f"{self.name} has been healed to {self.hit_points} hit points.")


# ============================================================
# PERSON 3: Create Move objects, list, and loop (Part 1 logic)
# ============================================================

# TODO: Create 9 Move objects using the table below:
# Name          | Type   | Low | High
# Tackle        | Normal | 5   | 20
# Quick Attack  | Normal | 6   | 25
# Slash         | Normal | 10  | 30
# Flamethrower  | Fire   | 5   | 30
# Ember         | Fire   | 10  | 20
# Water Gun     | Water  | 5   | 15
# Hydro Pump    | Water  | 20  | 25
# Vine Whip     | Grass  | 10  | 25
# Solar Beam    | Grass  | 18  | 27

tackle = None         # Replace None with Move(...)
quick_attack = None
slash = None
flamethrower = None
ember = None
water_gun = None
hydro_pump = None
vine_whip = None
solar_beam = None

# TODO: Put all 9 Move objects into a list
moves_list = []

# TODO: Loop 3 times:
#   - Randomly select a move from moves_list
#   - Print the result of get_info() on the selected move
#   - Print "Generated attack value: " + the result of generate_attack_value()
#   - Delete the selected move from the list (so it can't be picked again)
for i in range(3):
    pass

input("Press enter to continue...")


# ============================================================
# PERSON 4: Create Pokemon objects and run Part 2 logic
# ============================================================

# TODO: Create 3 Pokemon objects:
# Name       | Type  | Hit Points
bulbasaur = Pokemon("Bulbasaur", "Grass", 60)
charmander = Pokemon("Charmander", "Fire", 55)
squirtle = Pokemon("Squirtle", "Water", 65)


bulbasaur = None      # Replace None with Pokemon(...)
charmander = None
squirtle = None

# TODO: Print get_info() for Charmander
# TODO: Call heal() on Charmander
# TODO: Print get_info() for Charmander again (hit points should be higher)

# TODO: Put the 3 Pokemon objects in a list
pokemon_list = []

# TODO: Loop through pokemon_list and print get_info() for each one